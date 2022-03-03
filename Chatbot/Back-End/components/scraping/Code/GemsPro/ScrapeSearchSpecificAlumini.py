import os
from tkinter.tix import Select
from unicodedata import name
import selenium
from selenium.webdriver.support.ui import Select


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#Change Path to where chromedrive executable is located. 
PATH = "C:\Program Files (x86)\chromedriver.exe" 
driver = webdriver.Chrome(PATH)


driver.get("https://cgc.gems.pro/AlumCgc/Alumni/FindAlumni_List.aspx?SiteMapTreeExpanded=cf477dd3-6fe7-4299-a66d-96a49c86ab9d&SetLanguage=en-CA")








#filter is filled out with relevant data given by the user
FirstName = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtFirstName").send_keys("SIDNEY")
LastName = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtLastName").send_keys("MCGILL")
Games = driver.find_element_by_id("ctl00_ContentPlaceHolder1_selSetOfGames").send_keys("2017 Canada Summer Games")
Contingent = driver.find_element_by_id("ctl00_ContentPlaceHolder1_selContingent").send_keys("Alberta")
Type = driver.find_element_by_id("ctl00_ContentPlaceHolder1_selParticipantType").send_keys("Athlete")
Sport = driver.find_element_by_id("ctl00_ContentPlaceHolder1_selSport").send_keys("Cycling")





#Find Button is clicked after the filter is filled out to show given results.
Find = driver.find_element_by_name("ctl00$ContentPlaceHolder1$btnFind").send_keys(Keys.RETURN)

time.sleep(10)


#driver.quit()


