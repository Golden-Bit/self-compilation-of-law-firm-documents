import json
from typing import Dict, Any, Tuple, List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import Select

d_t = 1

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
    time.sleep(5*d_t)


def navigate_to_pratiche(driver):
    # Navigate to the "Pratiche" page
    pratiche_link = driver.find_element(By.XPATH, "//a[@href='/archive/archive']")
    pratiche_link.click()

    # Wait for the page to load
    time.sleep(5*d_t)


def create_pratica(driver, denominazione, dati_pratica):

    # Click the button to create a new "Pratica"
    new_pratica_button = driver.find_element(By.XPATH, "//a[@href='#' and contains(@class, 'btn-primary') and contains(@onclick, 'insertFile()')]")
    new_pratica_button.click()

    # Wait for the popup to load
    time.sleep(3*d_t)

    # Fill in the form fields with data from the JSON
    #driver.find_element(By.ID, "tipologiapratica").send_keys(dati_pratica["tipologia"])
    # driver.send_keys(dati_pratica["tipologia"])
    select = Select(driver.find_element(By.ID, "tipologiapratica"))
    select.select_by_value(dati_pratica["tipologia"])

    driver.find_element(By.ID, "nomepratica").send_keys(dati_pratica["nome_pratica"])

    # Ensure the "descrizione" field is interactable
    descrizione_field = driver.find_element(By.ID, "descrizione")
    driver.execute_script("arguments[0].scrollIntoView(true);", descrizione_field)
    descrizione_field.click()
    descrizione_field.send_keys(dati_pratica["descrizione"])

    driver.find_element(By.ID, "categoria").send_keys(dati_pratica["categoria"])
    driver.find_element(By.ID, "searchOggettoPratica").send_keys(dati_pratica["oggetto"])
    driver.find_element(By.ID, "avvocato").send_keys(dati_pratica["avvocato"])
    driver.find_element(By.ID, "statopratica").send_keys(dati_pratica["stato"])

    ####################################################################################################################
    #driver.find_element(By.ID, "dataapertura").send_keys(dati_pratica["data_apertura"])

    time.sleep(1*d_t)
    date_input = driver.find_element(By.ID, 'dataapertura')
    time.sleep(1*d_t)
    # Rimuovi l'attributo onfocus per permettere l'input manuale
    driver.execute_script("arguments[0].removeAttribute('onfocus')", date_input)
    time.sleep(1*d_t)
    # Imposta la data
    date_input.clear()
    time.sleep(1*d_t)
    date_input.send_keys(dati_pratica["data_apertura"])
    time.sleep(1*d_t)
    ####################################################################################################################

    driver.find_element(By.ID, "tipoValore").send_keys(dati_pratica["tipo_valore"])
    driver.find_element(By.ID, "valore").clear()
    time.sleep(1*d_t)
    driver.find_element(By.ID, "valore").send_keys(dati_pratica["valore"])

    # Click the "Conferma" button
    conferma_button = driver.find_element(By.ID, "saveFileButton")
    conferma_button.click()

    # Wait for the next page to load
    time.sleep(5*d_t)

    # Click on the "Soggetti" tab
    soggetti_tab = driver.find_element(By.XPATH, "//a[@href='#tabs-2-archive' and contains(@class, 'text-menu')]")
    soggetti_tab.click()

    # Wait for the page to load
    time.sleep(5*d_t)

    ####################################################################################################################
    # Click on the "Seleziona Anagrafiche" button
    seleziona_anagrafiche_button = driver.find_element(By.ID, "newPartButton")
    seleziona_anagrafiche_button.click()

    # Wait for the popup to load
    time.sleep(3*d_t)

    # Switch to the iframe containing the search form
    driver.switch_to.frame(driver.find_element(By.ID, "addPartsFrame"))

    # Insert the search term in the search field in the iframe
    popup_search_field = driver.find_element(By.ID, "searchField")
    popup_search_field.clear()
    popup_search_field.send_keys(denominazione)

    # Wait for the search results to load
    time.sleep(3*d_t)

    # Select the correct row based on denominazione
    rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'soggetti-row')]")
    for row in rows:
        #print("°"*100)
        #print(row)
        cell = row.find_element(By.XPATH, ".//td[2]/span")
        #print(cell.get_attribute("title"), denominazione)
        if cell.get_attribute("title") == denominazione:
            row.click()
            break

    # Wait for the popup to open
    time.sleep(3*d_t)

    # Switch to the newly opened modal (if necessary)
    driver.switch_to.default_content()  # Switch back to default content
    modal_iframe = driver.find_element(By.CSS_SELECTOR, "iframe[src*='frameindex']")
    driver.switch_to.frame(modal_iframe)

    time.sleep(2*d_t)

    # Select "Controparte" for both dropdowns
    person_role_select = driver.find_element(By.ID, "personRole")
    time.sleep(1 * d_t)
    person_role_select.send_keys("Controparte")

    relazione_select = driver.find_element(By.ID, "relazione")
    time.sleep(1 * d_t)
    relazione_select.send_keys("Controparte")

    # Click the "Aggiungi" button
    add_button = driver.find_element(By.ID, "addPartButton")
    add_button.click()
    ####################################################################################################################
    driver.switch_to.default_content()
    time.sleep(3)
    #input("...")
    ####################################################################################################################
    seleziona_anagrafiche_button = driver.find_element(By.ID, "newPartButton")
    seleziona_anagrafiche_button.click()

    # Wait for the popup to load
    time.sleep(3*d_t)

    # Switch to the iframe containing the search form
    driver.switch_to.frame(driver.find_element(By.ID, "addPartsFrame"))

    # Insert the search term in the search field in the iframe
    popup_search_field = driver.find_element(By.ID, "searchField")
    popup_search_field.clear()
    time.sleep(1 * d_t)
    popup_search_field.send_keys("SEV SPA")

    # Wait for the search results to load
    time.sleep(3*d_t)

    # Select the correct row based on denominazione
    rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'soggetti-row')]")
    for row in rows:
        # print("°"*100)
        # print(row)
        cell = row.find_element(By.XPATH, ".//td[2]/span")
        # print(cell.get_attribute("title"), denominazione)
        if cell.get_attribute("title") == "SEV SPA":
            row.click()
            break

    # Wait for the popup to open
    time.sleep(3*d_t)

    # Switch to the newly opened modal (if necessary)
    driver.switch_to.default_content()  # Switch back to default content
    modal_iframe = driver.find_element(By.CSS_SELECTOR, "iframe[src*='frameindex']")
    driver.switch_to.frame(modal_iframe)

    time.sleep(2*d_t)

    # Select "Controparte" for both dropdowns
    person_role_select = driver.find_element(By.ID, "personRole")
    time.sleep(1 * d_t)
    person_role_select.send_keys("Cliente")

    #relazione_select = driver.find_element(By.ID, "relazione")
    #relazione_select.select_by_value('1')
    select = Select(driver.find_element(By.ID, "relazione"))
    time.sleep(1 * d_t)
    select.select_by_value('1')


    # Click the "Aggiungi" button
    add_button = driver.find_element(By.ID, "addPartButton")
    add_button.click()
    ####################################################################################################################
    # Wait for the action to complete
    time.sleep(5*d_t)

    # Switch back to the default content after the modal interaction
    driver.switch_to.default_content()

    # Navigate back to the "Pratiche" page
    #navigate_to_pratiche(driver)


