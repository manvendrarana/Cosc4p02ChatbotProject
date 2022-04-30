import re

from scraping.modules.individual_athlete import scrape_individual_athlete
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AthleteScrape:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    # DRIVER_PATH = "C:\webdriver\chromedriver.exe"
    # driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    def scrape(self):
        dictName = "Athlete Name"
        dictContingent = "Athlete Province"
        dictType = "Athlete or Coach"
        dictSport = "Athlete Sport"
        dictAge = "Athlete Age"
        dictHeight = "Athlete Height"
        dictWeight = "Athlete Weight"
        dictClubTeam = "Athletes Clubs or Teams"
        dictCoach = "Athletes Coaches Name"
        dictTeamPosition = "Athletes Team Position"
        dictPrevSameGames = "Athletes Same Previous Games"
        dictPrevGames = "Athletes Previous Games"
        dictGoals = "Athletes Goals"
        dictPersonalBest = "Athletes Personal Best"
        dictAwards = "Athletes Awards"
        dictRoleModel = "Athletes Role Model"
        dictMediaInfo = "Athletes Media or Social Media Information"
        dictEvents = "Events Participated In"
        dictGolds = "Athletes Number of Gold Medals"
        dictSilvers = "Athletes Number of Silver Medals"
        dictBronzes = "Athletes Number of Bronze Medals"
        dictPlacings = "Athletes Placements"

        url = 'https://cg2019.gems.pro/Result/ShowPerson_List.aspx?SetLanguage=en-CA'
        self.driver.get(url)
        delay = 15

        try:
            self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtFirstName").send_keys("av")
            # use only a for 250 athletes,
            # comment the line to scrape all athletes(Warning your system might run out memory)

            btnFind = self.driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_btnFind').click()

            awaitElement = WebDriverWait(self.driver, delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'LM_ResultFlagContainer')))
            # print("Ready!")

            tblPeople = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_tblParticipant")
            tblElements = tblPeople.find_elements(By.CLASS_NAME, "DataCell")
            playerGUIDList = []
            for element in tblElements:
                try:
                    URL = element.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                    GUIDDirty = URL.split("Person_GUID=")
                    GUIDClean = GUIDDirty[1].split("&")
                    playerGUIDList.append(GUIDClean[0])
                except:
                    continue

        except NoSuchElementException:
            pass
            # print("Element not on this athletes page.")

        def filter(value, max_char):
            value = re.sub('[^A-Za-z0-9 ]+', '', value)
            value = value.strip()
            if len(value) > 0:
                return (value[:max_char] + '..') if len(value) > max_char else value
            else:
                return "Not Available"

        athleteList = []
        for player in playerGUIDList:
            playerDict = scrape_individual_athlete(player, self.driver)
            lng = 405

            txName = filter(str(playerDict.get(dictName)), lng)
            txContingent = filter(str(playerDict.get(dictContingent)), lng)
            txType = filter(str(playerDict.get(dictType)), lng)
            txSport = filter(str(playerDict.get(dictSport)), lng)
            txAge = filter(str(playerDict.get(dictAge)), lng)
            txHeight = filter(str(playerDict.get(dictHeight)), lng)
            txWeight = filter(str(playerDict.get(dictWeight)), lng)
            txClub = filter(str(playerDict.get(dictClubTeam)), lng)
            txCoach = filter(str(playerDict.get(dictCoach)), lng)
            txPosition = filter(str(playerDict.get(dictTeamPosition)), lng)
            txPrevSameGames = filter(str(playerDict.get(dictPrevSameGames)), lng)
            txPrev = filter(str(playerDict.get(dictPrevGames)), lng)
            txGoals = filter(str(playerDict.get(dictGoals)), lng)
            txPersonal = filter(str(playerDict.get(dictPersonalBest)), lng)
            txAwards = filter(str(playerDict.get(dictAwards)), lng)
            txRoleModel = filter(str(playerDict.get(dictRoleModel)), lng)
            txMediaInfo = filter(str(playerDict.get(dictMediaInfo)), lng)
            txEvents = filter(str(playerDict.get(dictEvents)), lng)
            txGolds = filter(str(playerDict.get(dictGolds)), lng)
            txSilvers = filter(str(playerDict.get(dictSilvers)), lng)
            txBronze = filter(str(playerDict.get(dictBronzes)), lng)
            txPlacings = filter(str(playerDict.get(dictPlacings)), lng)

            url = 'https://cg2019.gems.pro/Result/ShowPerson.aspx?Person_GUID=' + player + '&SetLanguage=en-CA'
            athleteList.append(
                [url,
                 txName,
                 txName + "''s contingent is " + txContingent,
                 txName + " participates in " + txSport,
                 txName + "''s age is " + txAge,
                 txName + "''s height is " + txHeight,
                 txName + "''s weight is " + txWeight,
                 txName + " belongs to " + txClub,
                 txName + "''s coach is " + txCoach,
                 txName + "''s position is " + txPosition,
                 txName + "''s previous aliases was " + txPrevSameGames,
                 txName + "''s alias is " + txPrev,
                 txName + "''s goals are " + txGoals,
                 txName + "''s personal best is " + txPersonal,
                 "Awards earned by " + txName + " are " + txAwards,
                 txName + "''s role model is " + txRoleModel,
                 txName + " participates in " + txEvents + " events ",
                 txName + " earned " + txGolds + " Gold medals",
                 txName + " earned " + txSilvers + " Silver medals",
                 txName + " earned " + txBronze + " Bronze medals",
                 txName + " had " + txPlacings + " placings."]
            )

        key = "Athletes_Info"
        documents = {
            key: {
                "url": "https://cg2019.gems.pro/Result/ShowPerson_List.aspx?SetLanguage=en-CA",
                "title": key.replace("_", " ").capitalize(),
                "section_title": "Information on Athlete URL, Name, Province, Sport, Age, Height, Weight, Club, "
                                 "Coach, Team Position, Previous Alias, Alias, Goals, Personal Best, Awards, "
                                 "Role Model, Events, Gold Medals, Silver Medals, Bronze Medals, Placings",
                "columns": ["URL", "Name", "Province", "Sport", "Age", "Height",
                            "Weight", "Club", "Coach", "Team Position",
                            "Previous Alias", "Alias", "Goals", "Personal Best",
                            "Awards", "Role Model", "Events", "Gold Medals",
                            "Silver Medals", "Bronze Medals", "Placings"],
                "values": athleteList
            }}

        return documents
