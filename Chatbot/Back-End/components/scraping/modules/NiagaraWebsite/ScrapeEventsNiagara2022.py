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

url = "https://niagara2022games.ca/events/"
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
March 15, 2022
TURTLE TUESDAY
Live demonstration with the turtle ambassadors of with Ontario Turtle Conservation Centre!
Details
May 7, 2022
ONCE, AND FOR ALL | COMMUNITY GOLF TOURNAMENT
Join us and become a part of the support movement that will inspire, transform, and unify Niagara.
Details
April 27, 2022
RISE WITH GLOWING HEARTS CELEBRATION CONCERT
100-day-out Celebration Concert for the Niagara 2022 Canada Summer Games
Details
January 6, 2022
N22 TOURISM FORUM � JAN 6, 2022
Learn how you can promote your business prior to and during the Niagara 2022 Canada Summer Games.
Details
November 25, 2021
N22 TOURISM FORUM
Learn how you can promote your business prior to and during the Niagara 2022 Canada Summer Games
Details
November 19, 2021
NIAGARA SUSTAINABILITY AND SPORT: THE LIFE CYCLE OF A SPORTING EVENT
This event is a follow up to the Spring �21 Sustainability Sport Summit
Details
October 1, 2021
TOURNAMENT OF TRADES
Become part of the movement
Details
April 27, 2021
� BIENVENUE/WELCOME � VIRTUAL EVENT
Together, we can build a powerful team of bilingual volunteers!
Details
April 9, 2021
AN INTRODUCTION TO SUSTAINABILITY IN SPORT
What happens when the worlds of sustainability and sport collide?
Details
July 30-2, 2020
NIAGARA EMANCIPATION DAY STC CELEBRATION
#EmancipationDaySTC Celebrations brings back a piece of history and to celebrate Black Culture.
Details
May 23, 2020
VIRTUAL WORLD TURTLE DAY
Join us on a virtual field trip as we celebrate World Turtle Day on Saturday, May 23!
Details
February 29, 2020
ONTARIO ERGOMETER CHAMPIONSHIPS
Ridley College hosts stationary rowing competition!
Details
March 17, 2020
TURTLE TUESDAY MARCH BREAK FAMILY EVENT
Join Shelly and friends and get up close and personal with a live turtle!
Details
February 8, 2020
CHORUS NIAGARA 14TH ANNUAL SINGATHON
Signathon with our mascot Shelly conducting!
Details
December 16, 2019
CANADA GAMES PARK GROUNDBREAKING CEREMONY
We are pleased to celebrate the start of the construction of Canada Games Park.
Details
December 19, 2019
SHELLY AT MERIDIAN CENTRE FOR PUCK DROP AT �UGLY CHRISTMAS SWEATER� GAME
Shelly at Meridian Centre for Puck Drop at "Ugly Christmas Sweater" Game
Details
December 5-7, 2019
CANADIAN WRESTLING TRIALS
Trials will serve as an opportunity for the nation�s best wrestlers to compete for a spot at the 2020 Tokyo Olympics
Details



"""