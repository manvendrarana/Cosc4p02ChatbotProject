from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from teams import scrape_team

url = 'https://cg2019.gems.pro/Result/ShowTeam_List.aspx?SetLanguage=en-CA'

DRIVER_PATH = "C:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get(url)
delay = 3

try:
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

for team in teamGUIDList:
    scrape_team(team, driver)