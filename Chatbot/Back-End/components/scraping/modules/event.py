from pprint import pprint
import webbrowser
from numpy import extract
from selenium import webdriver
from selenium.webdriver.common.by import By
import itertools

import pandas as pd


class EventScraper:

    def __init__(self, driver : webdriver.Chrome):
        self.driver = driver
        self.scrape()

    def pprint(values: list):
        print(*values, sep="\n")

    # On each page it returns a full list of all tables with labels
    def get_labels_and_content(self, url:str) -> list:
        self.driver.get(url)
        table_labels_elements = self.driver.find_elements(By.CLASS_NAME, 'LM_CollapsibleSectionName')[:-1]
        tables = []
        for element in table_labels_elements:
            table_content_id = element.get_attribute('id').replace("Label","Content")
            table_content_element = self.driver.find_element(By.ID, table_content_id)
            content_children_elements = table_content_element.find_elements(By.CLASS_NAME,"DataRowOdd") + table_content_element.find_elements(By.CLASS_NAME,"DataRowEven")
            tables.append(([[element.get_attribute("innerText")]], content_children_elements))
        return tables
    
    def get_names_and_urls(self, url:str) -> list:
        self.driver.get(url)
        table = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_tblSport").find_element(By.XPATH, "*").find_elements(By.XPATH, "*")[1:]# get the list of all elements holding events.
        return [(tpl.find_elements(By.XPATH,"*")[0].get_attribute("innerText"), tpl.find_elements(By.XPATH,"*")[0].find_element(By.TAG_NAME,"a").get_attribute("href")) for tpl in table] # name, url

    # scraping baseball page.
    def baseball(self,urls, filename):
        main_event_name, url = urls[0]
        extracted_data = self.get_labels_and_content(url)
        result = []
        for main_event, content_children_elements in extracted_data:
            copy_value = []
            for tpl in content_children_elements:
                values = [value.get_attribute("innerText") for value in tpl.find_elements(By.XPATH, "*")]
                values = [value.split("\n") for value in values]
                if  len(values) == 6 or len(values) == 2:
                    if len(copy_value)  <= 0:
                        values = values[1:-1] # deleting empty spaces
                        copy_value = values
                    else:
                        values = copy_value + values
                        copy_value = []
                        values = main_event + values
                        values = [value.replace("\xa0"," ").strip() for value in list(itertools.chain(*values))]
                        if len(values) < 10 :
                            values = values[:2] + ["Not Available"] + values[2:] # if there is no description for score type
                        values[6] = values[6].replace('-','/').split('/')[-1].strip()
                        values[8] = values[8].replace('-','/').split('/')[-1].strip()
                        result.append([main_event_name] + values)
        table_csv = pd.DataFrame(result, columns=['Main event name','match type', 'match name', 'score type', "date", "time", "location", "team A name", "team A score", "team B name", "team B score"])
        table_csv.to_csv(filename, index=False)
        print (table_csv)
                
    def basketball(self, urls, filename):
        result = []
        for main_event_name, url in urls:
            extracted_data = self.get_labels_and_content(url)
            for match_type, content_children_elements in extracted_data:
                copy_value = []
                for tuple in content_children_elements:
                    values = [value.get_attribute("innerText") for value in tuple.find_elements(By.XPATH, "*")]
                    values = [value.split("\n") for value in values]
                    if  len(values) == 6 or len(values) == 2:
                        if len(copy_value)  <= 0:
                            values = values[1:-1] # deleting empty spaces
                            copy_value = values
                        else:
                            values = copy_value + values
                            copy_value = []
                            values = match_type + values
                            values = [value.replace("\xa0"," ").strip() for value in list(itertools.chain(*values))]
                            if len(values) < 10 :
                                values = values[:2] + ["Not Available"] + values[2:] #
                            values[6] = values[6].replace('-','/').split('/')[-1].strip()
                            values[8] = values[8].replace('-','/').split('/')[-1].strip()
                            result.append([main_event_name] + values)
        #print(*result, sep="\n")
        table_csv = pd.DataFrame(result, columns=['Main event name','match type', 'match name', 'score type', "date", "time", "location", "team A name", "team A score", "team B name", "team B score"])
        table_csv.to_csv(filename, index=False)
        print (table_csv)

    def canoeKayak(self, urls, filename): # cannot use the common method
        result = []
        for main_event_name, url in urls:
            self.driver.get(url)
            table_headers = self.driver.find_elements(By.CLASS_NAME, "LM_CollapsibleSectionName")[:-1] # remove final standings
            table_content = [(heading.get_attribute("innerText"),self.driver.find_element(By.ID,heading.get_attribute("id").replace("Label","Content"))) for heading in table_headers]
            for match_type, content in table_content:
                rows = content.find_elements(By.XPATH, "*")[:-1]
                event_details = []
                for row in rows:
                    if len(event_details) <= 0:
                        event_details = row.find_elements(By.CLASS_NAME, "LM_ResultGameName")
                    else:
                        score_rows = row.find_elements(By.CLASS_NAME, "LM_ListDataRowOdd") + row.find_elements(By.CLASS_NAME, "LM_ListDataRowEven")
                        scores = [r.find_elements(By.XPATH, "*") for r in score_rows]
                        for score_row in scores: 
                            values = [main_event_name] + [entry.get_attribute("innerText") for entry in event_details + score_row]
                            values[5] = values[5].replace("\xa0","")
                            result.append(values)
                        event_details = []
        table_csv = pd.DataFrame(result, columns=['Main event name', 'match name', "date", "time", "location", "team name", "team score"])
        table_csv.to_csv(filename, index=False)
        print (table_csv)
        

    def scrape(self):
        baseball_urls = [("baseball", "https://cg2017.gems.pro/Result/Event_PO_T_T.aspx?Event_GUID=f28d5b6b-a468-446d-89a6-48132ba314d4&SetLanguage=en-CA")]
        basketball_urls = [("basketball female","https://cg2017.gems.pro/Result/Event_PO_T_T.aspx?Event_GUID=ac4b7742-afd1-4dae-a162-f8481f05323d&SetLanguage=en-CA"),("basketball male","https://cg2017.gems.pro/Result/Event_PO_T_T.aspx?Event_GUID=19aa7c44-37b6-4c28-ad29-703203cb8196&SetLanguage=en-CA")]
        canoekayak_urls = self.get_names_and_urls("https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=1c3ac9b6-46f3-402e-bc15-b0fd0afb6a1d&SetLanguage=en-CA")

        self.baseball(urls=baseball_urls, filename = "baseball.csv")
        self.basketball(urls=basketball_urls, filename = "basketball.cs")
        self.canoeKayak(urls=canoekayak_urls, filename = "canoe.csv")
