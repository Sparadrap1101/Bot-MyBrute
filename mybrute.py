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

            try:
                driver.find_element(By.CLASS_NAME, "css-v3tyeg")
                hasFightsLeft = False

                print("{} WINS A TOURNAMENT! HE CAN RANK UP!".format(bruteNames[j + 1]))
            except:
                try:
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
                            driver.find_element(By.CLASS_NAME, "css-v3tyeg")
                            hasFightsLeft = False

                            print("{} WINS A TOURNAMENT! HE CAN RANK UP!".format(bruteNames[j + 1]))
                        except:
                            tournamentRegistration = driver.find_element(By.CLASS_NAME, "css-yb6hwx")
                            tournamentRegistration.click()

                            time.sleep(1)
                    else: 
                        print("Already registered in the tournament.")
                except:
                    print("TOURNAMENT REGISTRATION FAILED!")

            fightCounter = 0
            try:
                fightsWonBefore = int(driver.find_elements(By.CLASS_NAME, "css-a0dt3d")[1].text)
            except:
                fightsWonBefore = 0
                print("FIGHT COUNTER FAILED")

            while hasFightsLeft:
                try:
                    driver.find_element(By.CLASS_NAME, "css-1dbhieh")
                    print("{} NEEDS TO LEVEL UP!".format(bruteNames[j + 1]))
                    hasFightsLeft = False
                except:
                    try:
                        driver.find_element(By.CLASS_NAME, "css-vbasy3")

                        try:
                            driver.get("https://brute.eternaltwin.org/{}/arena".format(bruteNames[j + 1]))

                            time.sleep(1.5)

                            randomOpponent = random.randint(0, 5)
                            opponents = driver.find_elements(By.CLASS_NAME, "css-rpybyc")
                            opponents[randomOpponent].click()

                            time.sleep(1)

                            runFight = driver.find_element(By.CLASS_NAME, "css-1e0h3j1")
                            runFight.click()

                            time.sleep(2.5)

                            fightCounter += 1
                        except:
                            print("FIGHT FAILED")

                        driver.get("https://brute.eternaltwin.org/{}/cell".format(bruteNames[j + 1]))

                        time.sleep(1.5)
                    except:
                        hasFightsLeft = False
            
            if fightCounter == 0:
                print("{} can't fight anymore, go to the next Brute.".format(bruteNames[j + 1]))
            else:
                try:
                    fightsWonAfter = int(driver.find_elements(By.CLASS_NAME, "css-a0dt3d")[1].text)

                    wins = fightsWonAfter - fightsWonBefore

                    print("{} is done. He won {}/{} fights!".format(bruteNames[j + 1], wins, fightCounter))
                except:
                    print("FIGHT COUNTER FAILED")

        accountButton = driver.find_element(By.CLASS_NAME,"MuiFab-primary")
        action = ActionChains(driver)
        action.move_to_element(accountButton).perform()

        time.sleep(1)

        logout = driver.find_element(By.ID,"Compte-action-0")
        logoutButton = logout.find_element(By.TAG_NAME, "button")
        logoutButton.click()

        time.sleep(2)

    driver.quit()


if __name__ == "__main__":

    startTime = time.time()

    load_dotenv()
    PASSWORD = os.getenv('PASSWORD')
    BASIC_ACCOUNTS = os.getenv('BASIC_ACCOUNTS')
    BEST_ACCOUNTS = os.getenv('BEST_ACCOUNTS')

    basicAccountsArray = BASIC_ACCOUNTS.split(", ")
    bestAccountsArray = BEST_ACCOUNTS.split(", ")

    makeBests = input("Do you want to fight with your best brutes ? (y/n) > ")
    if makeBests == "y":
        accountsArray = basicAccountsArray + bestAccountsArray
    else:
        accountsArray = basicAccountsArray

    foundIndex = False
    while foundIndex == False:
        startAcc = int(input("Please enter the index of the account you want to start by (e.g. 0) > "))

        if startAcc >= 0 and startAcc < len(accountsArray):
            foundIndex = True
    
    ProceedAccounts(startAcc)

    #thread1 = threading.Thread(target=ProceedAccounts, args=(startAcc,))
    #thread2 = threading.Thread(target=ProceedAccounts, args=(1,))
    #thread3 = threading.Thread(target=ProceedAccounts, args=(2,))
    #thread4 = threading.Thread(target=ProceedAccounts, args=(3,))

    #thread1.start()
    #thread2.start()
    #thread3.start()
    #thread4.start()
    #print("Closed {}".format(thread1))
    #print("Closed {}".format(thread2))
    #print("Closed {}".format(thread3))
    #print("Closed {}".format(thread4))

    time.sleep(2)

    #thread1.join()
    #thread2.join()
    #thread3.join()
    #thread4.join()
    #print("Closed {}".format(thread1))

    executionTime = time.time() - startTime
    print("\n--- All accounts has been processed in {} seconds. ---".format(round(executionTime, 2)))
