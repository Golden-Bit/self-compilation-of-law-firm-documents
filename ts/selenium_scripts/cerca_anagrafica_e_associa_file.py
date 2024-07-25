import json
from typing import List, Tuple

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

def search_and_upload_file(driver, denominazione, file_path):
    # Insert the search term in the search field
    search_field = driver.find_element(By.ID, "searchField")
    search_field.clear()  # Clear any previous text in the search field
    search_field.send_keys(denominazione)

    # Click the search button
    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()

    # Wait for the search results to load
    time.sleep(5)

    # Find the first result row
    results = driver.find_elements(By.XPATH, "//tr[contains(@class, 'soggetti-row')]")
    for result in results:
        denominazione_result = result.find_element(By.XPATH, ".//td[2]/div").text
        if denominazione_result == denominazione:
            result.click()
            break

    # Wait for the anagrafica details to load
    time.sleep(5)

    # Locate the file input element and upload the file
    file_input = driver.find_element(By.CSS_SELECTOR, "input.upload-documents-input[type='file']")
    file_input.send_keys(file_path)

    # Wait for the upload to complete
    time.sleep(10)

def process_denominations_and_files(driver, denominations_and_files):
    for denominazione, file_path in denominations_and_files:
        search_and_upload_file(driver, denominazione, file_path)
        navigate_to_anagrafiche(driver)  # Navigate back to the "Anagrafiche" page for the next iteration


def importa_documenti(denominations_and_files: List[Tuple[str, str]]):

    # Request username and password from the user
    user_username = "fabiana"  # input("Enter your username: ")
    user_password = "Faby0311@"  # input("Enter your password: ")

    # Initialize the Chrome WebDriver
    service = Service('C:\\Users\\Golden Bit\\Downloads\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    try:
        # Perform login
        login_to_site(driver, user_username, user_password)

        # Navigate to the "Anagrafiche" page for the first time
        navigate_to_anagrafiche(driver)

        # Process each denomination and file pair
        process_denominations_and_files(driver, denominations_and_files)

    finally:
        # Close the browser
        driver.quit()


    return


if __name__ == "__main__":
    # Dati di esempio
    denominations_and_files = [
        ("abc", "C:\\Users\\Golden Bit\\Desktop\\projects_in_progress\\GoldenProjects\\golden_bit\\repositories\\self-compilation-of-law-firm-documents\\input_data\\TemplateLetteraDiffida.docx"),
        ("abc", "C:\\Users\\Golden Bit\\Desktop\\projects_in_progress\\GoldenProjects\\golden_bit\\repositories\\self-compilation-of-law-firm-documents\\input_data\\TemplateLetteraDiffida_.docx")
    ]

    # Request username and password from the user
    user_username = "fabiana"  # input("Enter your username: ")
    user_password = "Faby0311@"  # input("Enter your password: ")

    # Initialize the Chrome WebDriver
    service = Service('C:\\Users\\Golden Bit\\Downloads\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    try:
        # Perform login
        login_to_site(driver, user_username, user_password)

        # Navigate to the "Anagrafiche" page for the first time
        navigate_to_anagrafiche(driver)

        # Process each denomination and file pair
        process_denominations_and_files(driver, denominations_and_files)

    finally:
        # Close the browser
        driver.quit()
