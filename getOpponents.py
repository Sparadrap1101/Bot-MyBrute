import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

startTime = time.time()

load_dotenv()
PASSWORD = os.getenv('PASSWORD')

executionTime = time.time() - startTime
print("\n--- The execution has last for {} seconds. ---".format(round(executionTime, 2)))
