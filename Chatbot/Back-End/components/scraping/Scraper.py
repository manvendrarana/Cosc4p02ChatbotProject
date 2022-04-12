import json
import os
import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from scraping.modules.event import EventScraper  # add components to run in python only mode


class Scraper:
    def __init__(self, output_buffer):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.output_buffer = output_buffer

    def scrape(self):
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
