import os
from pathlib import Path

import streamlit as st

#from ts.mapping_anagrafiche_v3 import process_file, converti_in_csv, genera_dizionario_soggetti
from mapping_anagrafiche_v3 import process_file, converti_in_csv, genera_dizionario_soggetti
from selenium_scripts.importa_anagrafiche import importa_anagrafiche


# Interfaccia utente con Streamlit
import json
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import tempfile

#from ts.selenium_scripts.crea_pratiche_e_associa_anagrafiche_ import importa_pratiche
from selenium_scripts.crea_pratiche_e_associa_anagrafiche import importa_pratiche
#from ts.selenium_scripts.cerca_anagrafica_e_associa_file import importa_documenti
from selenium_scripts.cerca_anagrafica_e_associa_file import importa_documenti


st.set_page_config(layout="wide")


def estrai_anagrafiche():
    st.title("Automazioni Team System")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        uploaded_file1 = st.file_uploader("Carica il primo file CSV (Anagrafiche)", type=['csv', 'xlsx'])
    with col2:
        uploaded_file2 = st.file_uploader("Carica il secondo file CSV (Fatture)", type=['csv', 'xlsx'])
    with col3:
        uploaded_file3 = st.file_uploader("Carica il terzo file CSV (Pratiche)", type=['csv', 'xlsx'])

    #st.markdown("---")

    if uploaded_file1 and uploaded_file2 and uploaded_file3:
        # Processare i file caricati
        df1 = process_file(uploaded_file1)
        df2 = process_file(uploaded_file2)
        df3 = process_file(uploaded_file3)

        # Generare il dizionario dei soggetti
        soggetti_dict = genera_dizionario_soggetti(df1, df2, df3)

        soggetti_dict = {k: v for k, v in list(soggetti_dict.items())[:3]}

        # Convertire il dizionario in CSV
        csv_output = converti_in_csv(soggetti_dict)

        # Salvare il CSV in un file temporaneo
        with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp_file:
            tmp_file.write(csv_output.encode('utf-8'))
            tmp_file_path = tmp_file.name

        # Creare un pulsante per il download del CSV
        st.download_button(
            label="Scarica il CSV di output",
            data=csv_output,
            file_name="dati_tutti_soggetti.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.markdown("---")

        # Creare un pulsante per avviare l'importazione
        if st.button('Avvia Importazione Anagrafiche', use_container_width=True):
            importa_anagrafiche(tmp_file_path)
            st.success('Importazione completata!')

        # Creare un pulsante per avviare l'importazione
        if st.button('Avvia Importazione Pratiche', use_container_width=True):
            # write here call to function used to perform this task
            # TODO:
            #  - [ ] use 'soggetti_dict' variable and iterate on subjects in order to create dict representation of a
            #  'Pratica' object
            importa_pratiche(soggetti_dict)
            st.success('Importazione completata!')

        st.markdown("---")

        uploaded_file4 = st.file_uploader("Carica documenti (Lettere di Diffida)", type=['docx', 'pdf'],
                                          accept_multiple_files=True)

        if uploaded_file4:
            # Creare un pulsante per avviare l'importazione
            if st.button('Avvia Importazione Lettere di Diffida', use_container_width=True):
                # write here call to function used to perform this task
                # TODO:
                #  - [ ] use subject's name situated inside document name in order to upload document into team
                #  system platform
                temp_files = []
                denominations_and_files = []
                temp_dir = 'temp_data'
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)

                for uploaded_file in uploaded_file4:
                    temp_file_path = os.path.join(temp_dir, uploaded_file.name)
                    with open(temp_file_path, 'wb') as f:
                        f.write(uploaded_file.getbuffer())
                    temp_files.append(temp_file_path)
                    file_name = os.path.splitext(uploaded_file.name)[
                        0]  # Use the filename (without extension) as the denomination
                    denominazione = file_name.split("_")[0]
                    denominations_and_files.append((denominazione, str(Path(temp_file_path).absolute())))

                importa_documenti(denominations_and_files)
                for temp_file in temp_files:
                    os.remove(temp_file)
                st.success('Importazione completata!')

        st.markdown("---")


if __name__ == "__main__":
    estrai_anagrafiche()
