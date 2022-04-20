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
    def __init__(self):
        self.scraped_data = None
        self.scraper = None
        self.busyTesting = False
        self.busyDb = False
        self.busyAi = False
        self.gettingDocuments = False
        self.database = DbHelper(sys.argv[1], sys.argv[2], output_buffer)  # sql username and password
        self.database.set_database(sys.argv[3])  # database name
        self.query_buffer = mp.Queue()
        self.max_ai_processes = int(sys.argv[4])  # max num of ai processes
        data = self.database.get_documents()
        self.ai = Ai(data, output_buffer)
        self.query_handler_thread = Thread()
        output_buffer.put(json.dumps({"type": "init",
                                      "message": "System is ready"}))

    def __add_ai_query(self, message):
        # What was the score of ON in K 4 1000m Canoe event?
        try:
            query = message["query"]
            msg_id = message["id"]
            self.query_buffer.put((msg_id, query))

            def threadFunction(max_processes, ai_obj):
                while self.busyAi:  # wait till ai update is complete
                    time.sleep(1)
                while not self.query_buffer.empty():
                    ai_obj.ask(self.query_buffer.get(), len(self.ai) >= max_processes)

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

    def scrape_pages(self, message):
        try:
            self.scraper = Scraper(output_buffer)
            if type(self.scraper) is not None:
                self.scraped_data = self.scraper.scrape()
                if type(self.database) == type(DbHelper):
                    self.database.set_documents(self.scraped_data)
            else:
                output_buffer.put(json.dumps({"type": "failed_admin",
                                              "message": message,
                                              "update_message": 'Scraper not initialized'
                                              }))
        except BaseException as e:
            output_buffer.put(json.dumps({"type": "update",
                                          "component": "scraper",
                                          "update": "error",
                                          "update_message": 'Failed to Scraper, \n system message: {}'.
                                         format(e)
                                          }))

    def __view_scraped_data(self, message):
        if not self.gettingDocuments:
            Thread(target=self.__get_all_documents_thread).start()

    def __change_max_ai_process(self, message):
        pass

    def __restart(self, message):
        pass

    def __system_test(self, message):
        if not self.busyTesting:
            def test_thread(self):
                pass

            pass

    def __get_all_documents_thread(self):  # to show documents on the front end in admin
        self.gettingDocuments = True
        while self.busyDb:  # db is being accessed
            time.sleep(1)
        self.accessingDb = True
        self.database.get_documents()
        self.accessingDb = False
        self.gettingDocuments = False

    def execute(self, message):
        switcher = {
            "ai_query": self.__add_ai_query,
            "scrape_pages": self.scrape_pages,
            "view_scraped_data": self.__view_scraped_data,
            "change_ai_max_process_by": self.__change_max_ai_process,
            "restart_system": self.__restart,
            "system_test": self.__system_test,
        }
        try:
            switcher[message["type"]](message)
        except:
            output_buffer.put(json.dumps({"type": "failed",
                                          "message": message,
                                          "reason": "Invalid query"}))


def output_message_handler():
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
