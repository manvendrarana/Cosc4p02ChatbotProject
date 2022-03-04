from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

sport_page_url = "https://cg2022.gems.pro/Result/Sport_List.aspx?SiteMapTreeExpanded=b970b19b-cbed-45c9-9e45-5fee884be016&SetLanguage=en-CA"  # page that lists all sports and links to each sport's events
sport_page_table_id = "ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_tblSportmatrix"  # id of the table that lists all sports and links to each sport's events
event_page_table_id = "ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_tblSport"  # id of the table that links to all events for a specific sport
event_profile_page_round_class = "LM_ResultRoundName"  # class where round name can be found (e.g., Finals) on event profile page
event_profile_page_round_table_class = "LM_CollapsibleSectionShow"  # class of the table for each round on event profile page
heat_info_class = "LM_ResultGameName"  # parts on event page that gives heat information
sport_event_urls = []


# returns the name and links of a table's vertical axis and their corresponding link
# parameter: url      -> url of the site where the table is located
#            table_id -> id of table on page
# return: list[[name, url],  [name, url],  [name, url],  ....]
def get_name_and_url(url, table_id):
    driver.get(url)
    event_url = []

    try:

        table = driver.find_element_by_id(table_id)
        event_links_odd = table.find_elements_by_class_name("DataRowOdd")
        event_links_even = table.find_elements_by_class_name("DataRowEven")

        for i in range(len(event_links_odd) + len(event_links_even)):
            if (i + 1) % 2 == 0:
                tag = event_links_even.pop(0).find_element_by_class_name("DataCell").find_element_by_tag_name("a")
            else:
                tag = event_links_odd.pop(0).find_element_by_class_name("DataCell").find_element_by_tag_name("a")
            event_url.append([tag.text, tag.get_attribute("href")])

    except NoSuchElementException:
        if driver.find_element_by_id(
                "ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_Section_PRE_A_Section_PRE_A_SectionLabel") != None:
            event_url = [[driver.find_element_by_class_name("LM_PageTitle").get_attribute("innerHTML"), url]]
    return event_url


# takes a sports name and returns their corresponding id
def get_sport_id(sport_name):
    if sport_name == "Athletics":
        return 0
    elif sport_name == "Baseball":
        return 1
    elif sport_name == "Basketball":
        return 2
    elif sport_name == "Box Lacrosse":
        return 3
    elif sport_name == "Canoe Kayak":
        return 4
    elif sport_name == "Cycling":
        return 5
    elif sport_name == "Diving":
        return 6
    elif sport_name == "Golf":
        return 7
    elif sport_name == "Rowing":
        return 8
    elif sport_name == "Rugby Sevens":
        return 9
    elif sport_name == "Sailing":
        return 10
    elif sport_name == "Soccer":
        return 11
    elif sport_name == "Softball":
        return 12
    elif sport_name == "Swimming":
        return 13
    elif sport_name == "Tennis":
        return 14
    elif sport_name == "Triathlon":
        return 15
    elif sport_name == "Volleyball":
        return 16
    elif sport_name == "Wrestling":
        return 17


# finds the url and name of all events, the id of the sport they are related to, and gives them an event id
# parameter: None
# return: list[[sport id, event id, event name, event url],  [sport id, event id, event name, event url],  ....]
def get_all_basic_event_information():
    event_id = 0
    global sport_event_urls
    sport_event_urls = get_name_and_url(sport_page_url, sport_page_table_id)
    all_events = []
    for i in sport_event_urls:
        events = get_name_and_url(i[1], event_page_table_id)
        for j in events:
            all_events.append([get_sport_id(i[0]), event_id, j[0], j[1]])
            event_id = event_id + 1
    return all_events


