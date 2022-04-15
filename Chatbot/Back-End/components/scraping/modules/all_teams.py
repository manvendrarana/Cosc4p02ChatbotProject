from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from teams import scrape_team

import pandas as pd


url = 'https://cg2019.gems.pro/Result/ShowTeam_List.aspx?SetLanguage=en-CA'

DRIVER_PATH = "C:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get(url)
delay = 3

try:
    #driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtName").send_keys("g")

    btnFind = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_btnFind').click()

    awaitElement = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'LM_ResultFlagContainer')))
    print("Ready!")

    tblTeams = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_tblTeam")
    tblElements = tblTeams.find_elements(By.CLASS_NAME, "DataCell")
    teamGUIDList = []
    for element in tblElements:
        try:
            URL = element.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            GUIDDirty = URL.split("Team_GUID=")
            GUIDClean = GUIDDirty[1].split("&")
            teamGUIDList.append(GUIDClean[0])
        except:
            continue

except NoSuchElementException:
    print("Element not on this athletes page.")

txtEvent = []
txtTeamName = []
txtContingent = []
txtFinalPosition = []
teamMembers = []
teamMatches = []

for team in teamGUIDList:
    teamDict = scrape_team(team, driver)
    txtEvent.append(teamDict.get('Team Event'))
    txtTeamName.append(teamDict.get('Team Name'))
    txtContingent.append(teamDict.get('Team Contingent'))
    txtFinalPosition.append(teamDict.get('Team Final Position'))
    teamMembers.append(teamDict.get('Team Members'))
    teamMatches.append(teamDict.get('Team Competitions'))

newDict = {
    'Team Name' : txtTeamName,
    'Team Members' : teamMembers,
    'Team Competitions' : teamMatches, 
    'Team Event' : txtEvent, 
    "Team Contingent" : txtContingent, 
    "Team Final Position" : txtFinalPosition
}

table_csv = pd.DataFrame(newDict, columns=['Team Name','Team Members', 'Team Competitions', 'Team Event', "Team Contingent", "Team Final Position"])
table_csv.to_csv("teams.csv", index = [0, 1, 2, 3, 4, 5])
print(table_csv)
print("Done.")
