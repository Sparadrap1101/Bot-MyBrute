import os
import time
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

load_dotenv()
PASSWORD = os.getenv('PASSWORD')
ACCOUNTS = os.getenv('ACCOUNTS')

accountsArray = ACCOUNTS.split(", ")


driver = webdriver.Chrome()

driver.quit()
