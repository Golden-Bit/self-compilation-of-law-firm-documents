from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def login_to_site(username, password):
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

        # Click the button to create a new "Anagrafica"
        new_anagrafica_button = driver.find_element(By.XPATH, "//a[@href='/anagrafiche/update' and contains(@class, 'btn-primary')]")
        new_anagrafica_button.click()

        # Wait for 10 seconds
        time.sleep(10)

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    # Request username and password from the user
    user_username = "fabiana"  # input("Enter your username: ")
    user_password = "Faby0311@"  # input("Enter your password: ")
    #search_denominazione = "abc"  # input("Enter the denominazione to search: ")

    # Perform login
    login_to_site(user_username, user_password)
