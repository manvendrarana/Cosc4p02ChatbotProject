from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from individual_athlete import scrape_individual_athlete

import pandas as pd

#DRIVER_PATH = "C:\webdriver\chromedriver.exe"
#driver = webdriver.Chrome(executable_path=DRIVER_PATH)
def scrape_all_individual_athletes(driver):
    
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
    driver.get(url)
    delay = 15

    try:
        #driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtFirstName").send_keys("as")

        btnFind = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_btnFind').click()

        awaitElement = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'LM_ResultFlagContainer')))
        print("Ready!")

        tblPeople = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_tblParticipant")
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
        print("Element not on this athletes page.")

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

    for player in playerGUIDList:
        playerDict = scrape_individual_athlete(player, driver)

        aName.append(playerDict.get(dictName))
        aContingent.append(playerDict.get(dictContingent))
        aType.append(playerDict.get(dictType))
        aSport.append(playerDict.get(dictSport))
        aAge.append(playerDict.get(dictAge))
        aHeight.append(playerDict.get(dictHeight))
        aWeight.append(playerDict.get(dictWeight))
        aClubTeam.append(playerDict.get(dictClubTeam))
        aCoach.append(playerDict.get(dictCoach))
        aTeamPosition.append(playerDict.get(dictTeamPosition))
        aPrevSameGames.append(playerDict.get(dictPrevSameGames))
        aPrevGames.append(playerDict.get(dictPrevGames))
        aGoals.append(playerDict.get(dictGoals))
        aPersonalBest.append(playerDict.get(dictPersonalBest))
        aAwards.append(playerDict.get(dictAwards))
        aRoleModel.append(playerDict.get(dictRoleModel))
        aMediaInfo.append(playerDict.get(dictMediaInfo))
        aEvents.append(playerDict.get(dictEvents))
        aGolds.append(playerDict.get(dictGolds))
        aSilvers.append(playerDict.get(dictSilvers))
        aBronzes.append(playerDict.get(dictBronzes))
        aPlacings.append(playerDict.get(dictPlacings))

        athleteDict = {
        dictName : aName,
        dictContingent : aContingent,
        dictType : aType,
        dictSport : aSport,
        dictAge : aAge,
        dictHeight : aHeight,
        dictWeight : aWeight,
        dictClubTeam : aClubTeam,
        dictCoach : aCoach,
        dictTeamPosition : aTeamPosition,
        dictPrevSameGames : aPrevSameGames,
        dictPrevGames : aPrevGames,
        dictGoals : aGoals,
        dictPersonalBest : aPersonalBest,
        dictAwards : aAwards,
        dictRoleModel : aRoleModel,
        dictMediaInfo : aMediaInfo,
        dictEvents : aEvents,
        dictGolds : aGolds,
        dictSilvers : aSilvers,
        dictBronzes : aBronzes,
        dictPlacings : aPlacings
    }

    table_csv = pd.DataFrame(athleteDict, columns=[dictName, dictContingent, dictType, dictSport, dictAge, dictHeight, dictWeight,
    dictClubTeam, dictCoach, dictTeamPosition, dictPrevGames, dictPrevGames, dictGoals, dictPersonalBest, dictAwards, dictRoleModel, dictMediaInfo,
    dictEvents, dictGolds, dictSilvers, dictBronzes, dictPlacings
    ])
    table_csv.to_csv("players.csv", index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], encoding = 'utf-8-sig')
    print(table_csv)
    print("Done.")
    return table_csv
