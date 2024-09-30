from selenium import webdriver

# Créez une instance du webdriver avec un chemin spécifique vers le chromedriver
# Assurez-vous de remplacer le chemin par le chemin où se trouve votre chromedriver
driver = webdriver.Chrome()

# Obtenez la version du ChromeDriver à partir de la propriété 'capabilites'
version_chromedriver = driver.capabilities['chrome']['chromedriverVersion']

print(f"Version de ChromeDriver : {version_chromedriver}")

# Fermez le navigateur
driver.quit()
