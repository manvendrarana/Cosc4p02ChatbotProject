import json
import multiprocessing as mp
import sys
import time
from threading import *

from ai.main import Ai
from database.db_helper import DbHelper
from scraping.Scraper import Scraper

output_buffer = mp.Queue()  # queue to manage all output messages


class Main:
    # self.database = DbHelper("root", "e#uoo!5YPZMQ3G", output_buffer)  # sql username and password
    # self.database.reset_database("testDb")
    # self.database.set_database("testDb")  # database name
    def __init__(self) -> None:
        """
            This is the initialization method.
            It initializes Db class and Ai class.
        """
        self.scraped_data = None
        self.scraper = None

        self.scraping = False
        self.updating = False
        self.gettingDocuments = False
        self.runningQueries = False

        self.database = DbHelper(sys.argv[1], sys.argv[2], output_buffer)  # sql username and password
        self.database.set_database(sys.argv[3])  # database name
        self.query_buffer = mp.Queue()
        self.max_ai_processes = int(sys.argv[4])  # max num of ai processes
        data = self.database.get_documents()
        self.ai = Ai(data, output_buffer)
        self.query_handler_thread = Thread()
        output_buffer.put(json.dumps({"type": "init",
                                      "message": "System is ready"}))

    def __add_ai_query(self, message: {}) -> None:
        """
        This method adds the query send by the customer to a buffer.
        It has a thread that runs if the input buffer is not empty.
        Thread runs the ask method of the Ai class.
        :param message: Message from Back end node js,
        format -> {
                    query: str,
                    id: str,
                }

        """
        # What was the score of ON in K 4 1000m Canoe event?
        if not self.updating:
            try:
                query = message["query"]
                msg_id = message["id"]
                self.query_buffer.put((msg_id, query))

                def threadFunction(max_processes, ai_obj):
                    self.runningQueries = True
                    while not self.query_buffer.empty():
                        ai_obj.ask(self.query_buffer.get(), len(self.ai) >= max_processes)
                    self.runningQueries = False

                if not self.query_handler_thread.is_alive():  # restart the thread if dead
                    self.query_handler_thread = Thread(target=threadFunction, args=[self.max_ai_processes, self.ai])
                    self.query_handler_thread.start()
            except BaseException as e:
                output_buffer.put(json.dumps({"type": "update",
                                              "component": "ai",
                                              "update": "error",
                                              "update_message": 'Failed to Process the query due to error'
                                                                ', \n system message: {}'.format(e)
                                              }))
                output_buffer.put(json.dumps({"type": "ai_query",
                                              "id": message["id"],
                                              "url": "N/A",
                                              "title": "N/A",
                                              "answer": "Sorry the ai cannot process this query"
                                              }))
        else:
            output_buffer.put(json.dumps({"type": "ai_query",
                                          "id": message["id"],
                                          "url": "N/A",
                                          "title": "N/A",
                                          "answer": "Sorry the server is updating it's knowledge. "
                                                    "Please try again after a while"
                                          }))

    def __view_scraped_data(self, message: {}) -> None:
        """
        This method converts the current scraped data dictionary to json and prints it back with the admin message
        id.
        Put to output buffer:
            onSuccess:
            {
                type: success_admin,
                id: message[id],
                data: JSON({})
            }
            onFailure:
            {
                type: failed_admin,
                id: message[id],
                error: str
            }
        :param message: Message sent by admin.
        format -> {
                    id: str
                }
        """

        def threadFunction():
            self.gettingDocuments = True
            while self.updating:  # wait till system being is updated
                time.sleep(1)
            # --------JSON PRINT LATEST SCRAPED DATA------------
            self.gettingDocuments = False

        Thread(target=threadFunction).start()

    def __change_max_ai_process(self, message: {}) -> None:
        """
        Changes the maximum number of threads for the Ai's predict method.
        With x threads the Ai can process x amount of queries concurrently.
        Put to output buffer:
            onSuccess:
            {
                type: success_admin,
                id: message[id]
            }
            onFailure:
            {
                type: failed_admin,
                id: message[id],
                error: str
            }
        :param message: Message from admin
            format -> {
                        value: int,
                        id: str,
                    }
        """
        self.max_ai_processes = max(0, self.max_ai_processes + int(message["value"]))

    def __scrape_pages(self, message: {}) -> None:
        """
        This method initializes the Scraper class and loads the returned info to scraped_data variable.
        Put to output buffer:
            onSuccess:
            {
                type: success_admin,
                id: message[id]
            }
            onFailure:
            {
                type: failed_admin,
                id: message[id],
                error: str
            }
        :param message: Message sent by the admin.
            format -> {
                        id: str
                    }
        """
        if not self.scraping:
            def threadFunction():
                self.scraping = True
                try:
                    self.scraper = Scraper(output_buffer)
                    self.scraped_data = self.scraper.scrape()
                    self.database.set_documents(self.scraped_data)
                    self.data = self.database.get_documents()
                    self.restarting = True
                    self.ai = Ai(self.data, output_buffer)
                    self.restarting = False
                    output_buffer.put(json.dumps({"type": "success_admin",
                                                  "id": message["id"]
                                                  }))
                except BaseException as e:
                    output_buffer.put(json.dumps({"type": "update",
                                                  "component": "scraper",
                                                  "update": "error",
                                                  "update_message": 'Failed to Scrape, \n system message: {}'.
                                                 format(e)
                                                  }))
                    output_buffer.put(json.dumps({"type": "failed_admin",
                                                  "id": message["id"],
                                                  "error": 'Failed to Scrape, \n system message: {}'.format(e)
                                                  }))
                self.scraping = False

            Thread(target=threadFunction).start()
        else:
            output_buffer.put(json.dumps({"type": "failed_admin",
                                          "id": message["id"],
                                          "error": "Already scraping"
                                          }))

    def __system_test(self, message: {}) -> None:
        """
        This method initializes the Test class.
        Output:
            onSuccess:
            {
                type: success_admin,
                id: message[id],
                passed: [str],
                failed: [str]
            }
            onFailure:
            {
                type: failed_admin,
                id: message[id],
                error: str
            }
        :param message: request sent by admin.
            format -> {
                        id: str
                    }
        """
        self.testing = True

        self.testing = False

    def execute(self, message: {}) -> None:
        """
        This method executes the type of request send by the Node.js server.
        :param message: message sent by customer/admin.
            format -> {
                        id: str
                    }
        """
        switcher = {
            "ai_query": self.__add_ai_query,
            "scrape_pages": self.__scrape_pages,
            "view_scraped_data": self.__view_scraped_data,
            "change_ai_max_process_by": self.__change_max_ai_process,
            "system_test": self.__system_test,
        }
        switcher[message["type"]](message)


def output_message_handler() -> None:
    """
        This method prints all the queued up messages in the output buffer.
    """
    while True:  # inefficient method :(
        while not output_buffer.empty():
            print(output_buffer.get())
        time.sleep(1)


Thread(target=output_message_handler).start()

dev_mode = True
main_obj = None
if dev_mode:
    sys.argv.append("root")
    sys.argv.append("e#uoo!5YPZMQ3G")
    sys.argv.append("testDb")
    sys.argv.append("1")
    main_obj = Main()
    main_obj.execute(json.loads(json.dumps({
        "type": "scrape_pages"
    })))

else:
    main_obj = Main()
    while True:
        main_obj.execute(json.loads(input()))
