import json
import logging
from typing import List, Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def login_to_site(driver, username, password):
    # Navigate to the login page
    driver.get("https://slcarotenuto.netlex.cloud/")

    while True:
        try:
            # Find the username field and input the username
            username_field = driver.find_element(By.ID, "unamelogin")
            username_field.send_keys(username)
            break
        except Exception as e:
            print(e)
            continue

    while True:
        try:
            # Find the password field and input the password
            password_field = driver.find_element(By.ID, "psswdlogin")
            password_field.send_keys(password)
            break
        except Exception as e:
            print(e)
            continue

    while True:
        try:
            # Find the login button and click it
            login_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary[type='submit']")
            login_button.click()
            break
        except Exception as e:
            print(e)
            continue

    # Wait for the page to load
    # time.sleep(5)


def navigate_to_pratiche(driver):

    while True:
        try:
            # Navigate to the "Anagrafiche" page
            anagrafiche_link = driver.find_element(By.XPATH, "//a[@href='/archive/archive']")
            anagrafiche_link.click()
            break
        except Exception as e:
            print(e)
            continue

    # Wait for the page to load
    # time.sleep(5)


def search_and_upload_file(driver, denominazione, file_path):

    while True:
        try:
            # Insert the search term in the search field
            search_field = driver.find_element(By.ID, "counterpart")
            search_field.clear()  # Clear any previous text in the search field
            search_field.send_keys(denominazione)
            break
        except Exception as e:
            print(e)
            continue

    while True:
        try:
            # Insert the search term in the search field
            search_field = driver.find_element(By.ID, "customer")
            search_field.clear()  # Clear any previous text in the search field
            search_field.send_keys("SEV SPA")
            break
        except Exception as e:
            print(e)
            continue

    while True:
        try:
            # Click the search button
            search_button = driver.find_element(By.ID, "archiveSearchButton")
            search_button.click()
            break
        except Exception as e:
            print(e)
            continue
    # Wait for the search results to load
    # time.sleep(5)

    is_clicked = False
    while True:
        try:
            # Find the first result row
            results = driver.find_elements(By.XPATH, "//tr[contains(@class, 'soggetti-row')]")
            results[0].click()
            is_clicked = True
            if is_clicked:
                break
        except Exception as e:
            print(e)
            continue

    # New logic for clicking the link and uploading the file
    while True:
        try:
            # Click the "Vedi tutti..." link
            view_all_link = driver.find_element(By.XPATH, "//a[contains(@href, '/archivedocuments/documents')]")
            view_all_link.click()
            break
        except Exception as e:
            print(e)
            continue

    # Wait for the new page to load
    # time.sleep(5)

    while True:
        try:
            # Click the "Carica sul gestionale" button to trigger the file upload
            upload_button = driver.find_element(By.ID, "carica_doc_gestionale")
            upload_input = upload_button.find_element(By.XPATH, ".//input[@type='file']")
            upload_input.send_keys(file_path)
            break
        except Exception as e:
            print(e)
            continue

    # Wait for the upload to complete
    # time.sleep(10)


def process_denominations_and_files(driver, denominations_and_files):
    for denominazione, file_path in denominations_and_files:
        search_and_upload_file(driver, denominazione, file_path)
        navigate_to_pratiche(driver)  # Navigate back to the "Anagrafiche" page for the next iteration


def importa_documenti(denominations_and_files: List[Tuple[str, str]]):
    # Set up logging
    logging.basicConfig(filename='importa_documenti_errors.log', level=logging.ERROR)

    # Request username and password from the user
    user_username = "fabiana"  # input("Enter your username: ")
    user_password = "Faby0311@"  # input("Enter your password: ")

    # Initialize the Chrome WebDriver
    service = Service('C:\\Users\\Golden Bit\\Desktop\\projects_in_progress\\GoldenProjects\\golden_bit\\repositories\\self-compilation-of-law-firm-documents\\ts\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    try:
        # Perform login
        login_to_site(driver, user_username, user_password)

        # Navigate to the "Anagrafiche" page for the first time
        navigate_to_pratiche(driver)

        # Process each denomination and file pair
        for denominazione, file_path in denominations_and_files:
            try:
                process_denominations_and_files(driver, [(denominazione, file_path)])
            except Exception as e:
                error_message = "\n#\n" * 120 + f"Failed to upload document '{file_path}' for '{denominazione}': {str(e)}" + "\n#\n" * 120
                logging.error(error_message)
                print(error_message)

    finally:
        # Close the browser
        driver.quit()

    return


if __name__ == "__main__":
    # Dati di esempio
    denominations_and_files = [
        ("abc", "C:\\Users\\Golden Bit\\Desktop\\projects_in_progress\\GoldenProjects\\golden_bit\\repositories\\self-compilation-of-law-firm-documents\\input_data\\TemplateLetteraDiffida.docx"),
        ("def", "C:\\Users\\Golden Bit\\Desktop\\projects_in_progress\\GoldenProjects\\golden_bit\\repositories\\self-compilation-of-law-firm-documents\\input_data\\TemplateLetteraDiffida_.docx"),
        ("abc", "C:\\Users\\Golden Bit\\Desktop\\projects_in_progress\\GoldenProjects\\golden_bit\\repositories\\self-compilation-of-law-firm-documents\\input_data\\TemplateLetteraDiffida.docx"),
        ("def", "C:\\Users\\Golden Bit\\Desktop\\projects_in_progress\\GoldenProjects\\golden_bit\\repositories\\self-compilation-of-law-firm-documents\\input_data\\TemplateLetteraDiffida_.docx")
    ]

    # Request username and password from the user
    user_username = "fabiana"  # input("Enter your username: ")
    user_password = "Faby0311@"  # input("Enter your password: ")

    # Initialize the Chrome WebDriver
    service = Service('C:\\Users\\Golden Bit\\Desktop\\projects_in_progress\\GoldenProjects\\golden_bit\\repositories\\self-compilation-of-law-firm-documents\\ts\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    try:
        # Perform login
        login_to_site(driver, user_username, user_password)

        # Navigate to the "Anagrafiche" page for the first time
        navigate_to_pratiche(driver)

        # Process each denomination and file pair
        #process_denominations_and_files(driver, denominations_and_files)
        # Set up logging
        logging.basicConfig(filename='importa_documenti_errors.log', level=logging.ERROR)

        for denominazione, file_path in denominations_and_files:
            try:
                process_denominations_and_files(driver, [(denominazione, file_path)])
            except Exception as e:
                error_message = f"Failed to upload document '{file_path}' for '{denominazione}': {str(e)}"
                logging.error(error_message)
                print(error_message)

    finally:
        # Close the browser
        driver.quit()
