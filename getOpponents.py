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
driver.set_window_size(1000, 800)

bruteNames = ["", "", "", "", "", ""]

foundAccount = False
while foundAccount == False:
    accountName = input("Please enter the account name you want > ")

    driver.get("https://eternaltwin.org/login")
    time.sleep(1)
    loginForm = driver.find_element(By.CLASS_NAME,"ng-pristine")
    username = loginForm.find_element(By.NAME, "login")
    username.send_keys(accountName)
    password = loginForm.find_element(By.NAME, "password")
    password.send_keys(PASSWORD)
    button = loginForm.find_element(By.NAME, "sign_in")
    button.click()

    time.sleep(2)

    verify = driver.find_element(By.CLASS_NAME, "button").text

    driver.get("https://brute.eternaltwin.org/")
    loginButton = driver.find_element(By.CLASS_NAME,"MuiButtonBase-root")
    loginButton.click()

    if verify == accountName:
        foundAccount = True
    else:
        print("Wrong name account, please try again.")

bruteName = input("Please enter the Brute name you want > ")

continueGetOpponents = True
while continueGetOpponents == True:
    try:
        driver.get("https://brute.eternaltwin.org/{}/arena".format(bruteName))

        time.sleep(1.5)

        opponents = driver.find_elements(By.CLASS_NAME, "css-rpybyc")

        for i in range(6):
            bruteNames[i] = opponents[i].find_element(By.TAG_NAME, "p").text

        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])

        for i in range(6):
            driver.get("https://brute.eternaltwin.org/{}/cell".format(bruteNames[i]))
            time.sleep(1)

        input("\nPress enter to continue.")

        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        wantToContinue = input("\nDo you want to get your opponents for the next fight ? (y/n) > ")

        if wantToContinue == "n":
            continueGetOpponents = False
    except:
        print("Wrong Brute name or no fight left, please try again.")

        bruteName = input("Please enter the Brute name you want > ")

driver.quit()

executionTime = time.time() - startTime
print("\n--- The execution has last for {} seconds. ---".format(round(executionTime, 2)))
