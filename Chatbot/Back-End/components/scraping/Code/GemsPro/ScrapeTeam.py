from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

PATH = "C:\Program Files (x86)\chromedriver.exe" 
driver = webdriver.Chrome(PATH)

driver.get("https://cg2019.gems.pro/Result/ShowTeam_List.aspx?SetLanguage=en-CA")

driver.find_element(By.CLASS_NAME, "LM_Button").click()


try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'DataCell')))
    print("Page is ready!")
    rowEven = driver.find_elements(By.CLASS_NAME, 'DataCell')
    for item in rowEven:
        try:
            print(item.text)
        except:
            pass
except TimeoutException:
    print("Loading took too much time!")

driver.close();