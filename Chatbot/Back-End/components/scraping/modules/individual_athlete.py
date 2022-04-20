from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# this GUID has a page with more txt sections
# GUID = "80befcce-cda0-4b35-9022-364ce2e1d1fe"

# this GUID has less txt sections so some elements won't exist
# GUID = '32d36b04-4953-44d6-af58-9a4f058e9198'

def countMedals(array, type):
    return sum(type in arr for arr in array)


def scrape_individual_athlete(GUID, driver):
    url = 'https://cg2019.gems.pro/Result/ShowPerson.aspx?Person_GUID=' + GUID + '&SetLanguage=en-CA'

    # DRIVER_PATH = "C:\webdriver\chromedriver.exe"
    # driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    driver.get(url)

    txtName = ""
    dictName = "Athlete Name"

    txtContingent = ""
    dictContingent = "Athlete Province"

    txtType = ""
    dictType = "Athlete or Coach"

    txtSport = ""
    dictSport = "Athlete Sport"

    txtAge = ""
    dictAge = "Athlete Age"

    txtHeight = ""
    dictHeight = "Athlete Height"

    txtWeight = ""
    dictWeight = "Athlete Weight"

    txtClubTeam = ""
    dictClubTeam = "Athletes Clubs or Teams"

    txtCoach = ""
    dictCoach = "Athletes Coaches Name"

    txtTeamPosition = ""
    dictTeamPosition = "Athletes Team Position"

    txtPrevSameGames = ""
    dictPrevSameGames = "Athletes Same Previous Games"

    txtPrevGames = ""
    dictPrevGames = "Athletes Previous Games"

    txtGoals = ""
    dictGoals = "Athletes Goals"

    txtPersonalBest = ""
    dictPersonalBest = "Athletes Personal Best"

    txtAwards = ""
    dictAwards = "Athletes Awards"

    txtRoleModel = ""
    dictRoleModel = "Athletes Role Model"

    txtMediaInfo = ""
    dictMediaInfo = "Athletes Media or Social Media Information"

    athleteEvents = []
    athleteConcatEvents = ""
    dictEvents = "Events Participated In"

    athleteGolds = []
    athleteGoldsCount = 0
    dictGolds = "Athletes Number of Gold Medals"

    athleteSilvers = []
    athleteSilversCount = 0
    dictSilvers = "Athletes Number of Silver Medals"

    athleteBronzes = []
    athleteBronzesCount = 0
    dictBronzes = "Athletes Number of Bronze Medals"

    athletePlacings = []
    athletePlacingCount = 0
    dictPlacings = "Athletes Placements"

    try:
        try:
            txtName = driver.find_element(By.ID, 'txtPersonNameFML').text
            print(txtName)
        except:
            print("Couldn't find player name.")

        try:
            # province
            txtContingent = driver.find_element(By.ID, 'txtContingent').text
            print(txtContingent)
        except:
            print("Couldn't find players contingent.")

        try:
            # athlete/coach
            txtType = driver.find_element(By.ID, 'txtParticipantTypeName').text
            print(txtType)
        except:
            print("Couldn't find player type.")

        try:
            txtSport = driver.find_element(By.ID, 'txtSportName').text
            print(txtSport)
        except:
            print("Couldn't find players sport.")

        try:
            txtAge = driver.find_element(By.ID, 'txtAge').text
            print(txtAge)
        except:
            print("Couldn't find players age.")

        try:
            txtHeight = driver.find_element(By.ID, 'txtHeight').text
            print(txtHeight)
        except:
            print("Couldn't find players height.")

        try:
            txtWeight = driver.find_element(By.ID, 'txtWeight').text
            print(txtWeight)
        except:
            print("Couldn't find players height.")

        try:
            # club or team affiliation
            txtClubTeam = driver.find_element(By.ID, 'txtSchool').text
            print(txtClubTeam)
        except:
            print("Couldn't find players club name.")

        try:
            # coaches name
            txtCoach = driver.find_element(By.ID, 'txtCoach').text
            print(txtCoach)
        except:
            print("Couldn't find players coach.")

        try:
            # forward/ext in hockey
            txtTeamPosition = driver.find_element(By.ID, 'txtTeamPosition').text
            print(txtTeamPosition)
        except:
            print("Couldn't find team position")

        try:
            # idk, 'Abbysoyko_', name they used elsewhere?
            txtPrevSameGames = driver.find_element(By.ID, 'txtPrevSameGames').text
            print(txtPrevSameGames)
        except:
            print("Couldn't find previous same games")

        try:
            # same as above, 'abbysoyko_10'
            txtPrevGames = driver.find_element(By.ID, 'txtPrevGames').text
            print(txtPrevGames)
        except:
            print("Couldn't find previous games")

        try:
            txtGoals = driver.find_element(By.ID, 'txtGamesGoal').text
            print(txtGoals)
        except:
            print("Couldn't find athlete goals.")

        try:
            txtPersonalBest = driver.find_element(By.ID, 'txtBestResult').text
            print(txtPersonalBest)
        except:
            print("Couldn't find athlete personal best")

        try:
            txtAwards = driver.find_element(By.ID, 'txtAwards').text
            print(txtAwards)
        except:
            print("Couldn't find awards")

        try:
            txtRoleModel = driver.find_element(By.ID, 'txtRoleModel').text
            print(txtRoleModel)
        except:
            print("Couldn't find role model")

        try:
            txtMediaInfo = driver.find_element(By.ID, 'txtMediaInfo').text
            print(txtMediaInfo)
        except:
            print("Couldn't find media info")

        try:
            # all elements at the top of an individual event, descending as
            # event name, player team, player number, placement
            resultTable = driver.find_elements(By.CLASS_NAME, "ResultEventHeaderContainer")
            for header in resultTable:
                headerItem = header.find_elements(By.CSS_SELECTOR, "p")
                index = 0
                placement = ""
                event = ""
                for item in headerItem:
                    if index == 0:
                        event = item.text
                    placement = item.text
                    index += 1
                positionSplit = placement.split("position: ")
                positionString = positionSplit[1]
                txtAthletePlacing = txtName + " got " + positionString + " in " + event

                # appending to arrays our values we've scraped
                athleteEvents.append(event)
                athletePlacings.append(txtAthletePlacing)
                print(txtAthletePlacing)
        except:
            print("Couldn't find events.")

        try:
            # will be harder, [ year / competition name / placing ]
            accomplishmentTable = driver.find_elements(By.CLASS_NAME, 'Gems_RwdContentContainer')
        except:
            print("Couldn't find accomplishments.")

    except NoSuchElementException:
        print("Error.")

    finally:

        athleteGoldsCount = countMedals(athletePlacings, "gold")
        athleteGoldsCount = athleteGoldsCount + countMedals(athletePlacings, "Gold")

        athleteSilversCount = countMedals(athletePlacings, "silver")
        athleteSilversCount = athleteSilversCount + countMedals(athletePlacings, "Silver")

        athleteBronzesCount = countMedals(athletePlacings, "bronze")
        athleteBronzesCount = athleteBronzesCount + countMedals(athletePlacings, "Bronze")

        print("I counted bronze: " + str(athleteBronzesCount))
        athletePlacingsCount = athleteGoldsCount + athleteSilversCount + athleteBronzesCount

        athleteDict = {
            dictName: txtName,
            dictContingent: txtContingent,
            dictType: txtType,
            dictSport: txtSport,
            dictAge: txtAge,
            dictHeight: txtHeight,
            dictWeight: txtWeight,
            dictClubTeam: txtClubTeam,
            dictCoach: txtCoach,
            dictTeamPosition: txtTeamPosition,
            dictPrevSameGames: txtPrevSameGames,
            dictPrevGames: txtPrevGames,
            dictGoals: txtGoals,
            dictPersonalBest: txtPersonalBest,
            dictAwards: txtAwards,
            dictRoleModel: txtRoleModel,
            dictMediaInfo: txtMediaInfo,
            dictEvents: athleteConcatEvents,
            dictGolds: athleteGoldsCount,
            dictSilvers: athleteSilversCount,
            dictBronzes: athleteBronzesCount,
            dictPlacings: athletePlacingsCount
        }
        return athleteDict
