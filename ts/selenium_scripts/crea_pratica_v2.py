import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Dati di esempio da un JSON
dati_pratica = {
    "tipologia": "1",  # Contenzioso civile == POLISWEB
    "nome_pratica": "Esempio Pratica",
    "descrizione": "Descrizione della nuova pratica",
    "categoria": "-1",
    "oggetto": "Oggetto della pratica",
    "avvocato": "1",  # Maria Afrodite Carotenuto
    "stato": "8",  # Aperta
    "data_apertura": "2023-07-17",
    "valore": "10000"
}

def login_to_site_and_create_pratica(username, password):
    # Path to the ChromeDriver
    service = Service('C:\\Users\\Golden Bit\\Downloads\\chromedriver-win64\\chromedriver.exe')

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=service)

    try:
        # Navigate to the login page
        driver.get("https://slcarotenuto.netlex.cloud/")

        # Find the username field and input the username
        username_field = driver.find_element(By.ID, "unamelogin")
        username_field.send_keys(username)

        # Find the password field and input the password
        password_field = driver.find_element(By.ID, "psswdlogin")
        password_field.send_keys(password)

        # Find the login button and click it
        login_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary[type='submit']")
        login_button.click()

        # Wait for the page to load
        time.sleep(5)

        # Navigate to the "Pratiche" page
        pratiche_link = driver.find_element(By.XPATH, "//a[@href='/archive/archive']")
        pratiche_link.click()

        # Wait for the page to load
        time.sleep(5)

        # Click the button to create a new "Pratica"
        new_pratica_button = driver.find_element(By.XPATH, "//a[@href='#' and contains(@class, 'btn-primary') and contains(@onclick, 'insertFile()')]")
        new_pratica_button.click()

        # Wait for the popup to load
        time.sleep(3)

        # Fill in the form fields with data from the JSON
        driver.find_element(By.ID, "tipologiapratica").send_keys(dati_pratica["tipologia"])
        driver.find_element(By.ID, "nomepratica").send_keys(dati_pratica["nome_pratica"])
        driver.find_element(By.ID, "descrizione").send_keys(dati_pratica["descrizione"])
        driver.find_element(By.ID, "categoria").send_keys(dati_pratica["categoria"])
        driver.find_element(By.ID, "searchOggettoPratica").send_keys(dati_pratica["oggetto"])
        driver.find_element(By.ID, "avvocato").send_keys(dati_pratica["avvocato"])
        driver.find_element(By.ID, "statopratica").send_keys(dati_pratica["stato"])

        # Assuming there are fields for data_apertura and valore
        driver.find_element(By.ID, "data_apertura").send_keys(dati_pratica["data_apertura"])
        driver.find_element(By.ID, "valore").send_keys(dati_pratica["valore"])

        # Click the "Conferma" button
        conferma_button = driver.find_element(By.ID, "saveFileButton")
        conferma_button.click()

        # Wait for 10 seconds
        time.sleep(10)

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    # Request username and password from the user
    user_username = "fabiana" #input("Enter your username: ")
    user_password = "Faby0311@" #input("Enter your password: ")

    # Perform login and create a new pratica
    login_to_site_and_create_pratica(user_username, user_password)
