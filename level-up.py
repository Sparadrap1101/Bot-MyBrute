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

if __name__ == "__main__":

    startTime = time.time()

    executionTime = time.time() - startTime
    print("\n--- All accounts has been processed in {} seconds. ---".format(round(executionTime, 2)))
