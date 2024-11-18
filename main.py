from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time


load_dotenv()

login_page = "https://login.live.com/login.srf?wa=wsignin1.0&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f&aadredir=1"
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

# Add a prompt to keep the browser open
input("Press Enter to close the browser...")