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

url = "https://niagara2022games.ca/about/alumni/"
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
7/21/21
JOURNEYING TO TOKYO FOR ONE FINAL RUN � JENNIFER SALLING
13 years ago, the dream of the Canadian Women�s National Softball Team seemed lost forever.
Read
7/19/21
CANADA GAMES ALUMNI TO WATCH AT THE TOKYO OLYMPICS AND PARALYMPICS
Many Canadian hopefuls headed to Tokyo are a large number of athletes who once upon a time competed at the Canada Games
Read
6/17/21
ALUMNI SPOTLIGHT: SHARON FIRTH
This past winter marked the 50th anniversary of Sharon Firth�s first appearance at the Canada Winter Games.
Read
5/13/21
ALUMNI SPOTLIGHT: PETER STEFANIUK
Stefaniuk still has his mementos from the 1971 Games in Saskatoon, Sask.
Read
3/8/21
GROWING THE GAME - STACEY ALLASTER
A look at Stacey Allaster's journey from Welland, Ont., to becoming the US Open's first-ever female tournament director.
Read
2/25/21
INSPIRING THE NEXTGEN � SHANICE MARCELLE
To understand the importance Marcelle places on her Black roots, one must understand her journey.
Read
2/8/21
CELEBRATING THE ACCOMPLISHMENTS OF BLACK CANADA GAMES ALUMNI
In honour of Black History Month, we look back at the amazing achievements of Black Canada Games athletes and coaches.
Read
12/17/20
RISING TO THE OCCASION - C�LESTE DAO
A look at C�leste Dao's winding path from the 2017 Canada Games to the University of Georgia.
Read
11/19/20
ALUMNI SPOTLIGHT: BRIAN BLEICH
Brian Bleich is giving back to the Canada Games 33 years after competing in them.
Read
9/10/20
ALUMNI SPOTLIGHT: MICHELLE FAZZARI
Michelle Fazzari credits the 2005 Canada Games as the turning point in her wrestling career.
Read
8/27/20
FROM PODIUMS TO PARLIAMENT - ADAM VAN KOEVERDEN
Adam van Koeverden was once just a teenager trying to find his way.
Read
7/30/20
ALUMNI SPOTLIGHT: GREG FRANCIS
Greg Francis thought he was a hard worker until he met Jay Triano.
Read
7/9/20
ALUMNI SPOTLIGHT: RICHARD DALTON
Twenty-seven years after competing as a 13-year-old in the Canada Summer Games in Kamloops, B.C....
Read
6/29/20
FOREVER CONNECTED BY THE CANADA GAMES
How Lisa Thomaidis� and Carly Clarke�s worlds collided at the 2001 Canada Games.
Read
6/18/20
ALUMNI DAVID THIBODEAU ON HIS CANADA GAMES EXPERIENCE AND ADVANCING LGBTQI2S AWARENESS IN SPORT
Read about how Canada Games Alumni David Thibodeau is making waves in the LGBTQI2S community.
Read
6/11/20
SPOTLIGHT: DON GOODWIN
Without the late Don Goodwin, there would likely be no Canada Games.
Read
6/6/20
PERSEVERING THROUGH A PANDEMIC - THE MEGAN VAN HEYST STORY
How one Niagara 2021 hopeful, her parents and coach have adjusted amidst the outbreak of COVID-19
Read
5/28/20
ALUMNI SPOTLIGHT: MAKIAH HUNT
The moment is indelibly etched in the memory of Makiah Hunt.
Read
5/14/20
ALUMNI SPOTLIGHT: JAYSON HILCHIE
Get to know Jayson Hilchie, Team Nova Scotia's 4x100m gold medalist at the 2001 Canada Summer Games!
Read
4/30/20
ALUMNI SPOTLIGHT: SIOBHAN MCLAUGHLIN
Siobhan McLaughlin�s Canada Summer Games resume is impressive.
Read
4/16/20
ALUMNI SPOTLIGHT: HANNAH TAYLOR
Hannah Taylor was a Canada Games athlete for all seasons.
Read
4/9/20
ALUMNI SPOTLIGHT: NANCY KESSLER
Get to know Nancy Kessler, a St. Catharines native and 2013 Canada Games gold medalist!
Read
4/2/20
CANADA GAMES ALUMNI SPOTLIGHT: SWEDE BURAK
Get to know Swede Burak, Team Ontario's rowing coach at the 2017 Canada Summer Games!
Read
3/19/20
CANADA GAMES ALUMNI SPOTLIGHT: SARAH WILEY
Get to know St. Catharines native and 2009 Canada Games gold medalist, Sarah Wiley!
Read
3/12/20
CANADA GAMES ALUMNI SPOTLIGHT: CLAYTON PYE
Get to know Brock Wrestling athlete and 2013 Canada Games Alumni Clayton Pye!
Read
2/27/20
CANADA GAMES ALUMNI SPOTLIGHT: TREVOR VAN NEST
In our first Alumni Spotlight series, get to know 1989 Canada Games Alumni and Niagara Falls resident, Trevor Van Nest.
Read

    
    """