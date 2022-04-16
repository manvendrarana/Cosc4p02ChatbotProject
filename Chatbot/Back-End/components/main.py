import json
import sys
import time

from scraping.Scraper import Scraper
from ai.main import Ai
from database.db_helper import DbHelper
import multiprocessing as mp
from threading import *

output_buffer = mp.Queue()  # queue to manage all output messages


class Main:

    def __init__(self):

        self.testing = False
        self.accessingDb = False
        self.updatingAi = False
        self.gettingDocuments = False
        self.database = DbHelper(sys.argv[1], sys.argv[2], output_buffer)  # sql username and password
        self.database.set_database(sys.argv[3])  # database name
        # self.database = DbHelper("root", "e#uoo!5YPZMQ3G", output_buffer)  # sql username and password
        # self.database.reset_database("testDb")
        # self.database.set_database("testDb")  # database name

        # self.scraper = Scraper(output_buffer)
        # data = self.scraper.scrape()
        # self.database.set_documents(data)

        self.query_buffer = mp.Queue()
        self.max_ai_processes = int(sys.argv[4])  # max num of ai processes
        data = self.database.get_documents()
        self.ai = Ai(data, output_buffer)
        self.query_handler_thread = Thread(target=self.query_handler, args=[self.max_ai_processes, self.ai])
        self.query_handler_thread.start()
        output_buffer.put(json.dumps({"type": "init",
                                      "message": "System is ready"}))

    def execute(self, message):
        switcher = {
            "ai_query": self.add_ai_query,
            "update_ai": self.update_ai,
            "show_db": self.get_all_documents,
            "test": self.test
        }
        try:
            switcher[message["type"]](message)
        except:
            output_buffer.put(json.dumps({"type": "failed",
                                          "message": message,
                                          "reason": "Invalid query"}))

    def get_all_documents(self, message):
        if not self.gettingDocuments:
            Thread(target=self.get_all_documents_thread).start()

    def update_ai(self, message):
        if not self.updatingAi:
            Thread(target=self.update_ai_thread).start()

    def test(self, message):
        if not self.testing:
            pass

    def add_ai_query(self, message):
        query = message["query"]
        msg_id = message["id"]
        self.query_buffer.put((msg_id, query))
        if not self.query_handler_thread.is_alive():  # restart the thread if dead
            self.query_handler_thread = Thread(target=self.query_handler, args=[self.max_ai_processes, self.ai])
            self.query_handler_thread.start()

    # ---------------------------- THREADED PROCESSES BEGIN -------------------------------------------

    def query_handler(self, max_processes, ai_obj):
        """
        This method is a Daemon thread for handling queries. It will run till query buffer is not empty
        :param max_processes:
        :param ai_obj:
        """
        while self.updatingAi:  # wait till ai update is complete
            time.sleep(1)
        while not self.query_buffer.empty():
            ai_obj.ask(self.query_buffer.get(), len(self.ai) >= max_processes)

    def update_ai_thread(self):
        # data = self.scraper.scrape()
        # ------Possible deadlock?-------
        while self.accessingDb:  # wait till db is free
            time.sleep(1)
        self.accessingDb = True
        # self.database.set_documents(data)
        data = self.database.get_documents()
        self.accessingDb = False
        # -----------------------------
        self.updatingAi = True
        self.ai.updateData(data)
        self.updatingAi = False
        output_buffer.put(json.dumps({"type": "update",
                                      "update_message": "Ai update completed",
                                      "component": "ai",
                                      "update": "working"}))

    def get_all_documents_thread(self):  # to show documents on the front end in admin
        self.gettingDocuments = True
        while self.accessingDb:  # db is being accessed
            time.sleep(1)
        self.accessingDb = True
        self.database.get_documents()
        self.accessingDb = False
        self.gettingDocuments = False

    def test_thread(self):
        pass

    # ---------------------------- THREADED PROCESSES END -------------------------------------------


def output_message_handler():
    while True:  # inefficient method :(
        while not output_buffer.empty():
            print(output_buffer.get())
        time.sleep(1)


Thread(target=output_message_handler).start()

main_obj = Main()

while True:
    main_obj.execute(json.loads(input()))

# sys.argv.append("root")
# sys.argv.append("e#uoo!5YPZMQ3G")
# sys.argv.append("testDb")
# sys.argv.append("1")
# main_obj.add_ai_query({"type": "ai_query", "id": 1, "query": "What was the score of ON in K 4 1000m Canoe event?"})
# main_obj.update_ai({"type": "update_ai"})
# main_obj.add_ai_query({"type": "ai_query", "id": 2, "query": "What was the score of Rowan Hardy-Kavanagh in C 1 200m "
#                                                              "female Canoe event?"})
# # ai.run("What are the runs of team new brunswick in baseball Group B Match 15?")
# # ai.run("Which events did New Brunswick participate in baseball group b?")
# # ai.run("Which matches did new brunswick participate in baseball group B?")
# # ai.run("Which matches did new brunswick participate in ?")
# # ai.run("How many points did Tiakotierenhton Diabo in Wrestling Individual Up to 60kg Female Placing?")
# # ai.run("What is the score of Rowan Hardy-Kavanagh in canoe events?")
# # ai.run("Which events did Rowan Hardy-Kavanagh participate in canoe?")
# # ai.run("What is the score of Brady Garcia in canoe events?")
# # ai.run("Which events did Brady Garcia participate in canoe?")
# # ai.run("What is the score of Hunter, Ydris in canoe events?")
# # ai.run("Which events did Hunter, Ydris participate in canoe?")
# # ai.run("What was the score of ON Canoe event?")
# # ai.run("What was the score of ON in K 4 1000m Canoe event?")
# # ai.run("What was the score of Gillian Ellsay in K 4 1000m Canoe event?")
# # ai.run("What are the participant names in the Mountain bike Cycling events")
# # ai.run("What is the time of Kayla Marwick in 100m freestyle swimming?")
# # ai.run("Which events did Kayla Marwick participate in swimming?")
# # ai.run("List all the events in canoe")
# # ai.run("Which athletes are participating in C 1 200m Female canoe")
# # ai.run("canoe")
