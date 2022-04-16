from pprint import pprint
from re import sub
import webbrowser
from numpy import extract
from pyparsing import col
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import itertools
import re
import pandas as pd


class EventScraper:
    """ This class scrapes all event data from the gems pro website"""

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    @staticmethod
    def pprint(values: list):
        """ Pretty Prints a List
        
        Keyword Arguments:
        values      -- list of values to be printed
        """
        print(*values, sep="\n")

    @staticmethod
    def clean_key(key):
        key = re.sub("_+", "_", key)
        key = re.sub(" +", "_", key)
        return key

    def get_labels_and_content(self, url: str) -> list:
        """  Receives a URL, scrapes the URL for all tables and labels
        
        Keyword Arguments: 
        url     -- string URL
        Returns:
        list    -- array of tables/labels scraped from the URL 
        """
        try:
            self.driver.get(url)
            table_labels_elements = self.driver.find_elements(By.CLASS_NAME, 'LM_CollapsibleSectionName')[:-1]
            tables = []
            for element in table_labels_elements:
                table_content_id = element.get_attribute('id').replace("Label", "Content")
                table_content_element = self.driver.find_element(By.ID, table_content_id)
                content_children_elements = table_content_element.find_elements(By.CLASS_NAME,
                                                                                "DataRowOdd") + table_content_element.find_elements(
                    By.CLASS_NAME, "DataRowEven")
                tables.append(([[element.get_attribute("innerText")]], content_children_elements))
            return tables
        except:
            return []

    def get_names_and_urls(self, url: str, prefix="") -> list:
        """ Receives a URL, scrapes the URL for all event names and associated hyperlinks 

        Keyword Arguments:
        url     -- string URL
        Returns:
        list    -- array of event names, and it's associated URL. 
        """
        try:
            self.driver.get(url)
            table = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_tblSport").find_element(By.XPATH,
                                                                                                       "*").find_elements(
                By.XPATH, "*")[1:]  # get the list of all elements holding events.
            return [((prefix + " " + tpl.find_elements(By.XPATH, "*")[0].get_attribute("innerText")).strip(),
                     tpl.find_elements(By.XPATH, "*")[0].find_element(By.TAG_NAME, "a").get_attribute("href")) for tpl
                    in
                    table]  # name, url
        except:
            return []

    def sports(self, main_section, main_url, urls, columns):
        """ Scrapes the Sports type events that don't conform to the 'Team' type, and puts all data inside a DataFrame, and exports to a CSV file

        Keyword Arguments:
        urls      -- list of URLs to scrape
        filename  -- name of CSV to create
        columns   -- extra columns associated with the particular sport (score is 'Runs' in Baseball but 'Points' in Basketball for example.)
        """
        documents = {}
        main_events = []
        try:
            for main_event_name, url in urls:
                main_events.append([main_event_name])
                self.driver.get(url)
                result = []
                table_headers = self.driver.find_elements(By.CLASS_NAME, "LM_CollapsibleSectionName")[
                                :-1]  # remove final standings
                table_content = [
                    self.driver.find_element(By.ID, heading.get_attribute("id").replace("Label", "Content"))
                    for heading in table_headers]
                for content in table_content:
                    rows = content.find_elements(By.XPATH, "*")[:-1]
                    event_details = []
                    for row in rows:
                        if len(event_details) <= 0:
                            event_details = row.find_elements(By.CLASS_NAME, "LM_ResultGameName")
                        else:
                            score_rows = row.find_elements(By.CLASS_NAME, "LM_ListDataRowOdd") + row.find_elements(
                                By.CLASS_NAME, "LM_ListDataRowEven")
                            scores = [r.find_elements(By.XPATH, "*") for r in score_rows]
                            for score_row in scores:
                                sub_values = [entry.get_attribute("innerText") for entry in event_details + score_row]
                                if sub_values[5] == '':
                                    sub_values.remove('')
                                # else:
                                #     print("false")
                                if sub_values[0] == '\n':
                                    sub_values.remove('\n')
                                if len(sub_values) == 6:
                                    sub_values.insert(4, "N/A")
                                values = sub_values
                                values[0] += " " + self.clean_key(
                                    main_event_name.replace("-", "_").replace(" ", "_") + "_" +
                                    main_section.replace(" ", "_")).replace("_", " ")
                                # values[1] = values[1].replace("\xa0", "")
                                values[5] = values[5].replace("\xa0", "")
                                result.append(values)
                            event_details = []
                key = self.clean_key(
                    main_section.replace(" ", "_") + "_" + main_event_name.replace("-", "_").replace(" ", "_"))

                documents[key] = {
                    "url": url,
                    "title": key.replace("_", " ").capitalize(),
                    "section_title": "Information of events ,location, time, date, participants, " + " ,".join(
                        columns) + " for " + main_event_name.replace("-", " ") + main_section.replace("_", " "),
                    "columns": ['event name', "date", "time", "location", "number", "name"] + columns,
                    "values": result
                }
            if len(documents) > 0:
                documents["list_events_" + main_section.replace(" ", "_")] = {
                    "url": main_url,
                    "title": main_section.replace(" ", "_"),
                    "section_title": "Information of all the events in " + main_section,
                    "columns": ["Events"],
                    "values": main_events
                }
            return documents
        except:
            return {}

    def team_sport(self, main_section, main_url, urls, columns):
        """ Scrapes the Team Sports type events and puts all data inside a DataFrame, and exports to a CSV file
        
        Keyword Arguments:
        urls      -- list of URLs to scrape
        filename  -- name of CSV to create
        columns   -- extra columns associated with the particular team sport (score is 'Runs' in Baseball but 'Points' in Basketball for example.)
        """
        try:
            documents = {}
            for main_event_name, url in urls:
                extracted_data = self.get_labels_and_content(url)
                result = []
                for match_type, content_children_elements in extracted_data:
                    copy_value = []
                    for child in content_children_elements:
                        values = [value.get_attribute("innerText") for value in child.find_elements(By.XPATH, "*")]
                        values = [value.split("\n") for value in values]
                        if len(values) == 6 or len(values) == 2:
                            if len(copy_value) <= 0:
                                values = values[1:-1]  # deleting empty spaces
                                copy_value = values
                            else:
                                values = copy_value + values
                                copy_value = []
                                values = match_type + values
                                values = [value.replace("\xa0", " ").strip() for value in
                                          list(itertools.chain(*values))]
                                if len(values) < 10:
                                    values = values[:2] + ["Not Available"] + values[2:]
                                values[6] = values[6].replace('-', '/').split('/')[-1].strip()
                                values[8] = values[8].replace('-', '/').split('/')[-1].strip()
                                values = [" ".join(values[0:3])] + values[4:]

                                result.append(values)

                    documents[(main_event_name + "_" + match_type[0][0].replace("\xa0", " ")).replace(" ", "_")] = {
                        "url": url,
                        "title": main_event_name + " " + match_type[0][0].replace("\xa0", " "),
                        "section_title": "Information of events , time, location ," + " ,".join(
                            columns) + " for " + main_event_name + " " + match_type[0][0].replace("\xa0", " "),
                        "columns": ['event', "time", "location"] + columns,
                        "values": result,
                    }
                    result = []
            return documents
        except:
            return {}

    # ----------------------- NEEDS FIXING BEGIN -----------------------
    def golf(self, urls, filename, type):
        """ Scrapes the Golf events and puts all data inside a DataFrame, and exports to a CSV file
        
        Keyword Arguments:
        urls      -- list of URLs to scrape
        filename  -- name of CSV to create
        type      -- team or individual (0 or 1 respectively)
        """
        try:
            documents = {}
            if type == 0:
                name = 'name'
            else:
                name = 'team'
            for main_event_name, url in urls:
                self.driver.get(url)
                result = []
                table_headers = self.driver.find_elements(By.CLASS_NAME, "LM_CollapsibleSectionName")[
                                :-1]  # remove final standings
                table_content = [(heading.get_attribute("innerText"),
                                  self.driver.find_element(By.ID,
                                                           heading.get_attribute("id").replace("Label", "Content")))
                                 for heading in table_headers]
                for match_type, content in table_content:
                    rows = content.find_elements(By.XPATH, "*")[:-1]
                    event_details = []
                    for row in rows:
                        if len(event_details) <= 0:
                            event_details = row.find_elements(By.CLASS_NAME, "LM_ResultGameName")
                        else:
                            score_rows = row.find_elements(By.CLASS_NAME, "LM_ListDataRowOdd") + row.find_elements(
                                By.CLASS_NAME, "LM_ListDataRowEven")
                            scores = [r.find_elements(By.XPATH, "*") for r in score_rows]
                            for score_row in scores:
                                sub_values = [entry.get_attribute("innerText") for entry in event_details + score_row]
                                sub_values = sub_values[21:28]
                                values = [main_event_name] + sub_values
                                result.append(values)
                            event_details = []
                documents[(main_event_name + "_" + match_type[0][0].replace("\xa0", " ")).replace(" ", "_")] = {
                    "url": url,
                    "title": main_event_name + " " + match_type[0][0].replace("\xa0", " "),
                    "section_title": "Information of event name ," + name + "round 1, round 2, round 3, final round, total"
                                     + " for " + main_event_name + " " + match_type[0][0].replace("\xa0", " "),
                    "df": pd.DataFrame(result,
                                       columns=['Main event name', name, 'round 1', 'round 2', 'round 3', 'final round',
                                                'total'])
                }
            return documents
        except:
            return {}

    def thlons(self, urls, filename, columns, type):
        """ Scrapes the Decathlon/Hepthlon events and puts all data inside a DataFrame, and exports to a CSV file
        
        Keyword Arguments:
        urls      -- list of URLs to scrape
        filename  -- name of CSV to create
        type      -- team or individual (0 or 1 respectively)
        """
        try:
            result = []
            for main_event_name, url in urls:
                self.driver.get(url)
                table_headers = self.driver.find_elements(By.CLASS_NAME, "LM_CollapsibleSectionName")[
                                :-1]  # remove final standings
                table_content = [(heading.get_attribute("innerText"),
                                  self.driver.find_element(By.ID,
                                                           heading.get_attribute("id").replace("Label", "Content")))
                                 for heading in table_headers]
                for match_type, content in table_content:
                    rows = content.find_elements(By.XPATH, "*")[:-1]
                    event_details = []
                    for row in rows:
                        if len(event_details) <= 0:
                            event_details = row.find_elements(By.CLASS_NAME, "LM_ResultGameName")
                        else:
                            score_rows = row.find_elements(By.CLASS_NAME, "LM_ListDataRowOdd") + row.find_elements(
                                By.CLASS_NAME, "LM_ListDataRowEven")
                            scores = [r.find_elements(By.XPATH, "*") for r in score_rows]
                            for score_row in scores:
                                sub_values = [entry.get_attribute("innerText") for entry in event_details + score_row]
                                if type == 0:
                                    sub_values = sub_values[51:64]
                                else:
                                    sub_values = sub_values[36:46]
                                values = [main_event_name] + sub_values
                                result.append(values)
                            event_details = []
            table_csv = pd.DataFrame(result, columns=['Main event name', 'number', 'name'] + columns)
            table_csv.to_csv(filename, index=False)
            print(table_csv)
        except:
            return {}

    def tennis(self, urls, filename, columns):
        """ Scrapes the Tennis events and puts all data inside a DataFrame, and exports to a CSV file

        Keyword Arguments:
        urls      -- list of URLs to scrape
        filename  -- name of CSV to create
        columns   -- extra columns associated with the particular team sport (score is 'Runs' in Baseball but 'Points' in Basketball for example.)
        """
        result = []
        for main_event_name, url in urls:
            extracted_data = self.get_labels_and_content(url)
            for match_type, content_children_elements in extracted_data:
                copy_value = []
                for tuple in content_children_elements:
                    values = [value.get_attribute("innerText") for value in tuple.find_elements(By.XPATH, "*")]
                    values = [value.split("\n") for value in values]
                    if len(values) == 6 or len(values) == 2:
                        if len(copy_value) <= 0:
                            values = values[1:-1]  # deleting empty spaces
                            copy_value = values
                        else:
                            values = copy_value + values
                            copy_value = []
                            values = match_type + values
                            values = [value.replace("\xa0", " ").strip() for value in list(itertools.chain(*values))]
                            if len(values) < 10:
                                values = values[:2] + ["Not Available"] + values[2:]  #
                            values[6] = values[6].replace('-', '/').split('/')[-1].strip()
                            values[8] = values[8].replace('-', '/').split('/')[-1].strip()
                            result.append([main_event_name] + values)
        table_csv = pd.DataFrame(result,
                                 columns=['Main event name', 'match type', 'match name', 'score type', "date", "time",
                                          "location"] + columns)
        table_csv.to_csv(filename, index=False)
        print(table_csv)

    # ----------------------- NEEDS FIXING END -----------------------

    def scrape(self):
        """ Gets the names and urls of all events, then scrapes those URLs """
        documents = {}

        baseball_urls = [("Baseball",
                          "https://cg2017.gems.pro/Result/Event_PO_T_T.aspx?Event_GUID=f28d5b6b-a468-446d-89a6"
                          "-48132ba314d4&SetLanguage=en-CA")]
        basketball_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=faede08e-b7b4-4262-bb3d-e5842172ffc5"
            "&SetLanguage=en-CA", prefix="Basketball")
        canoekayak_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=1c3ac9b6-46f3-402e-bc15-b0fd0afb6a1d"
            "&SetLanguage=en-CA")
        diving_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=bbd7a72c-8314-44e8-a6d7-80d304b2519a"
            "&SetLanguage=en-CA")
        golf_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=417680be-8746-4529-a171-194430dc7371"
            "&SetLanguage=en-CA")
        rowing_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=0f976863-1313-4c39-baa2-f9ae01b826f9"
            "&SetLanguage=en-CA")
        sailing_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=e0834e86-8a40-4379-b732-e1f17c03ccb1"
            "&SetLanguage=en-CA")
        soccer_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=a9254026-0b44-4a0c-b109-20bcba05ad3e"
            "&SetLanguage=en-CA", prefix="Soccer")
        softball_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=36c94721-ce80-4323-9d3d-5c46dccb5568"
            "&SetLanguage=en-CA", prefix="Softball")
        swimming_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=346c9aa2-699d-462d-862f-438981700d06"
            "&SetLanguage=en-CA")
        tennis_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=f06e0d96-1a2a-43e3-9205-ca04d6b50edb"
            "&SetLanguage=en-CA")
        triathlon_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=19a0f7d7-5379-47dd-98aa-35ba06c8dbda"
            "&SetLanguage=en-CA")
        volleyball_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=c6a97e4a-b30f-4214-8052-3b0d37483722"
            "&SetLanguage=en-CA")
        wrestling_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=6c3b66cb-ea77-4873-93e0-ed84f83b3a36"
            "&SetLanguage=en-CA", prefix="Wrestling")
        cycling_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=876a594a-2117-494f-9963-385321232a89"
            "&SetLanguage=en-CA")
        cycling_timed_urls = cycling_urls[0:2] + cycling_urls[4:8] + cycling_urls[10:12]
        cycling_points_urls = cycling_urls[2:4]
        cycling_pos_urls = cycling_urls[8:10]
        athletics_urls = self.get_names_and_urls(
            "https://cg2017.gems.pro/Result/Event_List.aspx?Sport_GUID=f3f4d35b-d99e-4538-a874-eab972650185"
            "&SetLanguage=en-CA")
        race_urls = athletics_urls[0: 16]
        hurdles_urls = athletics_urls[16:20]
        steeplechase_urls = athletics_urls[20:22]
        race_urls = race_urls + athletics_urls[22:28]
        relay_urls = athletics_urls[28:32]
        high_jump_urls = athletics_urls[32:34]
        long_jump_urls = athletics_urls[34:36]
        triple_jump_urls = athletics_urls[36:38]
        pole_vault_urls = athletics_urls[38:40]
        shot_put_urls = athletics_urls[40:44]
        discus_urls = athletics_urls[44:48]
        javelin_urls = athletics_urls[48:50]
        hammer_urls = athletics_urls[50:52]
        decathlon_urls = athletics_urls[52:53]
        heptathlon_urls = athletics_urls[53:54]

        documents |= self.sports(main_section="canoe", main_url="not available", urls=canoekayak_urls,
                                 columns=["score"])
        return documents
        documents |= self.sports(main_section="cycling timed", main_url="not available", urls=cycling_timed_urls,
                                 columns=["time"])
        documents |= self.sports(main_section="cycling points", main_url="not available", urls=cycling_timed_urls,
                                 columns=["time"])
        documents |= self.sports(main_section="cycling position", main_url="not available", urls=cycling_pos_urls,
                                 columns=["position"])
        documents |= self.sports(main_section="diving", main_url="not available", urls=diving_urls, columns=["points"])
        documents |= self.sports(main_section="rowing", main_url="not available", urls=rowing_urls, columns=["time"])
        documents |= self.sports(main_section="sailing", main_url="not available", urls=sailing_urls,
                                 columns=["position"])
        documents |= self.sports(main_section="swimming", main_url="not available", urls=swimming_urls,
                                 columns=["time"])
        documents |= self.sports(main_section="triathlon", main_url="not available", urls=triathlon_urls,
                                 columns=["time"])
        documents |= self.sports(main_section="race", main_url="not available", urls=race_urls, columns=["time"])
        documents |= self.sports(main_section="hurdles", main_url="not available", urls=hurdles_urls, columns=["time"])
        documents |= self.sports(main_section="steeplechase", main_url="not available", urls=steeplechase_urls,
                                 columns=["time"])
        documents |= self.sports(main_section="relay", main_url="not available", urls=relay_urls, columns=["time"])

        # # JUMPS DO NOT WORK WITH 2017/2019 SITE DATA, WILL WORK WITH 2022 VERSION
        # # self.sports(urls=high_jump_urls, filename="high_jump.csv", columns=["group A", "group B", "length"])
        # # self.sports(urls=long_jump_urls,filename="long_jump.csv",columns=["group A", "group B", "length"])
        # # self.sports(urls=triple_jump_urls,filename="triple_jump.csv",columns=["group A", "group B", "length"])
        # self.sports(main_section="pole_vault", urls=pole_vault_urls, main_url="not available", columns=["height"])
        # self.sports(main_section="short_put", urls=shot_put_urls, main_url="not available", columns=["length"])
        # self.sports(main_section="discus", urls=discus_urls, main_url="not available", columns=["length"])
        # self.sports(main_section="javelin", urls=javelin_urls, main_url="not available", columns=["length"])
        # self.sports(main_section="hammer", urls=hammer_urls, main_url="not available", columns=["length"])

        documents |= self.team_sport(urls=baseball_urls, columns=["team A", "team A runs", "team B", "team B runs"])
        documents |= self.team_sport(urls=basketball_urls,
                                     columns=["team A", "team A points", "team B", "team B points"])
        documents |= self.team_sport(urls=soccer_urls, columns=["team A", "team A score", "team B", "team B score"])
        documents |= self.team_sport(urls=softball_urls, columns=["team A", "team A runs", "team B", "team B runs"])
        documents |= self.team_sport(urls=wrestling_urls[0:2], columns=["team A", "team A points", "team B",
                                                                        "team B points"])
        documents |= self.team_sport(urls=wrestling_urls[2:], columns=["participant A", "participant A points",
                                                                       "participant B", "participant B points"])

        # TENNIS CURRENTLY NOT WORKING self.tennis(urls=tennis_urls[0:2], filename="tennis_individuals.csv",
        # columns=["participant A", "match A", "sets 1 A", "sets 2 A", "sets 3 A" , "participant B", "match B",
        # "sets 1 B",  "sets 2 B",  "sets 3 B"]) self.tennis(urls=tennis_urls[2:], filename="tennis_teams.csv",
        # columns= ["team A", "match A", "sets 1 A", "sets 2 A", "sets 3 A" , "team B",  "match B",  "sets 1 B",
        # "sets 2 B",  "sets 3 B"])

        # Pending Scraping...
        # self.golf(urls=golf_urls[0:2], filename="golf_individual.csv", type=0)
        # self.golf(urls=golf_urls[2:], filename="golf_teams.csv", type=1)
        #
        # self.thlons(urls=decathlon_urls, filename="decathlon.csv",
        #             columns=["100m", "Long Jump", "Shot Put", "High Jump", "400m", "110m Hurdles", "Discus",
        #                      "Pole Vault", "Javelin", "1500m", "Points"], type=0)
        # self.thlons(urls=heptathlon_urls, filename="heptathlon.csv",
        #             columns=["100m Hurdles", "High Jump", "Shot Put", "200m", "Long Jump", "Javelin", "800m", "Points"],
        #             type=1)
        # Pending Scraping...
        return documents
