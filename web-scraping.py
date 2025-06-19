# need to put the whole try block in a loop so that it adds one year each time it does a get request, and does a sleep in the middle. 
# how many years is reasonable to do?
# how to deal with the fact that some columns have multiple names or teams per category?

# Dashboard:
# sort by year (line graph) for each statistic
# sort by team for each statistic (bar graph)
# top 10 all-time best players or teams for each statistic (bar graph)
 

#Initialize selenium and the driver. import necessary items
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))



#declare empty variables to be used inside loop
stat_name = 'None'
year_text = 'None'
player_name = 'None'
team = 'None'
number = 'None'

#declare empty list for each stat
#list of stats I want to pull: stats_list = ['Batting Average', 'Home Runs', 'RBI', 'Stolen Bases', 'Total Bases']
bat_avg = []
home_runs = []
rbi = []
stolen_bases = []
tot_bases = []

for year in range(2000, 2025):
    try:
        #loop through years using year+=1 until 2024 (make sure to include 2024)
        get_link = f"https://www.baseball-almanac.com/yearly/yr{year}a.shtml"

        #connect to the webpage
        driver.get(get_link) 

        #Wait until div with id "wrapper" loads
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#wrapper')))
        print(f'Located wrapper, scraping {year} page now...')

        #find div with id "wrapper"
        wrapper = driver.find_element(By.CSS_SELECTOR, 'div[id="wrapper"]')

        #if wrapper
        if wrapper:
            #look for the first class "container" -> first class "ba-table" -> first element table with class "body" -> element tbody
            table_items = driver.find_elements(By.XPATH, './/*[@id="wrapper"]/div[2]/div[3]/table/tbody/tr')

            #turn column headers into a list
            column_headers_list = []
            column_headers = table_header = driver.find_elements(By.XPATH, './/*[@id="wrapper"]/div[2]/div[3]/table/tbody/tr[2]/td')
            for item in column_headers:
                column_headers_list.append(item.text)
            column_headers_list = column_headers_list[1:4]
            print('column_headers_list: ', column_headers_list)
            
            #make teams list
            teams_list = ['anaheim angels', 'arizona diamondbacks', 'atlanta braves', 'baltimore orioles', 'boston red sox', 'chicago cubs', 'chicago white sox', 'cleveland guardians', 'cleveland indians', 'cincinnati reds', 'colorado rockies', 'detroit tigers', 'florida marlins', 'houston astros', 'kansas city royals', 'los angeles dodgers', 'los angeles angels', 'miami marlins', 'milwaukee brewers', 'minnesota twins', 'new york yankees', 'oakland athletics', 'pittsburgh pirates', 'philadelphia phillies', 'sacramento athletics', 'san diego padres', 'san francisco giants','seattle mariners', 'st. louis cardinals', 'tampa bay rays', 'tampa bay devil rays', 'texas rangers', 'toronto blue jays', 'various american', 'washington nationals', 'oakland athletics', 'anaheim', 'baltimore', 'boston', 'chicago', 'cleveland', 'detroit', 'houston', 'kansas city', 'los angeles', 'minnesota', 'new york', 'oakland', 'tampa bay', 'tampa bay rays', 'texas', 'toronto', 'seattle']

            #loop through trs
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
                count += 1
                #list of stats to pull: stats_list = ['Batting Average', 'Home Runs', 'RBI', 'Stolen Bases', 'Total Bases']
                # bat_avg = {}
                # home_runs = {}
                # rbi = {}
                # stolen_bases = {}
                # tot_bases = {}

            #append to the correct dictionary based on stat name
                if stat_name.lower() == 'batting average':
                    bat_avg.append({'stat': stat_name, 'year': year_text, 'player': player_name, 'team': team, 'number': number})
                elif stat_name.lower() == 'home runs':
                    home_runs.append({'stat': stat_name, 'year': year_text, 'player': player_name, 'team': team, 'number': number})
                elif stat_name.lower() == 'rbi':
                    rbi.append({'stat': stat_name, 'year': year_text, 'player': player_name, 'team': team, 'number': number})
                elif stat_name.lower() == 'stolen bases':
                    stolen_bases.append({'stat': stat_name, 'year': year_text, 'player': player_name, 'team': team, 'number': number})
                elif stat_name.lower() == 'total bases':
                    tot_bases.append({'stat': stat_name, 'year': year_text, 'player': player_name, 'team': team, 'number': number})
        
        #WAIT BEFORE NEXT ROUND
        print(f'Finished scraping {year} page, pausing for 10 seconds.')
        sleep(10)

        print('bat_avg: ', bat_avg)
        print('\n home_runs: ', home_runs)
        print('\n rbi: ', rbi)
        print('\n stolen_bases: ', stolen_bases)
        print('\n tot_bases: ', tot_bases)



            #if all are true, create dataframes
            #put headers on dataframes
            # home_runs_df = pd.DataFrame.from_dict(home_runs))
            # stolen_bases_df = pd.DataFrame(stolen_bases)
            # rbi_df = pd.DataFrame(rbi)
            # bat_avg_df = pd.DataFrame(bat_avg)
            # total_bases_df = pd.DataFrame(tot_bases)


#print error message if it doesn't work
    except Exception as e: 
        print("couldn't get the web page")
        print(f"Exception: {type(e).__name__} {e}")

    #quit driver when done
    finally:
        driver.quit()


# #write to csv file
# home_runs.to_csv("home_runs.csv", sep=',', header=True, index=True)
# stolen_bases.to_csv("stolen_bases.csv", sep=',', header=True, index=True)
# rbi.to_csv("rbi.csv", sep=',', header=True, index=True)
# bat_avg.to_csv("bat_avg.csv", sep=',', header=True, index=True)
# total_bases.to_csv("total_bases.csv", sep=',', header=True, index=True)



