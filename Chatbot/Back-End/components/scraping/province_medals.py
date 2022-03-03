from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

DRIVER_PATH = "C:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get("https://cg2019.gems.pro/Result/MedalList.aspx?SetLanguage=en-CA")

table = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_tblMedals")
tableColumns = table.find_elements(By.CSS_SELECTOR, "tr")


medalDict = {}
for item in tableColumns:
    try:
        individualItem = item.find_elements(By.CLASS_NAME, "LM_ListDataCell")
        contigent = ""
        for newItem in individualItem:
            data = newItem.text
            if not data.isnumeric():
                contigent = data
                if data not in medalDict:
                    medalDict[data] = list()
            if data.isnumeric():
                medalDict[contigent].append(data)
    except:
        pass

print(medalDict)
driver.close();

'''
printing medalDict: 

{' Quebec': ['65', '41', '40', '146'], 
' Ontario': ['18', '43', '44', '105'], 
' Alberta': ['36', '33', '31', '100'], 
' British Columbia': ['30', '28', '29', '87'], 
' Manitoba': ['9', '7', '9', '25'], 
' Saskatchewan': ['3', '3', '11', '17'], 
' Nova Scotia': ['1', '6', '4', '11'], 
' New Brunswick': ['1', '3', '5', '9'], 
' Newfoundland and Labrador': ['1', '0', '1', '2'], 
' Prince Edward Island': ['0', '1', '1', '2'], 
' Northwest Territories': ['0', '0', '1', '1'], 
' Yukon': ['0', '0', '1', '1'], 
' Nunavut': ['0', '0', '0', '0']}
'''