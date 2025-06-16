#Initialize selenium and the driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


try:
    #connect to the webpage
    driver.get("https://www.baseball-almanac.com/yearly/yr1901a.shtml") 

    #find div with id "wrapper"
    wrapper = driver.find_element(By.CSS_SELECTOR, 'section[id="wrapper"]')

    #if wrapper
    if wrapper:
        #look for the first class "container" -> first class "ba-table" -> first element table with class "body" -> element tbody

#print error message if it doesn't work
except Exception as e: 
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")

#quit driver when done
finally:
    driver.quit()
