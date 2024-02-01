import os
import time
import random
import threading
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def ProceedAccounts(startAccount):
    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-javascript")

    driver = webdriver.Chrome(options=options)
    driver.set_window_position(0, 0)
    driver.set_window_size(1040, 850)

    for i in range(len(accountsArray) - startAccount):
        bruteNames = accountsArray[i + startAccount].split(" ")
        print("\nAccount {}: Brute names = {}".format(i + startAccount, bruteNames))

        try:
            driver.get("https://eternaltwin.org/login")
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
            print("LOGIN ACCOUNT FAILED")
        
        time.sleep(1)

        driver.get("https://brute.eternaltwin.org/")
        loginButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"MuiButtonBase-root")))
        loginButton.click()
        del loginButton

        time.sleep(3)

        for j in range(3):
            print("\n{} is working...".format(bruteNames[j + 1]))

            driver.get("https://brute.eternaltwin.org/{}/cell".format(bruteNames[j + 1]))
            hasFightsLeft = True
            try:
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME,"css-v3tyeg")))
                hasFightsLeft = False

                print("{} WINS A TOURNAMENT! HE CAN RANK UP!".format(bruteNames[j + 1]))
            except:
                try:
                    nextTournament = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"css-1rb3pee")))
                    if not nextTournament.text == "Brute inscrite.":
                        findTournament = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"css-1l4w6pd")))
                        tournament = WebDriverWait(findTournament, 10).until(EC.presence_of_element_located((By.TAG_NAME, "a")))
                        tournament.click()
                        del findTournament
                        del tournament

                        try:
                            tournamentSeen = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"css-9w9xg7")))
                            tournamentSeen.click()
                            del tournamentSeen

                            time.sleep(1.5)
                        except:
                            print("TOURNAMENT ALREADY SEEN")

                        driver.get("https://brute.eternaltwin.org/{}/cell".format(bruteNames[j + 1]))
                        try:
                            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME,"css-v3tyeg")))
                            hasFightsLeft = False

                            print("{} WINS A TOURNAMENT! HE CAN RANK UP!".format(bruteNames[j + 1]))
                        except:
                            tournamentRegistration = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"css-yb6hwx")))
                            tournamentRegistration.click()
                            del tournamentRegistration

                            time.sleep(1)
                    else: 
                        print("Already registered in the tournament.")
                    del nextTournament
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
                    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME,"css-1dbhieh")))
                    print("{} NEEDS TO LEVEL UP!".format(bruteNames[j + 1]))
                    hasFightsLeft = False
                except:
                    try:
                        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME,"css-vbasy3")))
                        try:
                            driver.get("https://brute.eternaltwin.org/{}/arena".format(bruteNames[j + 1]))

                            time.sleep(1)

                            randomOpponent = random.randint(0, 5)
                            opponents = driver.find_elements(By.CLASS_NAME, "css-rpybyc")
                            opponents[randomOpponent].click()
                            del randomOpponent
                            del opponents

                            runFight = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"css-1e0h3j1")))
                            runFight.click()
                            del runFight

                            fightCounter += 1
                        except:
                            print("FIGHT FAILED")

                        driver.get("https://brute.eternaltwin.org/{}/cell".format(bruteNames[j + 1]))
                    except:
                        hasFightsLeft = False

            time.sleep(1.5)

            if fightCounter == 0:
                print("{} can't fight anymore, go to the next Brute.".format(bruteNames[j + 1]))
            else:
                try:
                    fightsWonAfter = int(driver.find_elements(By.CLASS_NAME, "css-a0dt3d")[1].text)

                    wins = fightsWonAfter - fightsWonBefore
                    del fightsWonBefore
                    del fightsWonAfter

                    print("{} is done. He won {}/{} fights!".format(bruteNames[j + 1], wins, fightCounter))
                    del wins
                except:
                    print("FIGHT COUNTER FAILED")

        accountButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"MuiFab-primary")))
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
    print("\n--- DRIVER QUITTED ---")

    time.sleep(4)

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


# Next steps:
## Donner le nbre de win sur les tournois et contre quel lvl j'ai perdu ?
## Gérer les combats contre le boss de clan sur certains compte (autre script ? Qqc de spécial dans le 'accounts' ?)
## Essayer d'optimiser/réduire le temps en restant safe sur les délais de chargement
## Faire du Threading pour essayer de lancer l'exécution de plusieurs compte en même temps
## Faire un mode à activer ou non pour passer automatiquement les levels
## Régler problème de déconnexion qui bug quand tu fais autre chose en même temps
## Gérer le cas où y'a 4+ brutes sur un compte
