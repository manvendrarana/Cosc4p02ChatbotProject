import json
import time
from threading import Thread

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from components.ai.main import Ai
from components.database.db_helper import DbHelper
from components.scraping.modules.event import EventScraper
import multiprocessing as mp

output_buffer = mp.Queue()


# service = ChromeService(executable_path="./scraping/chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# scraper_obj = EventScraper(driver)
# canoekayak_urls = scraper_obj.get_names_and_urls(
#     "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=1c3ac9b6-46f3-402e-bc15-b0fd0afb6a1d"
#     "&SetLanguage=en-CA")
# documents = scraper_obj.sports(main_section="canoe", main_url="not available", urls=canoekayak_urls,
#                                  columns=["score"])
# output = scraper_obj.get_names_and_urls(
#     "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=1c3ac9b6-46f3-402e-bc15-b0fd0afb6a1d&SetLanguage=en-CA")
#
# with open('testing/data/test_scraper_event_getNamesAndUrls.json', 'w') as f:
#     json.dump(output, f, indent=4, sort_keys=True)
# driver.close()

def query_handler(max_processes, ai_obj):
    """
    This method is a Daemon thread for handling queries. It will run till query buffer is not empty
    :param max_processes:
    :param ai_obj:
    """
    query_buffer = mp.Queue()
    while not query_buffer.empty():
        ai_obj.ask(query_buffer.get(), len(ai_obj) >= max_processes)


database = DbHelper("root", "e#uoo!5YPZMQ3G", output_buffer)  # sql username and password
database.reset_database("testDb")

data = database.get_documents()
ai = Ai(data, output_buffer)
query_handler_thread = Thread(target=query_handler, args=[2, ai])
query_handler_thread.start()
