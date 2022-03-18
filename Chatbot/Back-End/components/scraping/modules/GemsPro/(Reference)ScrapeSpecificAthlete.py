import os
from tkinter.tix import Select
from unicodedata import name
import selenium
from selenium.webdriver.support.ui import Select


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Search Criteria is hardcoded. 

#Change Path to where chromedrive executable is located. 
PATH = "C:\Program Files (x86)\chromedriver.exe" 
driver = webdriver.Chrome(PATH)


driver.get("https://cg2019.gems.pro/Result/ShowPerson_List.aspx?SetLanguage=en-CA")








#filter is filled out with relevant data given by the user


# #This section is an example of a search that filters out a specific person with the given data
# FirstName = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtFirstName").send_keys("SIDNEY")
# LastName = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtLastName").send_keys("MCGILL")
# Games = driver.find_element_by_id("ctl00_ContentPlaceHolder1_selSetOfGames").send_keys("2017 Canada Summer Games")
# Contingent = driver.find_element_by_id("ctl00_ContentPlaceHolder1_selContingent").send_keys("Alberta")
# Type = driver.find_element_by_id("ctl00_ContentPlaceHolder1_selParticipantType").send_keys("Athlete")
# Sport = driver.find_element_by_id("ctl00_ContentPlaceHolder1_selSport").send_keys("Cycling")




#This section is an example of a search that filters out a group of people with the data that is common
FirstName = driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$txtFirstName").send_keys("Logan")
LastName = driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$txtLastName").send_keys("Aalders")
Contingent = driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$selContingent").send_keys("New Brunswick")
Sport = driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$selSport").send_keys("Wheelchair Basketball")








#Find Button is Entered after the filter is filled out to show given results.
Find = driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$btnFind").send_keys(Keys.RETURN)



try:
    AthleteList = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_pnlAlumni")))
    personNames = AthleteList.find_elements(By.CLASS_NAME,"PersonTile")
    for person in personNames:
        FirstN = person.find_element(By.CLASS_NAME,"PersonFirstName")
        LastN = person.find_element(By.CLASS_NAME,"PersonLastName")
        
        sport = person.find_element(By.CLASS_NAME,"ParticipantSport")
        print("First Name: "+FirstN.text  +", Last Name: " + LastN.text + ", Sport: " + sport.text)
        
        
        
        

    
except:
    pass







#print(AluminiList.text)

#driver.quit()
