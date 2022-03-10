"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
"""

from selenium import webdriver
import time

PATH = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get("https://demoqa.com/register")
driver.find_element_by_id("firstname").send_keys("Muhammad Umar")
driver.find_element_by_id("lastname").send_keys("Al-fatih")
driver.find_element_by_id("userName").send_keys("umaralfatih")
driver.find_element_by_id("password").send_keys("asDF12#$")
time.sleep(20)
driver.find_element_by_id("register").click()



