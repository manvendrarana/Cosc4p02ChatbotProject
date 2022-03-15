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

url = "https://cg2019.gems.pro/Result/ShowPerson.aspx?Person_GUID=76539f53-b67e-481b-903a-0de5308c44dd&SetLanguage=en-CA"
PATH = "C:\Program Files (x86)\chromedriver.exe" 
driver = webdriver.Chrome(PATH)




driver.get(url)



try:
     check = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_tdDataCell")))
     bio = driver.find_elements(By.ID,'ctl00_tdDataCell')
     for e in bio:
         name = driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txtPersonNameFML_divRootControl").text
         contingent = driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txtContingent_divRootControl").text
         hometown = driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txtHomeTown_divRootControl").text
         type = driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txtParticipantTypeName_divRootControl").text
         sport = driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txtSportName_divRootControl").text
         
         
         print(name+"\n")
         print(contingent+"\n")
         print(hometown+"\n")
         print(type+"\n")
         print(sport+"\n")
         
         
         
         
     
     
except:
    
    pass
    



    """
    output
    
    
    Name
Laine Sutherland

Contingent
New Brunswick

Hometown
Fredericton

Type
Athlete

Sport
Alpine Skiing

    
    
    """
