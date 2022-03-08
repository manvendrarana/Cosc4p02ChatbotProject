from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# this GUID has a page with more txt sections
#GUID = "80befcce-cda0-4b35-9022-364ce2e1d1fe"

# this GUID has less txt sections so some elements won't exist
GUID = 'd2dfde4e-3753-4f06-ad4e-2e3ec4f670ae'

url = 'https://cg2019.gems.pro/Result/ShowTeam.aspx?Team_GUID=' + GUID + '&SetLanguage=en-CA'

DRIVER_PATH = "C:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get(url)

try:
    txtEvent = driver.find_element(By.ID, 'txtEventName')
    print("Team Event: " + txtEvent.text)

    #province
    txtTeamName = driver.find_element(By.ID, 'txtName')
    print("Team Name: " + txtTeamName.text)

    # athlete/coach
    txtContingent = driver.find_element(By.ID, 'txtContingent')
    print("Team Contingent: " + txtContingent.text)

    # athlete/coach
    txtFinalPosition = driver.find_element(By.ID, 'txtFinalPosition')
    print("Team Final Position: " + txtFinalPosition.text)

    tblMatches = driver.find_element(By.CLASS_NAME, "LM_ListTable")
    tblHeaders = tblMatches.find_elements(By.CLASS_NAME, "LM_ListHeaderRow")
    for header in tblHeaders:
        print(header.text)

    teamMatches = []
    tblOdd = driver.find_elements(By.CLASS_NAME, "LM_ListDataRowOdd")
    for row in tblOdd:
        teamMatches.append(row.find_elements(By.CSS_SELECTOR, "td")[0].text)
        #for item in row.find_elements(By.CLASS_NAME, "LM_ListDataCell"):
            #print(item.text)

    tblEven = driver.find_elements(By.CLASS_NAME, "LM_ListDataRowEven")
    for row in tblEven:
            teamMatches.append(row.find_elements(By.CSS_SELECTOR, "td")[0].text)
        #for item in row.find_elements(By.CLASS_NAME, "LM_ListDataCell"):
            #print(item.text)

    tblTeamMembers = driver.find_element(By.CLASS_NAME, "LM_ShowTeamMemberTable")
    rowTeamMembers = tblTeamMembers.find_elements(By.CSS_SELECTOR, ".DataCell.InfoCell")
    teamMembers = []
    for row in rowTeamMembers:
        teamMembers.append(row.find_elements(By.CSS_SELECTOR, "td")[1].text)

    print("Team Matches: ")
    joinedTeamMatches = ", ".join(teamMatches)
    print(joinedTeamMatches)
    joinedTeamMembers = ", ".join(teamMembers)
    print("Team Members: ")
    print(joinedTeamMembers)
except NoSuchElementException:
    print("Element not on this athletes page.")