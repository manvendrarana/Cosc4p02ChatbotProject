import json
from threading import *

from haystack import Document
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import TableReader
from haystack.nodes.retriever import TableTextRetriever

"""
This class handles the Ai model initialization and Prediction on the queries.
For more info on Ai model used, 
please refer: 
https://haystack.deepset.ai/overview/intro
https://haystack.deepset.ai/tutorials/table-qa
"""


class Ai:

    def __printError(self, admin_req_id, error):
        """
        This method adds the error report to output buffer.
        If there is an admin request it includes the request id so that Node.js can reject it.
        :param admin_req_id: str
        :param error: str
        """
        if admin_req_id is not None:
            self.output_buffer.put(json.dumps({"type": "failed_admin",
                                               "id": admin_req_id,
                                               "error": error}))
        else:
            self.output_buffer.put(json.dumps({"type": "update",
                                               "component": "ai",
                                               "update": "error",
                                               "update_message": error}))

    def __processInfo(self):
        """
            This method converts the data sent by Database to Haystack processable data.
        """
        # Add the tables to the DocumentStore.
        self.output_buffer.put(json.dumps({"type": "update",
                                           "component": "ai",
                                           "update": "busy",
                                           "update_message": "Processing Documents"
                                           }))
        for key, table in self.tables.items():
            current_df = table["df"]
            current_doc_title = table["title"]
            current_section_title = table["section_title"]
            document = Document(
                content=current_df,
                content_type="table",
                meta={"title": current_doc_title, "section_title": current_section_title, "url": table["url"]},
                id=key,
            )
            self.processedTables.append(document)
        self.document_store.write_documents(self.processedTables, index="document")

    def __initPipeline(self):
        """
        This method initializes the table retriever and table reader.
        Table retriever retrieves top k matching docments from all documents stored in the DocumentManager.
        Table reader predicts the answer to the query on the retrieved table.
        """
        self.output_buffer.put(json.dumps({"type": "update",
                                           "component": "ai",
                                           "update": "busy",
                                           "update_message": "Initializing Pipeline"
                                           }))
        self.retriever = TableTextRetriever(
            document_store=self.document_store,
            query_embedding_model="deepset/bert-small-mm_retrieval-question_encoder",
            passage_embedding_model="deepset/bert-small-mm_retrieval-passage_encoder",
            table_embedding_model="deepset/bert-small-mm_retrieval-table_encoder",
            embed_meta_fields=["title", "section_title"],
        )

        # Add table embeddings to the tables in DocumentStore
        self.document_store.update_embeddings(retriever=self.retriever)
        self.reader = TableReader(model_name_or_path="google/tapas-large-finetuned-sqa", max_seq_len=512)
        self.output_buffer.put(json.dumps({"type": "update",
                                           "component": "ai",
                                           "update": "working",
                                           "update_message": "Ai Initialized"
                                           }))

    """
    This method removes all the dead threads that have predicted on a query.
    """

    def __clear_dead_processes(self):
        # only keep the alive processes
        self.ai_processes = [ai_process for ai_process in self.ai_processes if ai_process.is_alive()]

    """
    Overriding length function to return number of process currently running/dead.
    """

    def __len__(self):
        self.__clear_dead_processes()
        return len(self.ai_processes)

    """
    This method initializes the pipeline.
    """

    def __init__(self, data, output_buffer, admin_req_id=None):
        try:
            self.output_buffer = output_buffer
            self.tables = data
            self.retriever = None
            self.reader = None
            self.document_index = "document"
            self.document_store = InMemoryDocumentStore(embedding_dim=512)
            self.processedTables = []
            self.ai_processes = []
            self.__processInfo()
            self.__initPipeline()
        except BaseException as e:
            self.__printError(admin_req_id, 'Failed to initialize Ai, \n system message: {}'.format(e))

    """
    Updates the currently sored info and reinitializes the pipeline.
    """

    def updateData(self, data, admin_req_id=None):
        try:
            while self.__len__() > 0:  # wait for current requests to complete
                self.__clear_dead_processes()
            self.document_store = InMemoryDocumentStore(embedding_dim=512)
            self.processedTables = []
            self.tables = data
            self.__processInfo()
            self.__initPipeline()
        except BaseException as e:
            self.__printError(admin_req_id, "Failed to update the ai, system error {}".format(e))

    """
    This method creates a thread to predict on the query using the pipeline.
    """

    def ask(self, request, join, admin_req_id=None):
        try:
            msg_id, query = request
            if join:
                self.ai_processes[0].join()
                self.__clear_dead_processes()

            def threadFunction(query_msg, query_msg_id, output_buffer):
                try:
                    if query_msg is not None:
                        retrieved_tables = self.retriever.retrieve(query, top_k=1)
                        # Get highest scored table
                        retrieved_tables = [table for table in retrieved_tables if table.score >= 0.85]
                        if len(retrieved_tables) > 0:
                            # print(retrieved_tables[0].id)
                            table_doc = self.document_store.get_document_by_id(retrieved_tables[0].id)
                            prediction = self.reader.predict(query=query, documents=[table_doc])
                            answer = (" ".join([obj.answer for obj in prediction["answers"]])).strip()
                            if len(answer) > 0:
                                output = {"type": "ai_query",
                                          "id": query_msg_id,
                                          "url": table_doc.meta["url"],
                                          "title": table_doc.meta["title"],
                                          "answer": answer
                                          }
                                output_buffer.put(json.dumps(output))
                            else:
                                output = {"type": "ai_query",
                                          "id": query_msg_id,
                                          "url": table_doc.meta["url"],
                                          "title": table_doc.meta["title"],
                                          "answer": "The Ai was unable to retrieve info from the table please follow "
                                                    "the info link if available under this message. "
                                          }
                                output_buffer.put(json.dumps(output))
                        else:
                            output = {"type": "ai_query",
                                      "id": query_msg_id,
                                      "url": "N/A",
                                      "title": "N/A",
                                      "answer": "The Ai was unable to create a response for your question."
                                      }
                            output_buffer.put(json.dumps(output))
                except BaseException as e:
                    output = {"type": "ai_query",
                              "id": query_msg_id,
                              "url": "N/A",
                              "title": "N/A",
                              "answer": "Sorry the ai cannot process this query"
                              }
                    output_buffer.put(json.dumps(output))

            ai_thread = Thread(target=threadFunction, args=[query, msg_id, self.output_buffer])
            ai_thread.start()
            self.ai_processes.append(ai_thread)
        except BaseException as e:
            self.__printError(admin_req_id, "Ai did not process the query, system message {}".format(e))


