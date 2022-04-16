import json
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from components.scraping.modules.event import EventScraper


class MyTestCase(unittest.TestCase):

    def test_event_get_labels_and_content(self):
        service = ChromeService(executable_path="../scraping/chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        scraper_obj = EventScraper(driver)
        output = [[element, [obj.get_attribute("innerText") for obj in content_objs]] for element, content_objs in
                  scraper_obj.get_labels_and_content(
                      "https://cg2017.gems.pro/Result/Event_PO_T_T.aspx?Event_GUID=19aa7c44-37b6-4c28-ad29-703203cb8196"
                      "&SetLanguage=en-CA")]
        with open("data/test_scraper_event_getLabelsAndContent.json") as f:
            expected_output = json.load(f)
            self.assertEqual(output, expected_output)
        self.assertEqual(scraper_obj.get_labels_and_content("1"), [])
        driver.close()

    def test_event_get_names_and_urls(self):
        service = ChromeService(executable_path="../scraping/chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        scraper_obj = EventScraper(driver)
        output = scraper_obj.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=1c3ac9b6-46f3-402e-bc15-b0fd0afb6a1d&SetLanguage=en-CA")
        with open("data/test_scraper_event_getNamesAndUrls.json") as f:
            expected_output = [tuple(element) for element in json.load(f)]
            self.assertEqual(output, expected_output)
        self.assertEqual(scraper_obj.get_labels_and_content("1"), [])
        driver.close()

    def test_event_team_sports(self):
        service = ChromeService(executable_path="../scraping/chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        scraper_obj = EventScraper(driver)
        baseball_urls = [("Baseball",
                          "https://cg2017.gems.pro/Result/Event_PO_T_T.aspx?Event_GUID=f28d5b6b-a468-446d-89a6"
                          "-48132ba314d4&SetLanguage=en-CA")]
        output = scraper_obj.team_sport("Baseball", "N/A", urls=baseball_urls,
                                        columns=["team A", "team A runs", "team B", "team B runs"])
        with open("data/test_scraper_event_teamSports.json") as f:
            expected_output = json.load(f)
            self.assertEqual(output, expected_output)
        self.assertEqual(scraper_obj.sports(main_section="", main_url="", urls=[],
                                            columns=[]), {})
        driver.close()

    def test_event_sports(self):
        service = ChromeService(executable_path="../scraping/chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        scraper_obj = EventScraper(driver)
        canoekayak_urls = scraper_obj.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=1c3ac9b6-46f3-402e-bc15-b0fd0afb6a1d"
            "&SetLanguage=en-CA")
        output = scraper_obj.sports(main_section="canoe", main_url="not available", urls=canoekayak_urls,
                                    columns=["score"])
        with open("data/test_scraper_event_sports.json") as f:
            expected_output = json.load(f)
            self.assertEqual(output, expected_output)
        self.assertEqual(scraper_obj.sports(main_section="", main_url="", urls=[],
                                            columns=[]), {})
        driver.close()


if __name__ == '__main__':
    unittest.main()
