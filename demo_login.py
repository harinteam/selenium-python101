from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

service = ChromeService(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get("https://demoqa.com/login")
driver.find_element(By.ID, "userName").send_keys("umarAlfatih")

driver.find_element_by_id("password").send_keys("asDF12#$")
driver.find_element_by_id("login").click()