dev_mode = False

if dev_mode:
    from components.database.db_helper import DbHelper
    import multiprocessing as mp

    output_buffer = mp.Queue()
    database = DbHelper("root", "e#uoo!5YPZMQ3G", output_buffer)  # sql username and password
    database.set_database("testDb")  # database name
    query_buffer = mp.Queue()
    max_ai_processes = 1  # max num of ai processes
    data = database.get_documents()
    ai = Ai(data, output_buffer)
    ai.ask(("123", "What is Athlete Avi Adam's height?"), len(ai) >= max_ai_processes)
    ai.ask(("123", "What is Athlete Avi Adam's coach?"), len(ai) >= max_ai_processes)
    ai.ask(("123", "Who is Athlete Adel Akhmed's age?"), len(ai) >= max_ai_processes)
    ai.ask(("123", "Who is Athlete Adel Akhmed's height?"), len(ai) >= max_ai_processes)
    ai.ask(("123", "Who is Athlete Ashley Anaka's coach?"), len(ai) >= max_ai_processes)
    ai.ask(("123", "How do i get there?"), len(ai) >= max_ai_processes)
    ai.ask(("123", "How can i find the bus?"), len(ai) >= max_ai_processes)
    ai.ask(("123", "tickets?"), len(ai) >= max_ai_processes)
    ai.ask(("123", "Where can i get the tickets?"), len(ai) >= max_ai_processes)
    ai.ask(("123", "Latest news on the canada games?"), len(ai) >= max_ai_processes)
    ai.ask(("123", "What was the score of ON in K 4 1000m Canoe event?"), len(ai) >= max_ai_processes)
    while not output_buffer.empty():
        print(output_buffer.get())
