import allure
import openpyxl
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, NoSuchWindowException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.ie.options import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pytest
import json
import time
import datetime
import re
import os

########### VARIABLES ###########
navegador = u'Edge'

path = "your_path"

url = "https://www.bestbuy.com/"

######## XPATHS ########
country = "//img[contains(@alt,'Estados Unidos')]"

searchBar = "//input[contains(@id,'gh-search-input')]"

closeBox = "//*[@id='widgets-view-email-modal-mount']/div/div/div[1]/div/div/div/div/button"

searchButton = "//button[contains(@class,'header-search-button')]"

buyButton = str("btn btn-disabled btn-sm btn-block add-to-cart-button")
######### TEST ###########


####### open browser, get url and select country #######
driver = webdriver.Edge(path)

driver.maximize_window()

driver.implicitly_wait(15)

driver.get(url)

driver.find_element_by_xpath(country).click()

time.sleep(10)

############# Javascript c;lick to close a pop-up box ###############
localizador = driver.find_element(By.XPATH, closeBox)
driver.execute_script("arguments[0].click();", localizador)
print(u"Se hizo click en: " + str(localizador))

time.sleep(3)

############### find search bar and type what you want, in this case, "rtx 3080" ##############
driver.find_element_by_xpath(searchBar).send_keys("rtx 3080")

driver.find_element_by_xpath(searchButton).click()

########### try to find the element 'sold out' to check if it's available and take a screenshot ################
try:
    soldOut = "(//strong[contains(.,'Sold Out')])"
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, soldOut))
    )    
    findElement = driver.find_elements_by_xpath(soldOut)
    
    if findElement:
        print("Element 'sold out' located")
        driver.save_screenshot("notAvailable.png")
        
    else:
        driver.save_screenshot("available.png")
        print("Element 'sold out' not found. Must be available")

############## close the browser ##################
finally:
    time.sleep(5)
    driver.quit()
