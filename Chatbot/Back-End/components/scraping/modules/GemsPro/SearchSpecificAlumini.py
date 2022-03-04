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



#Change Path to where chromedrive executable is located. 
PATH = "C:\Program Files (x86)\chromedriver.exe" 
driver = webdriver.Chrome(PATH)


driver.get("https://cgc.gems.pro/AlumCgc/Alumni/FindAlumni_List.aspx?SiteMapTreeExpanded=cf477dd3-6fe7-4299-a66d-96a49c86ab9d&SetLanguage=en-CA")








#filter is filled out with relevant data given by the user


# #This section is an example of a search that filters out a specific person with the given data
# FirstName = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtFirstName").send_keys("SIDNEY")
# LastName = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtLastName").send_keys("MCGILL")
# Games = driver.find_element_by_id("ctl00_ContentPlaceHolder1_selSetOfGames").send_keys("2017 Canada Summer Games")
# Contingent = driver.find_element_by_id("ctl00_ContentPlaceHolder1_selContingent").send_keys("Alberta")
# Type = driver.find_element_by_id("ctl00_ContentPlaceHolder1_selParticipantType").send_keys("Athlete")
# Sport = driver.find_element_by_id("ctl00_ContentPlaceHolder1_selSport").send_keys("Cycling")




#This section is an example of a search that filters out a group of people with the data that is common
FirstName = driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$txtFirstName").send_keys("Mark")
LastName = driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$txtLastName").send_keys("H")
Games = driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_selSetOfGames").send_keys("")
Contingent = driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_selContingent").send_keys("")
Type = driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_selParticipantType").send_keys("")
Sport = driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_selSport").send_keys("")








#Find Button is Entered after the filter is filled out to show given results.
Find = driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$btnFind").send_keys(Keys.RETURN)



try:
    AluminiList = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_pnlAlumni")))
    personNames = AluminiList.find_elements(By.CLASS_NAME,"PersonTile")
    for person in personNames:
        FirstN = person.find_element(By.CLASS_NAME,"PersonFirstName")
        LastN = person.find_element(By.CLASS_NAME,"PersonLastName")
        type  = person.find_element(By.CLASS_NAME,"ParticipantType")
        sport = person.find_element(By.CLASS_NAME,"ParticipantSport")
        print("First Name: "+FirstN.text  +", Last Name: " + LastN.text + ", Type: " + type.text + ", Sport: " + sport.text)
        
        
        
        

    
except:
    pass







#print(AluminiList.text)

#driver.quit()


