import os
import time
import random
import threading
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def ProceedAccounts(startAccount):
    driver = webdriver.Chrome()
    driver.set_window_position(0, 0)
    driver.set_window_size(1040, 850)

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

        driver.get("https://brute.eternaltwin.org/")
        loginButton = driver.find_element(By.CLASS_NAME,"MuiButtonBase-root")
        loginButton.click()

        time.sleep(3)

        for j in range(3):
            print("\n{} is working...".format(bruteNames[j + 1]))

            driver.get("https://brute.eternaltwin.org/{}/cell".format(bruteNames[j + 1]))

            time.sleep(3)

            hasFightsLeft = True
