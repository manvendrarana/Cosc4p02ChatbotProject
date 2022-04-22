import json

from scraping.modules.event import EventScraper  # add components to run in python only mode
from scraping.modules.all_teams import TeamScraper
from scraping.modules.province_medals import ProvinceMedalScraper
from scraping.modules.sport_dates import SportsDateScraper
from scraping.modules.all_individual_athletes import AthleteScrape
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


class Scraper:
    def __init__(self, output_buffer):
        self.driver = None
        self.service = ChromeService(executable_path="./scraping/chromedriver.exe")
        self.output_buffer = output_buffer

    def scrape(self):
        self.driver = webdriver.Chrome(service=self.service)
        documents = {}
        self.output_buffer.put(json.dumps({"type": "update",
                                           "component": "scraper",
                                           "update": "busy",
                                           "update_message": "Starting Scraping"
                                           }))
        # --- All Scraping calls ----
        documents |= EventScraper(self.driver).scrape()
        self.output_buffer.put(json.dumps({"type": "update",
                                           "component": "scraper",
                                           "update": "busy",
                                           "update_message": "Events Scraped"
                                           }))
        self.driver.close()
        self.output_buffer.put(json.dumps({"type": "update",
                                           "component": "scraper",
                                           "update": "working",
                                           "update_message": "Everything is scraped"
                                           }))
        return documents
