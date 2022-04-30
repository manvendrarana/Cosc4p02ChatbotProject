from selenium import webdriver
from selenium.webdriver.common.by import By


# DRIVER_PATH = "C:\webdriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)

class ProvinceMedalScraper:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def scrape(self):
        self.driver.get("https://cg2019.gems.pro/Result/MedalList.aspx?SetLanguage=en-CA")
        provinceName = []
        provinceGold = []
        provinceSilver = []
        provinceBronze = []
        provinceTotal = []

        medArray = []
        self.driver.get("https://cg2019.gems.pro/Result/MedalList.aspx?SetLanguage=en-CA")

        try:
            table = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_tblMedals")
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
                    pass
                    # print("Datacell unavailable.")

            for province, values in medalDict.items():
                # print("Province Name: " + province)
                # print("Gold Medals: " + values[0])
                # print("Silver Medals: " + values[1])
                # print("Bronze Medals: " + values[2])
                # print("Total Medals: " + values[3])
                # print("\n")

                # medalTuple = (province, values[0], values[1], values[2], values[3])

                answerString = "{} got {} total medals, {} gold medals, {} silver medals, {} bronze medals".format(
                    province, values[3], values[0], values[1], values[2])

                medArray.append([answerString])

                # provinceName.append(province)
                # provinceGold.append(values[0])
                # provinceSilver.append(values[1])
                # provinceBronze.append(values[2])
                # provinceTotal.append(values[3])
                # print("Inserting into db: ")
                # print(medalTuple)

                # insert medalTuple into db here? tuple is medalTuple in the form (' Saskatchewan', '3', '3', '11', '17'),
                # (provname, gold, silver, bronze, total)


        except:
            pass
            # print("Table unavailable.")
        # driver.close()

        newDict = {
            'Answer': medArray,
        }

        # try:
        #     table_csv = pd.DataFrame(newDict,
        #                              columns=['Province Name', 'Province Gold Medals', 'Province Silver Medals',
        #                                       'Province Bronze Medals', "Province Total Medals"])
        #     table_csv.to_csv("provincemedals.csv", index=[0, 1, 2, 3, 4], encoding='utf-8-sig')
        #     print(table_csv)
        #     print("Done.")
        #     # return table_csv
        # except:
        #     print("Couldn't make CSV.")

        key = "info_province_medals"
        documents = {}
        documents[key] = {
            "url": "https://cg2019.gems.pro/Result/MedalList.aspx?SetLanguage=en-CA",
            "title": key.replace("_", " ").capitalize(),
            "section_title": "Province Medals",
            "columns": ["Province Medals"],
            "values": medArray
        }
        # print(documents)
        return documents

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
