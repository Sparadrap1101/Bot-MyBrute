import os
import time
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def ProceedAccounts(startAccount, nbreOfAccounts, accountsArray, sizeArray):
    PASSWORD = os.getenv('PASSWORD')
    options = Options()
    # prefs = {"profile.managed_default_content_settings.images": 2}
    # options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-javascript")

    driver = webdriver.Chrome(options=options)
    driver.set_window_position(sizeArray[0], sizeArray[1])
    driver.set_window_size(sizeArray[2], sizeArray[3])

    for i in range(nbreOfAccounts):
        bruteNames = accountsArray[i + startAccount].split(" ")
        print("\nAccount {}: Brute names = {}".format(i + startAccount, bruteNames))
        print("\n----------")

        try:
            driver.get("https://eternaltwin.org/login")
            time.sleep(1)
            loginForm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"ng-pristine")))
            username = WebDriverWait(loginForm, 10).until(EC.presence_of_element_located((By.NAME, "login")))
            username.send_keys(bruteNames[0])
            password = WebDriverWait(loginForm, 10).until(EC.presence_of_element_located((By.NAME, "password")))
            password.send_keys(PASSWORD)
            button = WebDriverWait(loginForm, 10).until(EC.presence_of_element_located((By.NAME, "sign_in")))
            button.click()
            del loginForm
            del username
            del password
            del button
        except:
            print("Account {}: LOGIN ACCOUNT FAILED".format(i + startAccount))
        
        time.sleep(1)

        driver.get("https://brute.eternaltwin.org/")
        
    driver.quit()
    print("\n--- END OF THE PROCESS ---")

if __name__ == "__main__":

    startTime = time.time()

    load_dotenv()
    BASIC_ACCOUNTS = os.getenv('BASIC_ACCOUNTS')
    BEST_ACCOUNTS = os.getenv('BEST_ACCOUNTS')

    basicAccountsArray = BASIC_ACCOUNTS.split(", ")
    bestAccountsArray = BEST_ACCOUNTS.split(", ")

    makeBests = input("Do you want to level up your best brutes ? (y/n) > ")
    if makeBests == "y":
        accountsArray = basicAccountsArray + bestAccountsArray
    else:
        accountsArray = basicAccountsArray

    foundIndex = False
    while foundIndex == False:
        startAcc = int(input("Please enter the index of the account you want to start by (e.g. 0) > "))

        if startAcc >= 0 and startAcc < len(accountsArray):
            foundIndex = True

    ProceedAccounts(startAcc, len(accountsArray) - startAcc, accountsArray, [0, 0, 850, 850])
    
    time.sleep(1)

    executionTime = time.time() - startTime
    print("\n--- All accounts has been processed in {} seconds. ---".format(round(executionTime, 2)))
