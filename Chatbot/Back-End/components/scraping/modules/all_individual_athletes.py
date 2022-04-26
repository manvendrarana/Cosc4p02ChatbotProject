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

        aName = []
        aContingent = []
        aType = []
        aSport = []
        aAge = []
        aHeight = []
        aWeight = []
        aClubTeam = []
        aCoach = []
        aTeamPosition = []
        aPrevSameGames = []
        aPrevGames = []
        aGoals = []
        aPersonalBest = []
        aAwards = []
        aRoleModel = []
        aMediaInfo = []
        aEvents = []
        aGolds = []
        aSilvers = []
        aBronzes = []
        aPlacings = []

        athleteList = []
        for player in playerGUIDList:
            playerDict = scrape_individual_athlete(player, self.driver)
            lng = 405

            txName = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictName)))
            txName = (txName[:lng] + '..') if len(txName) > lng else txName
            aName.append(txName)

            txContingent = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictContingent)))
            txContingent = (txContingent[:lng] + '..') if len(txContingent) > lng else txContingent
            aContingent.append(txContingent)

            txType = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictType)))
            txType = (txType[:lng] + '..') if len(txType) > lng else txType
            aType.append(txType)

            txSport = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictSport)))
            txSport = (txSport[:lng] + '..') if len(txSport) > lng else txSport
            aSport.append(txSport)

            txAge = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictAge)))
            txAge = (txAge[:lng] + '..') if len(txAge) > lng else txAge
            aAge.append(txAge)

            txHeight = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictHeight)))
            txHeight = (txHeight[:lng] + '..') if len(txHeight) > lng else txHeight
            aHeight.append(txHeight)

            txWeight = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictWeight)))
            txWeight = (txWeight[:lng] + '..') if len(txWeight) > lng else txWeight
            aWeight.append(txWeight)

            txClub = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictClubTeam)))
            txClub = (txClub[:lng] + '..') if len(txClub) > lng else txClub
            aClubTeam.append(txClub)

            txCoach = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictCoach)))
            txCoach = (txCoach[:lng] + '..') if len(txCoach) > lng else txCoach
            aCoach.append(txCoach)

            txPosition = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictTeamPosition)))
            txPosition = (txPosition[:lng] + '..') if len(txPosition) > lng else txPosition
            aTeamPosition.append(txPosition)

            txPrevSameGames = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictPrevSameGames)))
            txPrevSameGames = (txPrevSameGames[:lng] + '..') if len(txPrevSameGames) > lng else txPrevSameGames
            aPrevSameGames.append(txPrevSameGames)

            txPrev = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictPrevGames)))
            txPrev = (txPrev[:lng] + '..') if len(txPrev) > lng else txPrev
            aPrevGames.append(txPrev)

            txGoals = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictGoals)))
            txGoals = (txGoals[:lng] + '..') if len(txGoals) > lng else txGoals
            aGoals.append(txGoals)

            txPersonal = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictPersonalBest)))
            txPersonal = (txPersonal[:lng] + '..') if len(txPersonal) > lng else txPersonal
            aPersonalBest.append(txPersonal)

            txAwards = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictAwards)))
            txAwards = (txAwards[:lng] + '..') if len(txAwards) > lng else txAwards
            aAwards.append(txAwards)

            txRoleModel = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictRoleModel)))
            txRoleModel = (txRoleModel[:lng] + '..') if len(txRoleModel) > lng else txRoleModel
            aRoleModel.append(txRoleModel)

            txMediaInfo = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictMediaInfo)))
            txMediaInfo = (txMediaInfo[:lng] + '..') if len(txMediaInfo) > lng else txMediaInfo
            aMediaInfo.append(txMediaInfo)

            txEvents = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictEvents)))
            txEvents = (txEvents[:lng] + '..') if len(txEvents) > lng else txEvents
            aEvents.append(txEvents)

            txGolds = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictGolds)))
            txGolds = (txGolds[:lng] + '..') if len(txGolds) > lng else txGolds
            aGolds.append(playerDict.get(dictGolds))

            txSilvers = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictSilvers)))
            txSilvers = (txSilvers[:lng] + '..') if len(txSilvers) > lng else txSilvers
            aSilvers.append(txSilvers)

            txBronze = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictBronzes)))
            txBronze = (txBronze[:lng] + '..') if len(txBronze) > lng else txBronze
            aBronzes.append(txBronze)

            txPlacings = re.sub('[^A-Za-z0-9 ]+', '', str(playerDict.get(dictPlacings)))
            txPlacings = (txPlacings[:lng] + '..') if len(txPlacings) > lng else txPlacings
            aPlacings.append(txPlacings)

            url = 'https://cg2019.gems.pro/Result/ShowPerson.aspx?Person_GUID=' + player + '&SetLanguage=en-CA'

            athleteList.append(
                [url, txName, txContingent, txSport, txAge, txHeight, txWeight, txClub, txCoach, txPosition,
                 txPrevSameGames, txPrev, txGoals, txPersonal,
                 txAwards, txRoleModel, txEvents, txGolds, txSilvers, txBronze, txPlacings])

            athleteDict = {
                dictName: aName,
                dictContingent: aContingent,
                dictType: aType,
                dictSport: aSport,
                dictAge: aAge,
                dictHeight: aHeight,
                dictWeight: aWeight,
                dictClubTeam: aClubTeam,
                dictCoach: aCoach,
                dictTeamPosition: aTeamPosition,
                dictPrevSameGames: aPrevSameGames,
                dictPrevGames: aPrevGames,
                dictGoals: aGoals,
                dictPersonalBest: aPersonalBest,
                dictAwards: aAwards,
                dictRoleModel: aRoleModel,
                dictMediaInfo: aMediaInfo,
                dictEvents: aEvents,
                dictGolds: aGolds,
                dictSilvers: aSilvers,
                dictBronzes: aBronzes,
                dictPlacings: aPlacings
            }

        # try:
        #     table_csv = pd.DataFrame(athleteDict,
        #                              columns=[dictName, dictContingent, dictType, dictSport, dictAge, dictHeight,
        #                                       dictWeight,
        #                                       dictClubTeam, dictCoach, dictTeamPosition, dictPrevGames, dictPrevGames,
        #                                       dictGoals, dictPersonalBest, dictAwards, dictRoleModel, dictMediaInfo,
        #                                       dictEvents, dictGolds, dictSilvers, dictBronzes, dictPlacings
        #                                       ])
        #     table_csv.to_csv("players.csv",
        #                      index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        #                      encoding='utf-8-sig')
        #     # print(table_csv)
        #     # print("Done.")
        #     # return table_csv
        # except:
        #     # print("Couldn't print CSV")
        #     pass

        key = "info_athletes"
        documents = {
            key: {
                "url": "https://cg2019.gems.pro/Result/ShowPerson_List.aspx?SetLanguage=en-CA",
                "title": key.replace("_", " ").capitalize(),
                "section_title": "URL, Athlete Name, Athlete Province, Athlete Sport, Athlete Age, "
                                 "Athlete Height, Athlete Weight, Athlete Club, Athlete Coach,"
                                 " Athlete Team Position, Athlete Previous Alias, Athlete Alias, "
                                 "Athlete Goals, Athlete Personal Best, Athlete Awards, Athlete Role Model,"
                                 " Athlete Events, Athlete Gold Medals, Athlete Silver Medals, "
                                 "Athlete Bronze Medals, Athlete Placings",
                "columns": ["URL", "Athlete Name", "Athlete Province", "Athlete Sport", "Athlete Age", "Athlete Height",
                            "Athlete Weight", "Athlete Club", "Athlete Coach", "Athlete Team Position",
                            "Athlete Previous Alias", "Athlete Alias", "Athlete Goals", "Athlete Personal Best",
                            "Athlete Awards", "Athlete Role Model", "Athlete Events", "Athlete Gold Medals",
                            "Athlete Silver Medals", "Athlete Bronze Medals", "Athlete Placings"],
                "values": athleteList
            }}

        return documents
