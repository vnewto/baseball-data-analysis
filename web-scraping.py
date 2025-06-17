# need to put the whole try block in a loop so that it adds one year each time it does a get request, and does a sleep in the middle. 
# how many years is reasonable to do?
# how to deal with the fact that some columns have multiple names or teams per category?

# Dashboard:
# sort by year (line graph) for each statistic
# sort by team for each statistic (bar graph)
# top 10 all-time best players or teams for each statistic (bar graph)

#list of stats I want to pull: stats_list = ['Batting Average', 'Home Runs', 'RBI', 'Stolen Bases', 'Total Bases']
 

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

#start at year 2020
year = 2000
get_link = f"https://www.baseball-almanac.com/yearly/yr{year}a.shtml"
#loop through years using year+=1 until 2024 (make sure to include 2024)

try:
    #connect to the webpage
    driver.get(get_link) 

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

        #declare variables to be used inside loop
        # stat_name
        # year_text
        # player_name
        # team
        # number

        for tr in table_items:

            print(f"THIS IS TR {count}")
            #find the tds inside each tr
            tds = tr.find_elements(By.TAG_NAME, 'td')
            if len(tds) > 0:

                #loop through the tds
                for td in tds:

                    #check the class name
                    td_class = td.get_attribute('class')
                    print(f"this is a td with class of {td_class}")

                    #if class is header, print the year, then skip to the next td
                    if td_class == 'header':
                        h2 = td.find_element(By.TAG_NAME, 'h2')
                        year_text = h2.text.strip()
                        print(f"This td contains an h2 with the title of '{year_text}'")
                        continue

                    elif td_class.__contains__('datacolBlue'):
                        #check for a tag
                        a_tag = td.find_element(By.TAG_NAME, 'a')
                        #check title attribute
                        a_title = a_tag.get_attribute('title')
                        #if title contains "YEAR BY YEAR LEADER", print title text and make that name of stat
                        if "YEAR BY YEAR LEADERS FOR" in a_title:
                            stat_name = a_tag.text.strip()
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
                                    player_name = a.text
                                    print(f"Player name: {player_name}")
                        #if no a tag
                        elif len(a_tags) == 0:
                            #check if team name
                            td_text = td.text.strip()
                            if td_text.lower() in teams_list:
                                team = td_text
                                print(f'Team: {team}')
                            #if not team name, then it's the number
                            else:
                                number = td_text
                                print(f"number: {number}")

            
            count += 1
 
            #if all are true, create dataframes
            #put headers on dataframes
            # home_runs = pd.DataFrame()
            # stolen_bases = pd.DataFrame()
            # rbi = pd.DataFrame()
            # bat_avg = pd.DataFrame()
            # total_bases = pd.DataFrame()


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



