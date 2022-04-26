from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# DRIVER_PATH = "C:\webdriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)

class SportsDateScraper:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def scrape(self):
        self.driver.get(
            "https://cg2022.gems.pro/Result/Sport_List.aspx?SiteMapTreeExpanded=b970b19b-cbed-45c9-9e45-5fee884be016&SetLanguage=en-CA")

        delay = 5  # seconds
        try:
            awaitElement = WebDriverWait(self.driver, delay).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'tr>td>a>img')))
            # print("Page is ready!")
        except:
            pass
            # print("Page is taking too long")

        try:
            dataCell = self.driver.find_elements(By.CLASS_NAME, 'DataCell')
            sportDict = {}
        except:
            pass
            # print("Couldn't find table cells")
        try:
            for item in dataCell:
                try:
                    splitArray = []
                    itemCell = item.find_element(By.CSS_SELECTOR, "a")
                    splitArray = itemCell.get_attribute('title').split("\n")
                    sportName = splitArray[0]
                    sportTime = splitArray[1]
                    if sportName not in sportDict:
                        sportDict[sportName] = list()
                    sportDict[sportName].append(sportTime)
                except:
                    pass
        except TimeoutException:
            pass
            # print("Can't iterate through cells")

        sportName = []
        sportTimes = []
        sportList = []
        for sport in sportDict:
            # print("\n\nSport name: " + sport)
            sportName.append(sport)
            # print("Sport tuples:")
            timeString = ""
            for times in sportDict[sport]:
                if timeString != "":
                    timeString = timeString + ", and " + times
                if timeString == "":
                    timeString = timeString + times
                # sports_date_tuple = (sport, times)
                # print(sports_date_tuple)
            sportTimes.append(timeString)
            sportList.append([sport, timeString])
        # print("\n")
        # print(sportDict)

        # newDict = {
        #     'Sports Names': sportName,
        #     'Sports Times': sportTimes
        # }
        #
        # try:
        #     table_csv = pd.DataFrame(newDict, columns=['Sports Names', 'Sports Times'])
        #     table_csv.to_csv("sports_dates.csv", index=[0, 1, 2, 3, 4, 5], encoding='utf-8-sig')
        #     # print(table_csv)
        #     # print("Done.")
        #     # return table_csv
        # except:
        #     pass
        #     # print("Couldn't make CSV.")

        key = "info_sports_dates"
        documents = {
            key: {
                "url": "https://cg2022.gems.pro/Result/Sport_List.aspx?SiteMapTreeExpanded=b970b19b-cbed-45c9-9e45-5fee884be016&SetLanguage=en-CA",
                "title": key.replace("_", " ").capitalize(),
                "section_title": "Sports Name, Sports Dates",
                "columns": ["Sports Name", "Sports Dates"],
                "values": sportList
            }}

        return documents

    # driver.close();

    '''
    Example output

    Sport name: Volleyball
    Sport dates:
    Monday, August 8, 2022
    Tuesday, August 9, 2022
    Thursday, August 11, 2022
    Friday, August 12, 2022
    Saturday, August 13, 2022
    Tuesday, August 16, 2022
    Wednesday, August 17, 2022
    Thursday, August 18, 2022
    Friday, August 19, 2022
    Saturday, August 20, 2022
    Sunday, August 21, 2022


    Sport name: Wrestling
    Sport dates:
    Tuesday, August 9, 2022
    Wednesday, August 10, 2022
    Thursday, August 11, 2022

    dictionary contents:

    {'Athletics': ['Tuesday, August 16, 2022', 'Wednesday, August 17, 2022', 'Friday, August 19, 2022', 'Saturday, August 20, 2022'], 'Baseball': ['Sunday, August 7, 2022', 'Monday, August 8, 2022', 'Tuesday, August 9, 2022', 'Wednesday, August 10, 2022', 'Friday, August 12, 2022', 'Saturday, August 13, 2022'], 'Basketball': ['Monday, August 8, 2022', 'Tuesday, August 9, 2022', 'Wednesday, August 10, 2022', 'Thursday, August 11, 2022', 'Friday, August 12, 2022', 'Saturday, August 13, 2022'], 'Box Lacrosse': ['Sunday, August 7, 2022', 'Monday, August 8, 2022', 'Tuesday, August 9, 2022', 'Wednesday, August 10, 2022', 'Thursday, August 11, 2022', 'Friday, August 12, 2022', 'Tuesday, August 16, 2022', 'Wednesday, August 17, 2022', 'Thursday, August 18, 2022', 'Friday, August 19, 2022', 'Saturday, August 20, 2022', 'Sunday, August 21, 2022'], 'Canoe Kayak': ['Tuesday, August 16, 2022', 'Wednesday, August 17, 2022', 'Thursday, August 18, 2022', 'Friday, August 19, 2022'], 'Cycling': ['Monday, August 8, 2022', 'Wednesday, August 10, 2022', 'Friday, August 12, 2022', 'Tuesday, August 16, 2022', 'Thursday, August 18, 2022', 'Saturday, August 20, 2022'], 'Diving': ['Tuesday, August 16, 2022', 'Wednesday, August 17, 2022', 'Thursday, August 18, 2022', 'Saturday, August 20, 2022', 'Sunday, August 21, 2022'], 'Golf': ['Wednesday, August 17, 2022', 'Thursday, August 18, 2022', 'Friday, August 19, 2022', 'Saturday, August 20, 2022'], 'Rowing': ['Wednesday, August 17, 2022', 'Thursday, August 18, 2022', 'Saturday, August 20, 2022', 'Sunday, August 21, 2022'], 'Rugby Sevens': ['Monday, August 8, 2022', 'Tuesday, August 9, 
    2022'], 'Sailing': ['Wednesday, August 17, 2022', 'Thursday, August 18, 2022', 'Friday, August 19, 2022', 'Saturday, August 20, 2022'], 'Soccer': ['Sunday, August 7, 2022', 'Monday, August 8, 2022', 'Tuesday, August 9, 2022', 'Thursday, August 11, 2022', 'Friday, August 12, 2022', 'Tuesday, August 16, 2022', 'Wednesday, August 17, 2022', 'Thursday, August 18, 
    2022', 'Saturday, August 20, 2022', 'Sunday, August 21, 2022'], 'Softball': ['Sunday, August 7, 2022', 'Monday, August 8, 2022', 'Tuesday, August 9, 2022', 'Wednesday, August 10, 2022', 'Thursday, August 11, 2022', 'Friday, August 12, 2022', 'Tuesday, August 16, 2022', 'Wednesday, August 17, 2022', 'Thursday, August 18, 2022', 'Friday, August 19, 2022', 'Saturday, August 20, 2022', 'Sunday, August 21, 2022'], 'Swimming': ['Sunday, August 7, 2022', 'Monday, August 8, 2022', 'Tuesday, August 9, 2022', 'Wednesday, August 10, 2022', 'Thursday, August 11, 2022', 'Friday, August 12, 2022'], 'Tennis': ['Sunday, August 7, 2022', 'Monday, August 8, 2022', 'Tuesday, August 9, 2022', 'Wednesday, August 10, 2022', 'Thursday, August 11, 2022', 'Friday, August 12, 2022', 'Saturday, August 13, 2022'], 'Triathlon': ['Monday, August 8, 2022', 'Thursday, August 11, 2022', 'Friday, August 12, 2022'], 'Volleyball': ['Monday, August 8, 2022', 'Tuesday, August 9, 2022', 'Thursday, August 11, 2022', 'Friday, August 12, 2022', 'Saturday, August 13, 2022', 'Tuesday, August 16, 2022', 'Wednesday, August 17, 2022', 'Thursday, August 18, 2022', 'Friday, August 19, 2022', 'Saturday, August 20, 2022', 'Sunday, August 21, 2022'], 'Wrestling': ['Tuesday, August 9, 2022', 'Wednesday, August 10, 2022', 'Thursday, August 11, 2022']}
    '''
