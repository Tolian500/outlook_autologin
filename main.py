import os
from dotenv import load_dotenv, dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
# from tags import tags
import time
import os
import time
import json
from datetime import datetime

load_dotenv()

login_page = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=165&ct=1731492304&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26culture%3dpl-pl%26country%3dpl%26RpsCsrfState%3d8f6f176e-e6b9-4cf8-349a-42e14882c4f3&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c"
email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--lang=en")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")

# Mimic Windows by setting the User-Agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")

# Force Chrome to report the platform as Windows
chrome_options.add_argument("--platform=WIN")

driver = webdriver.Chrome(options=chrome_options)
print("Driver initialised as Windows user")
driver.get(login_page)
time.sleep(2)

email_input = driver.find_element(By.NAME, 'loginfmt')
email_input.send_keys(email, Keys.ENTER)
time.sleep(2)
pass_input = driver.find_element(By.NAME, 'passwd')
pass_input.send_keys(password, Keys.ENTER)
