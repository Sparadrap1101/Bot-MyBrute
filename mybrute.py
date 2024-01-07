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

    driver.get("https://brute.eternaltwin.org/")
    loginButton = driver.find_element(By.CLASS_NAME,"MuiButtonBase-root")
    loginButton.click()

    time.sleep(3)

    for j in range(3):
        print("\n{} is working...".format(bruteNames[j + 1]))

        driver.get("https://brute.eternaltwin.org/{}/cell".format(bruteNames[j + 1]))

        time.sleep(2)

        nextTournament = driver.find_element(By.CLASS_NAME, "css-1rb3pee")
        if not nextTournament.text == "Brute inscrite.":
            findTournament = driver.find_element(By.CLASS_NAME, "css-1l4w6pd")
            tournament = findTournament.find_element(By.TAG_NAME, "a")
            tournament.click()
            
            time.sleep(2)

            try:
                tournamentSeen = driver.find_element(By.CLASS_NAME, "css-9w9xg7")
                tournamentSeen.click()

                time.sleep(2)
            except:
                print("TOURNAMENT ALREADY SEEN")

            driver.get("https://brute.eternaltwin.org/{}/cell".format(bruteNames[j + 1]))

            time.sleep(2)

            try:
                tournamentRegistration = driver.find_element(By.CLASS_NAME, "css-yb6hwx")
                tournamentRegistration.click()

                time.sleep(1)
            except:
                print("TOURNAMENT REGISTRATION FAILED")

        else: 
            print("Already registered in the tournament.")

    accountButton = driver.find_element(By.CLASS_NAME,"MuiFab-primary")
    action = ActionChains(driver)
    action.move_to_element(accountButton).perform()

    time.sleep(1)

    deconnexion = driver.find_element(By.ID,"Compte-action-0")
    deconnexionButton = deconnexion.find_element(By.TAG_NAME, "button")
    deconnexionButton.click()

    time.sleep(2)

driver.quit()

executionTime = time.time() - startTime
print("\n--- All accounts has been processed in {} seconds. ---".format(round(executionTime, 2)))
