import multiprocessing as mp
from threading import Thread

from components.ai.main import Ai
from components.database.db_helper import DbHelper

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
