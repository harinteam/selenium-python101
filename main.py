"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
"""

from selenium import webdriver

PATH = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get("https://demoqa.com/register")