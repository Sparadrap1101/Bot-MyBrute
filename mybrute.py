import os
import time
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

startTime = time.time()

load_dotenv()
PASSWORD = os.getenv('PASSWORD')
ACCOUNTS = os.getenv('ACCOUNTS')

accountsArray = ACCOUNTS.split(", ")

foundIndex = False
while foundIndex == False:
    startAccount = int(input("Please enter the index of the account you want to start by (e.g. 0) > "))

    if startAccount >= 0 and startAccount < len(accountsArray):
        foundIndex = True

driver = webdriver.Chrome()

for i in range(len(accountsArray) - startAccount):
    bruteNames = accountsArray[i + startAccount].split(" ")
    print("\nAccount {}: Brute names = {}".format(i + startAccount, bruteNames))

    driver.get("https://eternaltwin.org/login")
    loginForm = driver.find_element(By.CLASS_NAME,"ng-pristine")
    username = loginForm.find_element(By.NAME, "login")
    username.send_keys(bruteNames[0])
    password = loginForm.find_element(By.NAME, "password")
    password.send_keys(PASSWORD)
    button = loginForm.find_element(By.NAME, "sign_in")
    button.click()

    time.sleep(1)

driver.quit()

executionTime = time.time() - startTime
print("\n--- All accounts has been processed in {} seconds. ---".format(round(executionTime, 2)))
