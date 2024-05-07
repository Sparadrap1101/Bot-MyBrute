import os
import gc
import time
import random
import multiprocessing
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def ProceedAccounts(startAccount, nbreOfAccounts, accountsArray, sizeArray):
    PASSWORD = os.getenv('PASSWORD')
    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-javascript")

    driver = webdriver.Chrome(options=options)
    driver.set_window_position(sizeArray[0], sizeArray[1])
    driver.set_window_size(sizeArray[2], sizeArray[3])

    quitDriver = 0
    for i in range(nbreOfAccounts):
        quitDriver += 1
        bruteNames = accountsArray[i + startAccount].split(" ")
        print(color.YELLOW + "\nAccount {}: Brute names = ".format(i + startAccount) + color.BOLD + "{}".format(bruteNames) + color.END)

        try:
            driver.get("https://eternaltwin.org/login")
            time.sleep(3)
            loginForm = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME,"ng-pristine")))
            username = WebDriverWait(loginForm, 15).until(EC.presence_of_element_located((By.NAME, "login")))
            username.send_keys(bruteNames[0])
            password = WebDriverWait(loginForm, 15).until(EC.presence_of_element_located((By.NAME, "password")))
            password.send_keys(PASSWORD)
            button = WebDriverWait(loginForm, 15).until(EC.presence_of_element_located((By.NAME, "sign_in")))
            button.click()
            del loginForm
            del username
            del password
            del button
        except:
            print(color.RED + color.BOLD + "Account {}: LOGIN ACCOUNT FAILED".format(i + startAccount) + color.END)

        time.sleep(1)

        driver.get("https://brute.eternaltwin.org/")
        loginButton = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME,"MuiButtonBase-root")))
        loginButton.click()
        del loginButton

        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME,"css-17tdeih")))

        time.sleep(1)

        for j in range(len(bruteNames) - 1):
            printArray = []
            printArray.append("\nAccount {}: {} - Work in progress...".format(i + startAccount, bruteNames[j + 1]))

            driver.get("https://brute.eternaltwin.org/{}/cell".format(bruteNames[j + 1]))
            hasFightsLeft = True
            try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME,"css-v3tyeg")))
                hasFightsLeft = False

                printArray.append(color.GREEN + color.BOLD + "Account {}: {} - WINS A TOURNAMENT! HE CAN RANK UP!".format(i + startAccount, bruteNames[j + 1]) + color.END)
            except:
                try:
                    nextTournament = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME,"css-1rb3pee")))
                    if not nextTournament.text == "Brute inscrite.":
                        findTournament = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME,"css-1l4w6pd")))
                        tournament = WebDriverWait(findTournament, 15).until(EC.presence_of_element_located((By.TAG_NAME, "a")))
                        tournament.click()
                        del findTournament
                        del tournament

                        try:
                            tournamentSeen = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME,"css-9w9xg7")))
                            tournamentSeen.click()
                            del tournamentSeen

                            time.sleep(4)
                        except:
                            printArray.append(color.RED + "Account {}: {} - TOURNAMENT ALREADY SEEN".format(i + startAccount, bruteNames[j + 1]) + color.END)

                        driver.get("https://brute.eternaltwin.org/{}/cell".format(bruteNames[j + 1]))
                        try:
                            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME,"css-v3tyeg")))
                            hasFightsLeft = False

                            printArray.append(color.GREEN + color.BOLD + "Account {}: {} - WINS A TOURNAMENT! HE CAN RANK UP!".format(i + startAccount, bruteNames[j + 1]) + color.END)
                        except:
                            tournamentRegistration = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME,"css-yb6hwx")))
                            tournamentRegistration.click()
                            del tournamentRegistration

                            time.sleep(2)
                    else: 
                        printArray.append("Account {}: {} - Already registered in the tournament.".format(i + startAccount, bruteNames[j + 1]))
                    del nextTournament
                except:
                    printArray.append(color.RED + "Account {}: {} - TOURNAMENT REGISTRATION FAILED!".format(i + startAccount, bruteNames[j + 1]) + color.END)

            fightCounter = 0
            try:
                fightsWonBefore = int(driver.find_elements(By.CLASS_NAME, "css-a0dt3d")[1].text)
            except:
                fightsWonBefore = 0
                printArray.append(color.RED + "Account {}: {} - FIGHT COUNTER FAILED".format(i + startAccount, bruteNames[j + 1]) + color.END)

            while hasFightsLeft:
                try:
                    WebDriverWait(driver, 1.5).until(EC.presence_of_element_located((By.CLASS_NAME,"css-1dbhieh")))
                    printArray.append(color.CYAN + color.BOLD + "Account {}: {} - NEEDS TO LEVEL UP!".format(i + startAccount, bruteNames[j + 1]) + color.END)
                    hasFightsLeft = False
                except:
                    try:
                        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME,"css-vbasy3")))
                        try:
                            driver.get("https://brute.eternaltwin.org/{}/arena".format(bruteNames[j + 1]))

                            time.sleep(2)

                            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME,"css-xxeckd")))
                            randomOpponent = random.randint(0, 5)
                            opponents = driver.find_elements(By.CLASS_NAME, "css-rpybyc")
                            opponents[randomOpponent].click()
                            del randomOpponent
                            del opponents
                            
                            time.sleep(3)

                            runFight = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME,"css-3iozau")))
                            runFight.click()
                            del runFight

                            time.sleep(2.5)

                            fightCounter += 1
                        except:
                            printArray.append(color.RED + "Account {}: {} - FIGHT FAILED".format(i + startAccount, bruteNames[j + 1]) + color.END)

                        driver.get("https://brute.eternaltwin.org/{}/cell".format(bruteNames[j + 1]))
                    except:
                        hasFightsLeft = False

            if fightCounter == 0:
                printArray.append("Account {}: {} - Can't fight anymore, go to the next Brute.".format(i + startAccount, bruteNames[j + 1]))
            else:
                try:
                    fightsWonAfter = int(driver.find_elements(By.CLASS_NAME, "css-a0dt3d")[1].text)

                    wins = fightsWonAfter - fightsWonBefore
                    del fightsWonBefore
                    del fightsWonAfter

                    printArray.append(color.YELLOW + "Account {}: {} - Done. He won {}/{} fights!".format(i + startAccount, bruteNames[j + 1], wins, fightCounter) + color.END)
                    del wins
                except:
                    printArray.append(color.RED + "Account {}: {} - FIGHT COUNTER FAILED".format(i + startAccount, bruteNames[j + 1]) + color.END)

            for info in printArray:
                print(info)

        time.sleep(8)

        accountButton = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME,"css-17tdeih")))
        action = ActionChains(driver)
        action.move_to_element(accountButton).perform()
        del accountButton
        del action

        time.sleep(1.5)

        logout = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,"Compte-action-0")))
        logoutButton = WebDriverWait(logout, 15).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        logoutButton.click()
        del logout
        del logoutButton

        gc.collect()

        if quitDriver == 3:
            driver.quit()
            print(color.RED + color.BOLD + "\n--- DRIVER QUITTED ---" + color.END)

            time.sleep(2)

            options = Options()
            prefs = {"profile.managed_default_content_settings.images": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_argument("--disable-javascript")

            driver = webdriver.Chrome(options=options)
            driver.set_window_position(sizeArray[0], sizeArray[1])
            driver.set_window_size(sizeArray[2], sizeArray[3])

            quitDriver = 0

    driver.quit()
    print(color.RED + color.BOLD + "\n--- END OF THE PROCESS ---" + color.END)

if __name__ == "__main__":

    startTime = time.time()

    load_dotenv()
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

    multiprocess = input("Do you want to multiprocess the script ? (y/n) > ")
    if multiprocess == "y":
        nbreAccounts = len(accountsArray) - startAcc
        nbrePerProcess = int(nbreAccounts / 4)

        startAcc1 = startAcc
        sizeArray1 = [0, 0, 720, 800]
        process1 = multiprocessing.Process(target=ProceedAccounts, args=(startAcc1, nbrePerProcess, accountsArray, sizeArray1))
        print(color.BOLD + "Process1: from account n°{} to account n°{}!".format(startAcc1, startAcc1 + nbrePerProcess) + color.END)

        startAcc2 = startAcc + nbrePerProcess
        sizeArray2 = [720, 0, 720, 800]
        process2 = multiprocessing.Process(target=ProceedAccounts, args=(startAcc2, nbrePerProcess, accountsArray, sizeArray2))
        print(color.BOLD + "Process2: from account n°{} to account n°{}!".format(startAcc2, startAcc2 + nbrePerProcess) + color.END)

        startAcc3 = startAcc + nbrePerProcess * 2
        sizeArray3 = [0, 0, 720, 800]
        process3 = multiprocessing.Process(target=ProceedAccounts, args=(startAcc3, nbrePerProcess, accountsArray, sizeArray3))
        print(color.BOLD + "Process3: from account n°{} to account n°{}!".format(startAcc3, startAcc3 + nbrePerProcess) + color.END)

        startAcc4 = startAcc + nbrePerProcess * 3
        sizeArray4 = [720, 0, 720, 800]
        process4 = multiprocessing.Process(target=ProceedAccounts, args=(startAcc4, len(accountsArray) - startAcc4, accountsArray, sizeArray4))
        print(color.BOLD + "Process4: from account n°{} to account n°{}!".format(startAcc4, startAcc4 + len(accountsArray) - startAcc4) + color.END)

        process1.start()
        process2.start()
        process3.start()
        process4.start()

        process1.join()
        process2.join()
        process3.join()
        process4.join()
    else:
        ProceedAccounts(startAcc, len(accountsArray) - startAcc, accountsArray, [0, 0, 850, 850])
    
    time.sleep(1)

    executionTime = time.time() - startTime
    print(color.BOLD + "\n--- All accounts has been processed in {} seconds. ---".format(round(executionTime, 2)) + color.END)

# Next steps:
## Donner le nbre de win sur les tournois et contre quel lvl j'ai perdu ?
## Gérer les combats contre le boss de clan sur certains compte (autre script ? Qqc de spécial dans le 'accounts' ?)