def genera_pratiche(subjects_dict: Dict[str, Any]):

    pratiche = []

    for subject_key, subject_info in subjects_dict.items():

        denominazione = subject_info["Ragione_Sociale"]

        pratica = {
            "tipologia": "11",
            "nome_pratica": "Recupero credito SEV",
            "descrizione": "Recupero credito SEV- Stragiudiziale",
            "categoria": "-1",
            "oggetto": "Recupero credito SEV",
            "avvocato": "1",
            "stato": "8",
            "data_apertura": subject_info.get("Data affido"),
            "tipo_valore": "0",
            "valore": subject_info.get("Residuo ad oggi")
        }

        pratiche.append((denominazione, pratica))

    return pratiche


def importa_pratiche(subjects_dict: Dict[str, Any]):

    # Request username and password from the user
    user_username = "fabiana" #input("Enter your username: ")
    user_password = "Faby0311@" #input("Enter your password: ")

    # Initialize the Chrome WebDriver
    service = Service('C:\\Users\\Golden Bit\\Downloads\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    pratiche = genera_pratiche(subjects_dict)

    try:
        # Perform login
        login_to_site(driver, user_username, user_password)

        # Iterate over each denominazione and dati_pratica pair
        for denominazione, dati_pratica in pratiche:
            dati_pratica["valore"] = str(dati_pratica["valore"]).replace(".", "").replace(",", ".")
            print(json.dumps(dati_pratica, indent=2))
            navigate_to_pratiche(driver)
            create_pratica(driver, denominazione, dati_pratica)

    finally:
        # Close the browser
        driver.quit()

    return


if __name__ == "__main__":
    # Dati di esempio
    dati_pratiche_list = [
        ("abc", {
            "tipologia": "1",
            "nome_pratica": "Esempio Pratica 1",
            "descrizione": "Descrizione della nuova pratica 1",
            "categoria": "-1",
            "oggetto": "Oggetto della pratica 1",
            "avvocato": "1",
            "stato": "8",
            "data_apertura": "17/07/2023",
            "tipo_valore": "0",
            "valore": "10000"
        }),
        ("abc", {
            "tipologia": "1",
            "nome_pratica": "Esempio Pratica 2",
            "descrizione": "Descrizione della nuova pratica 2",
            "categoria": "-1",
            "oggetto": "Oggetto della pratica 2",
            "avvocato": "1",
            "stato": "8",
            "data_apertura": "17/07/2023",
            "tipo_valore": "0",
            "valore": "20000"
        })
    ]

    #importa_pratiche()