from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = "https://niagara2022games.ca/news/"
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(url)
# /html/body/main/section/div/div/div[1]/div/div/small
# /html/body/main/section/div/div/div[1]/div/div/h1
# /html/body/main/section/div/div/div[1]/div/div/p


try:
    check = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-body")))
    print("page ready for scrape")
    newsList = driver.find_elements(By.CLASS_NAME, 'card-body')
    for e in newsList:
        news = e.text
        print(news)



except:

    pass

    """ 
    Output
    3/4/22
DIPAOLA DIPIETRO & LITTLE PARTNERS WITH NIAGARA 2022 AS OFFICIAL GAMES� ACCOUNTANTS
DDL & Co. will be providing Niagara 2022 with financial accounting support.
Read
2/22/22
NIAGARA 2022 PARTNERS WITH ICE RIVER GREEN BOTTLE CO. & GREENLID TO HELP HYDRATE AND FEED CANADA GAMES PARTICIPANTS
Ice River Green Bottle Co. and Greenlid will be providing healthy hydration and compostable cutlery at Niagara 2022.
Read
2/8/22
BUILDING ON NIAGARA�S ROWING LEGACY AT HENLEY ISLAND
Nestled in a quiet corner in the City of St. Catharines lies Henley Island � home to the new Henley Rowing Centre.
Read
1/31/22
TORCHBEARER NOMINATIONS NOW OPEN
Represent your local community in the lead up to Niagara 2022 by applying to take part in the Torch Relay!
Read
1/27/22
NIAGARA COLLEGE BECOMES THE OFFICIAL EXPERIENTIAL & DIGITAL PRODUCTION PARTNER OF THE NIAGARA 2022 CANADA SUMMER GAMES
Niagara College will be responsible for management and oversight of the full digital production of Niagara 2022.
Read
1/21/22
MAKING HER MARK � NEWFOUNDLAND & LABRADOR RISING STAR JAIDA LEE IS SET TO MAKE HISTORY IN NIAGARA
Jaida Lee is set to be the first-ever female to compete on a male baseball team at the Canada Games.
Read
1/7/22
REVISITING NIAGARA 2022�S BEST MOMENTS FROM 2021
We are looking back at our best and brightest highlights from the year 2021.
Read
12/22/21
RISE WITH GLOWING HEARTS CONCERT FOR NIAGARA 2022 CANADA SUMMER GAMES POSTPONED DUE TO THE ONGOING COVID-19 PANDEMIC
Niagara 2022 has made the decision to postpone next January�s Rise with Glowing Hearts concert to April 27, 2022.
Read
12/7/21
NIAGARA 2022 & NIAGARA TRAIL MAINTENANCE ASSOCIATION AIM TO LEAVE COMMUNITY LEGACY AT 12 MILE CREEK
70+ volunteers from the NTMA have put in close to 1000 hours of work developing & maintaining a trail at 12 Mile Creek.
Read
12/2/21
TWO BROCK GRADS ARE SET TO LEAD TEAM ONTARIO AT NIAGARA 2022
The Niagara 2022 Canada Summer Games will be a homecoming for Steve Sevor and Jennifer Bennett.
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
11/3/21
CHRISTINA NOTARIO BECOMES THE 1,000TH PERSON TO SUBMIT A VOLUNTEER APPLICATION
The 1,000th person to submit a volunteer application for the Niagara 2022 Canada Summer Games
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
CALL FOR ARTISTS
Niagara 2022 Games calling to performers to submit their application to take part in live cultural events.
Read
10/20/21
THREE NIAGARA CREDIT UNIONS COME TOGETHER TO SUPPORT THE NIAGARA 2022 CANADA SUMMER GAMES
Team Credit Union collaborative partners are calling on community members to follow their lead and join N22 Games.
Read
10/20/21
STRONGER TOGETHER � NIAGARA CREDIT UNIONS JOIN FORCES IN SUPPORT OF 2022 CANADA SUMMER GAMES
Learn how Niagara�s three credit unions are working together in support of the 2022 Canada Summer Games.
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
9/8/21
DECADES LATER, THUNDER BAY AND LONDON STILL ENJOY BENEFITS FROM HOSTING CANADA GAMES
The legacies continue to live on in the Ontario communities that once hosted the Canada Games.
Read
8/24/21
NIAGARA PARALYMPIANS PREPARE TO TAKE THE STAGE IN TOKYO
Niagara athletes will compete on the cycling track and water during the 2020 Summer Paralympic Games
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
NIAGARA OLYMPIANS HAVE THEIR EYES SET ON THE PODIUM IN TOKYO
The list of Niagara Olympians competing in the Tokyo Summer Olympics is small in numbers but high in medal hopes.
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
7/8/21
A BLUENOSER�S WINDING JOURNEY TO THE CANADA GAMES
It�s 30 years in the making since I was introduced to the Canada Games ideology.
Read
6/1/21
STATEMENT FROM THE CANADA GAMES FAMILY
The Canada Games family joins Canadians in mourning the horrific loss of 215 Indigenous children.
Read
5/31/21
NIAGARA 2022 AIMS TO SET NEW STANDARD IN ACCESSIBILITY
The Niagara 2022 Canada Summer Games hope to set a trend by making accessibility a priority.
Read
5/28/21
NIAGARA 2022 PARTNERS WITH PETERS CONSTRUCTION GROUP
Peters Construction Group is officially partnering up with the Niagara 2022 Canada Summer Games as a sponsor.
Read
5/20/21
CANADA GAMES PARK ON TRACK TO BE COMPLETED BY END OF 2021
In just 18 months, CGP is rapidly transforming into the state-of-the-art sport and recreation complex that was promised.
Read
4/23/21
SEEING THE CANADA GAMES THROUGH THE EYES OF A VOLUNTEER
Let�s get one thing straight: volunteers are the lifeblood of the Canada Games. 
Read
4/21/21
VOLUNTEER SPOTLIGHT: CLAUDE AND KATHY DALLAIRE
Sport has always been a way of life for Claude and Kathy Dallaire.
Read
4/19/21
VOLUNTEER SPOTLIGHT: CHRISTOPHER YOUNG AND TEMI ODUNUGA
Without volunteers, the Canada Games wouldn�t be possible.
Read
4/10/21
WRESTLING AND THE CANADA GAMES � A FAMILY AFFAIR FOR THE ROMANO�S
It�s all wrestling, all the time for Samantha, Katelyn and Matteo Romano.
Read
3/19/21
L�ASSEMBL�E DE LA FRANCOPHONIE DE L�ONTARIO NAMED FRANCOPHONE COMMUNITY NETWORK PARTNER OF THE NIAGARA 2022 CANADA SUMMER GAMES
L'AFO to become the Francophone Community Network Partner of the Niagara 2022 Canada Summer Games.
Read
3/5/21
IMPORTANCE OF DIVERSITY IN LEADERSHIP
Having the opportunity to be involved in the Niagara 2022 Canada Summer Games is very dear to my heart.
Read
11/25/20
AGE CATEGORIES FOR THE NIAGARA 2022 CANADA SUMMER GAMES
Find out the age categories for each sport featured at the Niagara 2022 Canada Summer Games
Read
11/12/20
NIAGARA HOST SOCIETY HOLDS GROUNDBREAKING CEREMONY FOR NEW HENLEY ROWING CENTRE IN ST. CATHARINES
Ground was officially broken in St. Catharines on Thursday afternoon for the Henley Rowing Centre
Read
10/26/20
NEW DATES ANNOUNCED FOR NIAGARA 2022 CANADA SUMMER GAMES
The Niagara 2022 Canada Summer Games have been rescheduled for August 6-21, 2022.
Read
9/25/20
NIAGARA CANADA SUMMER GAMES POSTPONEMENT - FAQS
Common questions and answers on the decision to postpone the Niagara Canada Summer Games.
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
7/21/20
CANADIAN TIRE CORPORATION BECOMES AN OFFICIAL PARTNER OF THE NIAGARA 2021 CANADA SUMMER GAMES
Canada�s iconic retailer will play an important role in helping deliver our country�s largest multi-sport event
Read
7/20/20
SETTING UP FOR SUCCESS: HOW TEAM PEI TRAINING TEAM ATHLETES ALINA CROCKETT AND ABBY HYNDMAN MAINTAIN TRAINING DURING A GLOBAL PANDEMIC
Many athletes are finding creative ways to continue their training during the unprecedented Covid-19 pandemic
Read
7/15/20
N21 PARTNERS STEP UP IN THE FIGHT AGAINST COVID-19
Many partners of the Niagara 2021 Canada Summer Games have been doing their part to help the Niagara Region
Read
7/13/20
NIAGARA 2021 CANADA SUMMER GAMES ANNOUNCES OFFICIAL FESTIVAL EXPERIENCE PARTNER
Absolute XM, an event management and festival planning agency, will assist with the creation of...
Read
6/17/20
CANADIAN JUNIOR VIRTUAL CYCLING SERIES GIVES N21 HOPEFULS A PREVIEW OF NEXT SUMMER�S ROAD RACE
Dylan Bibic got a virtual preview of the cycling course scheduled to be used at the Niagara 2021 Canada Summer Games
Read
6/9/20
MOSAIC NORTH AMERICA BECOMES AN OFFICIAL MARKETING PARTNER OF THE NIAGARA 2021 CANADA SUMMER GAMES
The 2021 Canada Games Host Society and Mosaic North America are excited to announce their partnership
Read
6/8/20
LEADING WITH PRIDE AT THE CANADA GAMES
The power of sport has the capability to bring people together and create a sense of belonging and inclusivity...
Read
5/28/20
16U BOYS & GIRLS BOX LACROSSE NATIONAL CHAMPIONSHIPS, 2020 MINTO CUP CANCELLED DUE TO ONGOING COVID-19 PANDEMIC
With continued public health concerns due to the ongoing COVID-19 pandemic...
Read
5/25/20
NIAGARA LIGHT OF HOPE UNITES REGION WITH MESSAGE OF HOPE AND SOLIDARITY AMIDST COVID-19 PANDEMIC
Altogether, the Niagara Light Hope travelled over 360 kilometres over the course of 17 days
Read
5/21/20
SOFTBALL CANADA CANCELS 2020 U14 & U16 BOYS CANADIAN FAST PITCH CHAMPIONSHIPS DUE TO ONGOING COVID-19 PANDEMIC
U14 & U16 Boys Canadian Fast Pitch Championships were originally scheduled to take place from August 5th to 9th, 2020
Read
5/1/20
NIAGARA 2021 CANADA SUMMER GAMES AND PSI NIAGARA TO PRESENT �NIAGARA LIGHT OF HOPE� DURING THE MONTH OF MAY ACROSS THE REGION
Coming together to unify Niagara�s residents with a message of hope and solidarity
Read
4/25/20
HONOURING OUR VOLUNTEERS : CAROL PHILLIPS
Giving thanks to our Volunteer Services Committee Chair.
Read
4/24/20
HONOURING OUR VOLUNTEERS : IAVOR PERDUHOV & HARVIE HAGERTY
Giving thanks to our Fit-out and Venue Committee Chairs.
Read
4/23/20
HONOURING OUR VOLUNTEERS: SUE MORIN
Giving thanks to our Official Languages Committee Chair.
Read
4/22/20
HONOURING OUR VOLUNTEERS: CRYSTAL VELLA & JANE ARKELL
Giving thanks to our Accessibility and Sustainability Committee Chairs.
Read
4/21/20
HONOURING OUR VOLUNTEERS: GERRY MCILHONE & ROB FOSTER
Giving thanks to our Transportation and Technology Committee Chairs.
Read
4/20/20
HONOURING OUR VOLUNTEERS: BILL FENWICK
Giving thanks to our Games Services Committee Chair.
Read
3/25/20
PSI NIAGARA BECOMES OFFICIAL AUDIO-VISUAL & SHOW SUPPLIER OF THE NIAGARA 2021 CANADA SUMMER GAMES
PSI Niagara helps to deliver an unforgettable experience to all our spectators and participants from across the country.
Read
3/11/20
MERIDIAN CREDIT UNION BECOMES OFFICIAL SPONSOR OF THE NIAGARA 2021 CANADA SUMMER GAMES VOLUNTEER PROGRAM
Ontario-based credit union will play an important role in supporting over 4,000 volunteers for the Games.
Read
3/5/20
SPOTLIGHT ON: LYNN HAMILTON
In honour of International Women�s Day, get to know Lynn Hamilton - our Sport Chair!
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
1/10/20
NIAGARA 2021 MEDAL DESIGN PROGRAM � CALL FOR PORTFOLIOS
Announcing an open call to artists to submit portfolios for the design of the 2021 Canada Games medals.
Read
12/16/19
CANADA GAMES PARK OFFICIALLY BREAKS GROUND
The ceremony officially kicked off partnerships and the beginning of construction on the site.
Read
12/7/19
A SUCCESSFUL TEST EVENT FOR THE NIAGARA 2021 CANADA SUMMER GAMES HOST SOCIETY
The Niagara 2021 Canada Summer Games Host Society was proud to co-host a successful Canadian Wrestling Trials.
Read
12/5/19
CONTRACTOR SELECTED TO BUILD LEGACY PROJECTS FOR NIAGARA 2021 CANADA SUMMER GAMES
Ontario based construction company has won the bid to build the legacy project facilities for the Games.
Read
11/19/19
REGATTASPORT A PERFECT FIT FOR THE NIAGARA 2021 CANADA SUMMER GAMES
RegattaSport is named the official licensed merchandiser of the Niagara 2021 Canada Summer Games.
Read
11/10/19
INTRODUCING SHELLY!
We are excited to officially introduce Shelly, the Niagara 2021 Canada Summer Games mascot!
Read
10/24/19
GET READY TO MEET OUR MASCOT!
Join us on November 10 at Rogers Hometown Hockey in Welland and be the first to meet our mascot!
Read
10/11/19
GET YOUR TICKETS FOR THE 2019 CANADIAN WRESTLING TRIALS IN NIAGARA
Canada's top wrestlers vying for a spot on the national team for Tokyo 2020
Read
10/8/19
FULL STEAM AHEAD FOR NIAGARA 2021 INFRASTRUCTURE PROJECTS
Government funding has been committed to move forward with the 2021 Canada Games Infrastructure Project.
Read
7/5/19
THE COUNTDOWN IS ON
Live music, fireworks, food trucks and Niagara craft beverages and more!
Read
6/30/19
MASCOT CHALLENGE CLOSES AND SUBMISSIONS ARE IN REVIEW
Our panel of judges will review all submissions over the course of summer 2019 and winners will be notified soon
Read
6/21/19
NIAGARA 2021 CANADA SUMMER GAMES CELEBRATES NATIONAL INDIGENOUS HISTORY MONTH
National Indigenous Peoples Day � commemorating the cultures and contributions of Indigenous Peoples in Canada
Read
5/23/19
NIAGARA�S YOUTH TO NAME & DESIGN 2021 CANADA GAMES MASCOT
Our mascot will have a very visible presence throughout Niagara in the lead up to and during the Canada Games.
Read
5/13/19
2021 CANADA GAMES WILL BE BIGGER THAN WINTER OLYMPICS
Once, and for all. That�s a phrase that Niagara residents will be seeing and hearing a lot of.
Read

    
    
    
    
    """
