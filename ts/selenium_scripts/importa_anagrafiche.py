import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def login_to_site(driver, username, password):
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


def navigate_to_anagrafiche(driver):
    # Navigate to the "Anagrafiche" page
    anagrafiche_link = driver.find_element(By.XPATH, "//a[@href='/anagrafiche']")
    anagrafiche_link.click()

    # Wait for the page to load
    time.sleep(5)


def upload_csv_and_import(driver, csv_path):
    # Locate the file input element and upload the CSV file
    file_input = driver.find_element(By.ID, "file")
    file_input.send_keys(csv_path)

    time.sleep(2)

    # Click the "Importa Anagrafiche" button
    import_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success[name='import']")
    import_button.click()

    # Wait for the import to complete
    time.sleep(2)


def importa_anagrafiche(csv_path: str):

    # Request username, password, and CSV path from the user
    user_username = "fabiana"  # input("Enter your username: ")
    user_password = "Faby0311@"  # input("Enter your password: ")

    # Initialize the Chrome WebDriver
    service = Service('C:\\Users\\Golden Bit\\Downloads\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    try:
        # Perform login
        login_to_site(driver, user_username, user_password)

        # Navigate to the "Anagrafiche" page
        navigate_to_anagrafiche(driver)

        # Upload the CSV file and start the import
        upload_csv_and_import(driver, csv_path)

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":

    csv_path = "C:\\Users\\Golden Bit\\Downloads\\dati_tutti_soggetti(5).csv"  # input("Enter the path to the CSV file: ")

    importa_anagrafiche(csv_path)
