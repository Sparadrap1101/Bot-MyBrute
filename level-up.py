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
        loginButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"MuiButtonBase-root")))
        loginButton.click()
        del loginButton

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"css-17tdeih")))

        for j in range(len(bruteNames) - 1):
            driver.get("https://brute.eternaltwin.org/{}/cell".format(bruteNames[j + 1]))

            waitChoice = False
            try:
                time.sleep(1)
                
                levelUp = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME,"css-1i5638y")))
                levelUp.click()
                del levelUp
                print("\n{} NEEDS TO LEVEL UP:".format(bruteNames[j + 1]))

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"css-rqbvn6")))

                time.sleep(1)

                choices = driver.find_elements(By.CLASS_NAME, "css-12z2g5x")
                lastChoice = 0
                try:
                    choice1 = choices[0].text
                    choice2 = choices[1].text
                except:
                    parentDiv = driver.find_elements(By.CLASS_NAME, "css-foqdw6")
                    try:
                        oldChoices = parentDiv[0].find_elements(By.CLASS_NAME, "css-ewpxee")
                        choice1 = oldChoices[0].text
                        choice2 = choices[0].text
                        lastChoice = 1
                    except:
                        oldChoices = parentDiv[1].find_elements(By.CLASS_NAME, "css-ewpxee")
                        choice2 = oldChoices[0].text
                        choice1 = choices[0].text
                        lastChoice = 2

                choice2 = choice2.replace('en\n', '')
                if choice1[:13] == "Nouvelle arme":
                    arrayChoice = choice1.split('\n')
                    choice1 = arrayChoice[1]
                elif choice1[:19] == "Nouvelle compétence":
                    arrayChoice = choice1.split('\n')
                    choice1 = arrayChoice[1]
                elif choice1[:16] == "Nouveau familier":
                    arrayChoice = choice1.split('\n')
                    choice1 = arrayChoice[1]
                elif choice1[0] == "+":
                    choice1 = choice1.replace('en\n', '')

                print("--> 0: {}\n--> 1: {}".format(choice1, choice2))
                if lastChoice == 1:
                    print("\033[4m" + "\nLast destiny choice:" + "\033[0m" + " {}".format(choice1))
                elif lastChoice == 2:
                    print("\033[4m" + "\nLast destiny choice:" + "\033[0m" + " {}".format(choice2))

                driver.get("https://brute.eternaltwin.org/{}/cell".format(bruteNames[j + 1]))
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"css-1n2tkhe")))
                driver.execute_script("window.scrollTo(0, 250)")
                waitChoice = True
            except:
                try:
                    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME,"css-v3tyeg")))
                    print("\nAccount {}: {} - WINS A TOURNAMENT! HE CAN RANK UP!".format(i + startAccount, bruteNames[j + 1]))
                    print("\n{} don't need to level up.".format(bruteNames[j + 1]))
                except:
                    print("\n{} don't need to level up.".format(bruteNames[j + 1]))

            while waitChoice:
                userChoice = input("\nWhich skill do you want for this new level ? (0: Left, 1: Right, exit: Next Brute) > ")
                if userChoice == "0":
                    print("\033[1m" + "\n- You chose {}!".format(choice1) + "\033[0m")
                    driver.get("https://brute.eternaltwin.org/{}/level-up".format(bruteNames[j + 1]))

                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"css-rqbvn6")))
                    choices = driver.find_elements(By.CLASS_NAME, "css-rqbvn6")
                    choices[0].click()
                    waitChoice = False

                    time.sleep(1)

                elif userChoice == "1":
                    print("\033[1m" + "\n- You chose {}!".format(choice2) + "\033[0m")
                    driver.get("https://brute.eternaltwin.org/{}/level-up".format(bruteNames[j + 1]))

                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"css-1wi9ne9")))
                    choices = driver.find_elements(By.CLASS_NAME, "css-1wi9ne9")
                    choices[1].click()
                    waitChoice = False

                    time.sleep(1)

                elif userChoice == "exit":
                    print("Exiting, go to the next brute...")
                    waitChoice = False
                else:
                    print("Wrong answer, please try again.")

            print("\n----------")

        time.sleep(1)

        accountButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"css-17tdeih")))
        action = ActionChains(driver)
        action.move_to_element(accountButton).perform()
        del accountButton
        del action

        time.sleep(1)

        logout = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"Compte-action-0")))
        logoutButton = WebDriverWait(logout, 10).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        logoutButton.click()
        del logout
        del logoutButton

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
