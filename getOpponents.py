import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

startTime = time.time()

load_dotenv()
PASSWORD = os.getenv('PASSWORD')

driver = webdriver.Chrome()
driver.set_window_position(0, 0)
driver.set_window_size(1000, 850)

bruteNames = ["", "", "", "", "", ""]

foundAccount = False
while foundAccount == False:
    accountName = input("Please enter the account name you want > ")

    driver.get("https://eternaltwin.org/login")
    loginForm = driver.find_element(By.CLASS_NAME,"ng-pristine")
    username = loginForm.find_element(By.NAME, "login")
    username.send_keys(accountName)
    password = loginForm.find_element(By.NAME, "password")
    password.send_keys(PASSWORD)
    button = loginForm.find_element(By.NAME, "sign_in")
    button.click()

driver.quit()

executionTime = time.time() - startTime
print("\n--- The execution has last for {} seconds. ---".format(round(executionTime, 2)))
