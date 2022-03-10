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

url = "https://niagara2022games.ca/media/releases/"
PATH = "C:\Program Files (x86)\chromedriver.exe" 
driver = webdriver.Chrome(PATH)


driver.get(url)





try:
    check = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-body")))
    print("page ready for scrape")
    newsList = driver.find_elements(By.CLASS_NAME,'card-body')
    for e in newsList:
        news = e.text
        print(news)
    
    

except:
    
    pass



    """
    1/27/22
NIAGARA COLLEGE BECOMES THE OFFICIAL EXPERIENTIAL & DIGITAL PRODUCTION PARTNER OF THE NIAGARA 2022 CANADA SUMMER GAMES
Niagara College will be responsible for management and oversight of the full digital production of Niagara 2022.
Read
12/22/21
RISE WITH GLOWING HEARTS CONCERT FOR NIAGARA 2022 CANADA SUMMER GAMES POSTPONED DUE TO THE ONGOING COVID-19 PANDEMIC
Niagara 2022 has made the decision to postpone next January�s Rise with Glowing Hearts concert to April 27, 2022.
Read
11/10/21
ALGOMA CENTRAL CORPORATION TO BRING THE SPIRIT OF NEWFOUNDLAND AND LABRADOR TO THE NIAGARA 2022 CANADA SUMMER GAMES
The Niagara 2022 Host Society is thrilled to announce its partnership with Algoma Central Corporation.
Read
11/9/21
TIM HICKS, LOVERBOY, POESY AND JEREMIE ALBINO TO PERFORM AT 200-DAY-OUT CONCERT FOR THE NIAGARA 2022 CANADA SUMMER GAMES
'Rise with Glowing Hearts' will celebrate the 200-day countdown to the Niagara 2022 Canada Summer Games.
Read
11/5/21
POESY AND NIAGARA HOST SOCIETY RELEASE �STEEL HEART� � THE ANTHEM OF THE NIAGARA 2022 CANADA SUMMER GAMES
The Niagara Host Society and POESY are thrilled to announce the release of �Steel Heart� as Niagara 2022's anthem.
Read
10/25/21
NIAGARA 2022 CANADA SUMMER GAMES OPENS PORTAL FOR APPLICANTS SEEKING GAMES-TIME VOLUNTEER ROLES
Niagara 2022 Host Society inviting residents from the Niagara Region and beyond to apply for the volunteer positions.
Read
10/22/21
GFL TEAMS UP WITH NIAGARA 2022 AS THE GAMES� OFFICIAL SUSTAINABILITY PARTNER
GFL is the Official Sustainability and Exclusive Waste Management Partner of the Niagara 2022 Canada Summer Games.
Read
10/20/21
THREE NIAGARA CREDIT UNIONS COME TOGETHER TO SUPPORT THE NIAGARA 2022 CANADA SUMMER GAMES
Team Credit Union collaborative partners are calling on community members to follow their lead and join N22 Games.
Read
10/6/21
CANADA STEAMSHIP LINES AND NIAGARA HOST SOCIETY REVEAL PARTNERSHIP AND EXCITING PLANS FOR THE TORCH RELAY PROGRAM OF THE NIAGARA 2022 CANADA SUMMER GAMES
Niagara 2022�s Torch Relay program, presented by Canada Steamship Lines (CSL)
Read
10/4/21
ACCENTURE TO BE OFFICIAL PARTNER OF DIVERSITY AND INCLUSION FOR THE NIAGARA 2022 CANADA SUMMER GAMES
Accenture will support the Niagara 2022 Canada Summer Games in creating a welcoming environment for all
Read
9/16/21
NIAGARA 2022 CANADA SUMMER GAMES CELEBRATES OFFICIAL OPENING OF THE MERIDIAN VOLUNTEER CENTRE
The Meridian Volunteer Centre will act as a central hub for Niagara 2022 volunteers and serve as a welcome centre
Read
8/10/21
NIAGARA 2022 CELEBRATES ONE YEAR OUT FROM CANADA SUMMER GAMES
Last Friday, we passed the one year mark from the start of the Niagara 2022 Canada Summer Games
Read
8/4/21
FEDERAL GOVERNMENT ANNOUNCES UP TO $1.1-MILLION IN FUNDING FOR THE NIAGARA 2022 CANADA SUMMER GAMES
Across from Canada Games Park (CGP) yesterday, the Honourable Steven Guilbeault, Minister of Canadian Heritage...
Read
7/22/21
SPORTS AND ABILITIES CENTRE AT CANADA GAMES PARK NAMED IN HONOUR OF WALKER FAMILY
The Walker Sports and Abilities Centre at CGP is a state-of-the-art facility designed to be accessible for everyone.
Read
7/20/21
FIRSTONTARIO CREDIT UNION ANNOUNCED AS OFFICIAL SPONSOR OF THE NIAGARA 2022 CANADA SUMMER GAMES
FirstOntario Credit Union has become an official partner of the Niagara 2022 Canada Summer Games
Read
7/15/21
ALECTRA BECOMES OFFICIAL ENERGY SUPPLIER OF THE NIAGARA 2022 CANADA SUMMER GAMES
The Niagara Host Society is thrilled to announce its partnership with Alectra
Read
7/13/21
PENFINANCIAL JOINS THE NIAGARA 2022 CANADA SUMMER GAMES AS AN OFFICIAL PARTNER
PenFinancial Credit Union has become an official partner of the Niagara 2022 Canada Summer Games
Read
5/28/21
NIAGARA 2022 PARTNERS WITH PETERS CONSTRUCTION GROUP
Peters Construction Group is officially partnering up with the Niagara 2022 Canada Summer Games as a sponsor.
Read
3/19/21
L�ASSEMBL�E DE LA FRANCOPHONIE DE L�ONTARIO NAMED FRANCOPHONE COMMUNITY NETWORK PARTNER OF THE NIAGARA 2022 CANADA SUMMER GAMES
L'AFO to become the Francophone Community Network Partner of the Niagara 2022 Canada Summer Games.
Read
11/12/20
NIAGARA HOST SOCIETY HOLDS GROUNDBREAKING CEREMONY FOR NEW HENLEY ROWING CENTRE IN ST. CATHARINES
Ground was officially broken in St. Catharines on Thursday afternoon for the Henley Rowing Centre
Read
10/26/20
NEW DATES ANNOUNCED FOR NIAGARA 2022 CANADA SUMMER GAMES
The Niagara 2022 Canada Summer Games have been rescheduled for August 6-21, 2022.
Read
9/16/20
NIAGARA 2021 CANADA SUMMER GAMES POSTPONED DUE TO THE ONGOING COVID-19 PANDEMIC
The Niagara 2021 Canada Games will be postponed until the summer of 2022.
Read
8/6/20
2021 CANADA GAMES HOST SOCIETY ANNOUNCES CREATION OF THE INDIGENOUS PARTNERSHIP COUNCIL
Canada Games Host Society partners with a council represented by various Indigenous communities.
Read
7/29/20
2021 CANADA GAMES HOST SOCIETY SELECTS NIAGARA-BASED ARTIST AS WINNER OF THE MEDAL DESIGN PROGRAM
Shaun O�Melia, a native of St. Catharines and an alumnus of Niagara College, will design the medals that will be...
Read
7/15/20
N21 PARTNERS STEP UP IN THE FIGHT AGAINST COVID-19
Many partners of the Niagara 2021 Canada Summer Games have been doing their part to help the Niagara Region
Read
7/13/20
NIAGARA 2021 CANADA SUMMER GAMES ANNOUNCES OFFICIAL FESTIVAL EXPERIENCE PARTNER
Absolute XM, an event management and festival planning agency, will assist with the creation of...
Read
6/9/20
MOSAIC NORTH AMERICA BECOMES AN OFFICIAL MARKETING PARTNER OF THE NIAGARA 2021 CANADA SUMMER GAMES
The 2021 Canada Games Host Society and Mosaic North America are excited to announce their partnership
Read
5/21/20
SOFTBALL CANADA CANCELS 2020 U14 & U16 BOYS CANADIAN FAST PITCH CHAMPIONSHIPS DUE TO ONGOING COVID-19 PANDEMIC
U14 & U16 Boys Canadian Fast Pitch Championships were originally scheduled to take place from August 5th to 9th, 2020
Read
5/1/20
NIAGARA 2021 CANADA SUMMER GAMES AND PSI NIAGARA TO PRESENT �NIAGARA LIGHT OF HOPE� DURING THE MONTH OF MAY ACROSS THE REGION
Coming together to unify Niagara�s residents with a message of hope and solidarity
Read
3/25/20
PSI NIAGARA BECOMES OFFICIAL AUDIO-VISUAL & SHOW SUPPLIER OF THE NIAGARA 2021 CANADA SUMMER GAMES
PSI Niagara helps to deliver an unforgettable experience to all our spectators and participants from across the country.
Read
3/11/20
MERIDIAN CREDIT UNION BECOMES OFFICIAL SPONSOR OF THE NIAGARA 2021 CANADA SUMMER GAMES VOLUNTEER PROGRAM
Ontario-based credit union will play an important role in supporting over 4,000 volunteers for the Games.
Read
2/26/20
NIAGARA REGION TO HOST U14 & U16 BOYS CANADIAN FAST PITCH CHAMPIONSHIPS FOR THE FIRST TIME
U14 and U16 Boys Canadian Fast Pitch Championships to take place in Grimsby and Lincoln � August 5th to 9th, 2020.
Read
1/15/20
LOCAL, FAMILY-OWNED GAS COMPANY TO SERVE AS THE OFFICIAL FUEL SUPPLIER OF THE GAMES
Gale�s Gas Bars Limited has been named the official fuel supplier of the Niagara 2021 Canada Summer Games.
Read
1/14/20
ST. CATHARINES WINS BID TO HOST THE 2020 MINTO CUP
The 2020 Minto Cup will take place in St. Catharines at the same time as the U16 Canadian Box Lacrosse Nationals.
Read
12/16/19
CANADA GAMES PARK OFFICIALLY BREAKS GROUND
The ceremony officially kicked off partnerships and the beginning of construction on the site.
Read
12/5/19
CONTRACTOR SELECTED TO BUILD LEGACY PROJECTS FOR NIAGARA 2021 CANADA SUMMER GAMES
Ontario based construction company has won the bid to build the legacy project facilities for the Games.
Read
11/19/19
REGATTASPORT A PERFECT FIT FOR THE NIAGARA 2021 CANADA SUMMER GAMES
RegattaSport is named the official licensed merchandiser of the Niagara 2021 Canada Summer Games.
Read
    
    """