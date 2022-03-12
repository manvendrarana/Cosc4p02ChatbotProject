from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import pandas as pd

#DRIVER_PATH = "C:\webdriver\chromedriver.exe"
#driver = webdriver.Chrome(executable_path=DRIVER_PATH)

def scrape_province_medals(driver):

    driver.get("https://cg2019.gems.pro/Result/MedalList.aspx?SetLanguage=en-CA")

    try: 
        table = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_tblMedals")
        tableColumns = table.find_elements(By.CSS_SELECTOR, "tr")

        medalDict = {}
        for item in tableColumns:
            try:
                individualItem = item.find_elements(By.CLASS_NAME, "LM_ListDataCell")
                contigent = ""
                for newItem in individualItem:
                    data = newItem.text.lstrip()
                    if not data.isnumeric():
                        contigent = data
                        if data not in medalDict:
                            medalDict[data] = list()
                    if data.isnumeric():
                        medalDict[contigent].append(data)
            except:
                print("Datacell unavailable.")

        provinceName = []
        provinceGold = []
        provinceSilver = []
        provinceBronze = []
        provinceTotal = []

        for province, values in medalDict.items():
            print("Province Name: " + province)
            print("Gold Medals: " + values[0])
            print("Silver Medals: " + values[1])
            print("Bronze Medals: " + values[2])
            print("Total Medals: " + values[3])
            print("\n")

            #medalTuple = (province, values[0], values[1], values[2], values[3])
            provinceName.append(province)
            provinceGold.append(values[0])
            provinceSilver.append(values[1])
            provinceBronze.append(values[2])
            provinceTotal.append(values[3])
            #print("Inserting into db: ")
            #print(medalTuple)

            #insert medalTuple into db here? tuple is medalTuple in the form (' Saskatchewan', '3', '3', '11', '17'), 
            # (provname, gold, silver, bronze, total)

            print("Insert successful.\n")
            
    except: print("Table unavailable.")
    #driver.close()

    newDict = {
        'Province Name' : provinceName,
        'Province Gold Medals' : provinceGold,
        'Province Silver Medals' : provinceSilver, 
        'Province Bronze Medals' : provinceBronze, 
        "Province Total Medals" : provinceTotal, 
    }

    table_csv = pd.DataFrame(newDict, columns=['Province Name','Province Gold Medals', 'Province Silver Medals', 'Province Bronze Medals', "Province Total Medals"])
    table_csv.to_csv("provincemedals.csv", index = [0, 1, 2, 3, 4], encoding = 'utf-8-sig')
    print(table_csv)
    print("Done.")
    return table_csv
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