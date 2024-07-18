import streamlit as st

from ts.mapping_anagrafiche_v3 import process_file, converti_in_csv, genera_dizionario_soggetti


# Interfaccia utente con Streamlit
def estrai_anagrafiche():
    st.title("Generatore di CSV da Anagrafiche")
    #st.write("Carica i tre file CSV per generare il file CSV di output.")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        uploaded_file1 = st.file_uploader("Carica il primo file CSV (Anagrafiche)", type=['csv', 'xlsx'])
    with col2:
        uploaded_file2 = st.file_uploader("Carica il secondo file CSV (Fatture)", type=['csv', 'xlsx'])
    with col3:
        uploaded_file3 = st.file_uploader("Carica il terzo file CSV (Pratiche)", type=['csv', 'xlsx'])

    st.markdown("---")

    # Caricamento dei file

    if uploaded_file1 and uploaded_file2 and uploaded_file3:
        # Processare i file caricati
        df1 = process_file(uploaded_file1)
        df2 = process_file(uploaded_file2)
        df3 = process_file(uploaded_file3)

        # Generare il dizionario dei soggetti
        soggetti_dict = genera_dizionario_soggetti(df1, df2, df3)

        # Convertire il dizionario in CSV
        csv_output = converti_in_csv(soggetti_dict)

        # Creare un pulsante per il download del CSV
        st.download_button(
            label="Scarica il CSV di output",
            data=csv_output,
            file_name="dati_tutti_soggetti.csv",
            mime="text/csv",
            use_container_width=True
        )
