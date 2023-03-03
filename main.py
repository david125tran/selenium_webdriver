from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://orteil.dashnet.org/cookieclicker/"

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

#Select English Button
time.sleep(4) #let webpage load 1st
english_button = driver.find_element(By.ID, "langSelect-EN")
english_button.click()
time.sleep(4) #let webpage load 1st

timeout = time.time() + 5
five_min = time.time() + 25000
cookie = driver.find_element(By.ID, "bigCookie")

#Loop the clicking and keep purchasing the most expensive item
while True:

    #Make a click
    cookie.click()

    #If it has been longer than 5 seconds:
    if time.time() > timeout:

        #Reset the timer
        timeout = time.time() + 5

        #Make a purchase
        for num in range (30, -1, -1):
            id = f"product{str(num)}"
            try:
                purchase_button = driver.find_element(By.ID, id)
                purchase_button.click()

                #If something got purchased, exit the purchase for loop
                if purchase_button.get_attribute("automationTrack") != None:
                    break
            except:
                pass

    #Check to see if it has been 5 mins
    if time.time() > five_min:
        break

result = driver.find_element(By.CSS_SELECTOR, "#cookiesPerSecond")
print(f"You had cookies {result.text}")