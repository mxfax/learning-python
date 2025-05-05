from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import getpass

job_title = input("Please input your desired job title, or skills: ")
location = input("Please input the desired location where you want to work: ")

USERNAME = input("Please input your LinkedIn username: ")
PASS = getpass.getpass("Please input your LinkedIn password: ")

options = Options()
options.set_preference('intl.accept_languages', 'en-GB')

#USERNAME = ""
#PASS = ""

driver = webdriver.Firefox(options=options)
driver.get("https://www.linkedin.com/login")
time.sleep(5) 
username = driver.find_element(By.NAME, "session_key")
username.send_keys(USERNAME)
password = driver.find_element(By.NAME, "session_password")
password.send_keys(PASS)
time.sleep(2)

button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
button.click()
time.sleep(5)
jobs = driver.find_element(By.LINK_TEXT, "Jobs")
jobs.click()
time.sleep(5)

jobs_input = driver.find_element(By.XPATH, "//input[@aria-label='Search by title, skill, or company']")
jobs_input.send_keys(job_title)
time.sleep(1)
jobs_location = driver.find_element(By.XPATH, "//input[@aria-label='City, state, or zip code']")
jobs_location.clear()
time.sleep(1)
jobs_location.send_keys(location)
time.sleep(1)
jobs_location.send_keys(Keys.ENTER)
