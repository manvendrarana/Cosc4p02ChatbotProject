from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://cg2019.gems.pro/Result/ShowPerson_List.aspx?SetLanguage=en-CA'

driver = webdriver.Chrome('C:\Downloads\chromedriver_win32\chromedriver.exe')

driver.get(url)

driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_btnFind"]').click()

names = []
sport = []

player_names = driver.find_elements(By.XPATH, '//table[@id="ctl00_ContentPlaceHolder1_tblParticipant"]/tbody/tr/td/a')
player_sport = driver.find_elements(By.XPATH, '//table[@id="ctl00_ContentPlaceHolder1_tblParticipant"]/tbody/tr/td[2]/div[2]')

for player in player_names:
    names.append(player.text)

for player in player_sport:
    sport.append(player.text)

for i in range(len(names)):
    print(names[i] + '\t ' + sport[i])













