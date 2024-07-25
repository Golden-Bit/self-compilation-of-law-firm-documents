from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def login_and_search_anagrafica(username, password, denominazione):
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

        # Navigate to the "Anagrafiche" page
        anagrafiche_link = driver.find_element(By.XPATH, "//a[@href='/anagrafiche']")
        anagrafiche_link.click()

        # Wait for the page to load
        time.sleep(5)

        # Insert the search term in the search field
        search_field = driver.find_element(By.ID, "searchField")
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

        # Wait for 10 seconds
        time.sleep(10)

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    # Request username, password, and denominazione from the user
    user_username = "fabiana"  # input("Enter your username: ")
    user_password = "Faby0311@"  # input("Enter your password: ")
    search_denominazione = "abc"  # input("Enter the denominazione to search: ")

    # Perform login and search anagrafica
    login_and_search_anagrafica(user_username, user_password, search_denominazione)
