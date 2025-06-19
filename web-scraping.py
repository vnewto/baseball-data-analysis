# need to put the whole try block in a loop so that it adds one year each time it does a get request, and does a sleep in the middle. 
# how many years is reasonable to do?
# how to deal with the fact that some columns have multiple names or teams per category?

# Dashboard:
# sort by year (line graph) for each statistic
# sort by team for each statistic (bar graph)
# top 10 all-time best players or teams for each statistic (bar graph)
 

#list of stats to pull: stats_list = ['Batting Average', 'Home Runs', 'RBI', 'Stolen Bases', 'Total Bases']


#Initialize selenium and the driver. import necessary items
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import pandas as pd

#add user agent
chrome_options = Options()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36')

#set up driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#declare empty variables to be used inside loop
stat_name = 'None'
year_text = 'None'
player_name = 'None'
team = 'None'
number = 'None'

#declare empty list to append each dictionary row
baseball_data = []

#loop through years using year+=1 until 2024 (make sure to include 2024)
for year in range(2000, 2025):
    try:
        get_link = f"https://www.baseball-almanac.com/yearly/yr{year}a.shtml"

        #connect to the webpage
        print('Opening webpage...')
        driver.get(get_link) 

        #Wait until div with id "wrapper" loads or up to 10 seconds, whichever happens first
        print('Waiting for page to load...')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#wrapper')))
        print(f'Located wrapper, scraping {driver.title} page now for year {year}...')

        #find div with id "wrapper"
        wrapper = driver.find_element(By.CSS_SELECTOR, 'div[id="wrapper"]')

        #if wrapper
        if wrapper:
            #look for the first class "container" -> first class "ba-table" -> first element table with class "body" -> element tbody
            table_items = driver.find_elements(By.XPATH, './/*[@id="wrapper"]/div[2]/div[3]/table/tbody/tr')
            
            #make teams list
            teams_list = ['anaheim angels', 'arizona diamondbacks', 'atlanta braves', 'baltimore orioles', 'boston red sox', 'chicago cubs', 'chicago white sox', 'cleveland guardians', 'cleveland indians', 'cincinnati reds', 'colorado rockies', 'detroit tigers', 'florida marlins', 'houston astros', 'kansas city royals', 'los angeles dodgers', 'los angeles angels', 'miami marlins', 'milwaukee brewers', 'minnesota twins', 'new york yankees', 'oakland athletics', 'pittsburgh pirates', 'philadelphia phillies', 'sacramento athletics', 'san diego padres', 'san francisco giants','seattle mariners', 'st. louis cardinals', 'tampa bay rays', 'tampa bay devil rays', 'texas rangers', 'toronto blue jays', 'various american', 'washington nationals', 'oakland athletics', 'anaheim', 'baltimore', 'boston', 'chicago', 'cleveland', 'detroit', 'houston', 'kansas city', 'los angeles', 'minnesota', 'new york', 'oakland', 'tampa bay', 'tampa bay rays', 'texas', 'toronto', 'seattle']

            #loop through trs
            print('Looking through table items now...')
            count = 1

            for tr in table_items:

                print(f"THIS IS TR {count}")
                #find the tds inside each tr
                tds = tr.find_elements(By.TAG_NAME, 'td')
                if len(tds) > 0:

                    #loop through the tds
                    for td in tds:

                        #check the class name
                        td_class = td.get_attribute('class')
                        # print(f"this is a td with class of {td_class}")

                        #if class is header, print the year, then skip to the next td
                        if td_class == 'header':
                            h2 = td.find_element(By.TAG_NAME, 'h2')
                            year_text = h2.text.strip() # define year_text
                            print(f"This td contains an h2 with the title of '{year_text}'")
                            continue

                        elif td_class.__contains__('datacolBlue'):
                            #check for a tag
                            a_tag = td.find_element(By.TAG_NAME, 'a')
                            #check title attribute
                            a_title = a_tag.get_attribute('title')
                            #if title contains "YEAR BY YEAR LEADER", print title text and make that name of stat
                            if "YEAR BY YEAR LEADER" in a_title:
                                stat_name = a_tag.text.strip() #define stat_name
                                print(f"stat_name: {stat_name}")
                        
                        elif td_class.__contains__('datacolBox'):
                            #check for a tags
                            a_tags = td.find_elements(By.TAG_NAME, 'a')
                            #if a tags found
                            if len(a_tags) > 0:
                                #loop through the a tags
                                for a in a_tags:
                                    #if href contains "/players/player" then a text = player
                                    a_href = a.get_attribute('href')
                                    if "/players/player" in a_href:
                                        player_name = a.text.strip() #define player_name
                                        print(f"Player name: {player_name}")
                                    elif "roster" in a_href:
                                        team = a.text.strip()
                                        print('team: ', team)
                                    else:
                                        print(f'<a> tag href contains the link {a_href}, does not fit specified conditions.')
                            #if no a tag
                            elif len(a_tags) == 0:
                                #check if team name
                                td_text = td.text.strip()
                                if td_text.lower() in teams_list:
                                    team = td_text #define team
                                    print(f'Team: {team}')
                                #if not team name, then it's the number
                                else:
                                    number = td_text.strip() #define number
                                    print(f"number: {number}")
                        else:
                            print(f'<td> tag found with class {td_class} - does not fit any specified category.')
                else: 
                    print("No <td> tags found in this <tr>.")
                
                count += 1

                #append to the list
                baseball_data.append({'stat': stat_name, 'year': year_text, 'player': player_name, 'team': team, 'number': number})

                #print length of list after scraping
                print(f'Scraped a total of {len(baseball_data)} rows.')

                #reset values to 'None' before restarting loop
                stat_name = 'None'
                player_name = 'None'
                team = 'None'
                number = 'None'
        
        #WAIT BEFORE NEXT ROUND
        print(f'Finished scraping {year} page, pausing for 10 seconds.')
        sleep(10)

        print('baseball_data: ', baseball_data)

        #create dataframe from dictionary
        baseball_data_df = pd.DataFrame.from_dict(baseball_data)


#print error message if it doesn't work
    except Exception as e: 
        print("couldn't get the webpage")
        print(f"Exception: {type(e).__name__} {e}")

    #quit driver when done
    finally:
        driver.quit()


# #write to csv file
baseball_data_df.to_csv("baseball_data.csv", sep=',', header=True, index=True)