def get_match_data_dataCell(dataCell1, dataCell2):
    if len(dataCell1) == 7:
        match = dataCell1.pop(0).text
        print(match)
        info = dataCell1.pop(0).text.split("<br>")
        team1_abbreviation = dataCell1.pop(0).text
        team1_sets_won = dataCell1.pop(0).text
        team1_set1_points = dataCell1.pop(0).text
        team1_set2_points = dataCell1.pop(0).text
        team1_set3_points = dataCell1.pop(0).text

        team2_abbreviation = dataCell2.pop(0).text
        team2_sets_won = dataCell2.pop(0).text
        team2_set1_points = dataCell2.pop(0).text
        team2_set2_points = dataCell2.pop(0).text
        team2_set3_points = dataCell2.pop(0).text
        try:
            temp = info[2].split("\n")
        except:
            print(str(info))

        data = [match, str(info[0]) + str(info[1]) + str(temp[0]), str(temp[1]), str(temp[2]), team1_abbreviation, team1_sets_won, team1_set1_points,
                team1_set2_points,
                team1_set3_points, team2_abbreviation, team2_sets_won, team2_set1_points, team2_set2_points,
                team2_set3_points]
    else:  # len(dataCell1) == 4
        match = dataCell1.pop(0).text
        info = dataCell1.pop(0).text.split(",")
        team1_abbreviation = dataCell1.pop(0).text
        team1_points = dataCell1.pop(0).text
        team2_abbreviation = dataCell2.pop(0).text
        team2_points = dataCell2.pop(0).text

        temp = info[2].split("\n")
        #print("info: " + str(info[0]) + " " + str(info[1]) + " " + str(temp[0]) + " " + temp[1] + " " + temp[2])

        data = [match, str(info[0]) + str(info[1]) + str(temp[0]), str(temp[1]), str(temp[2]), team1_abbreviation, team1_points, team2_abbreviation,
                team2_points]
    return data


# gets the specific information on an event
# parameter: event_info -> [sport id, event id, event name, event url]
def get_specific_event_information(event_info):
    driver.get(event_info[3])
    round_names = []
    rounds = driver.find_elements_by_class_name(event_profile_page_round_class)
    round_tables = driver.find_elements_by_class_name(event_profile_page_round_table_class)
    all_heat_info = driver.find_elements_by_class_name(heat_info_class)

    # get name of each round
    for r in rounds:
        round_names.append(r.text)

    count = 0
    for rt in round_tables:
        if all_heat_info != []:
            for r in range(int(len(rt.find_elements_by_class_name(heat_info_class)) / 4)):
                # [heat name, date, time, location]
                heat_info = [round_names[count]]
                for i in range(4):
                    if all_heat_info == []:
                        break
                    info = all_heat_info.pop(0).text
                    while not info:
                        if all_heat_info == []:
                            break
                        info = all_heat_info.pop(0).text
                    heat_info.append(info)
                if heat_info != [] and heat_info != ['']:
                    event_info.append(heat_info)
            count = count + 1
        else:
            event_links_odd = rt.find_elements_by_class_name("DataRowOdd")
            event_links_even = rt.find_elements_by_class_name("DataRowEven")

            for j in range(len(event_links_odd) + len(event_links_even)):
                if (j + 1) % 2 == 0:
                    if event_links_even != []:
                        test = event_links_even.pop(0).find_elements_by_class_name("DataCell")
                        if (len(test) == 4 or len(test) == 7) and (
                                test[0].text == "Match" or
                                test[0].text == "Game" or
                                test[0].text == "Tie" or
                                test[0].text == "Duel" or
                                test[0].text == "Bout"):

                            data = get_match_data_dataCell(test,
                                                           event_links_even.pop(0).find_elements_by_class_name(
                                                               "DataCell"))
                            event_info.append(data)
                else:
                    if event_links_odd != []:
                        test = event_links_odd.pop(0).find_elements_by_class_name("DataCell")
                        if (len(test) == 4 or len(test) == 7) and (
                                test[0].text == "Match" or
                                test[0].text == "Game" or
                                test[0].text == "Tie" or
                                test[0].text == "Duel" or
                                test[0].text == "Bout"):
                            data = get_match_data_dataCell(test,
                                                           event_links_odd.pop(0).find_elements_by_class_name(
                                                               "DataCell"))
                            event_info.append(data)
    return event_info


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    basic_event_info = get_all_basic_event_information()
    for i in basic_event_info:
        #[sport id, event id, event name, event url, [match name, heat name, date, time, location], results]
        print(get_specific_event_information(i))
    driver.close()
