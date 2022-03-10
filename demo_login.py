
from selenium import webdriver


PATH = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get("https://demoqa.com/login")
driver.find_element_by_id("userName").send_keys("umaralfatih")
driver.find_element_by_id("password").send_keys("asDF12#$")
driver.find_element_by_id("login").click()