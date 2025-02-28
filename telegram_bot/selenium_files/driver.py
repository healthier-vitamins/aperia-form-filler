from selenium import webdriver
from selenium_files.config import FORM_URL

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(FORM_URL)
