import json
import pandas as pd


# Funzione per processare i file caricati
def process_file(file):
    if isinstance(file, str):
        file_type = file.split('.')[-1]
    else:
        file_type = file.name.split('.')[-1]
    if file_type == 'csv':
        df = pd.read_csv(file, delimiter=';', on_bad_lines='skip').fillna('')
    elif file_type == 'xlsx':
        df = pd.read_excel(file).fillna('')
    else:
        raise ValueError("Formato file non supportato. Caricare un file .csv o .xlsx.")
    return df


# Funzione per aggiornare il dizionario dei soggetti
def aggiorna_soggetto(soggetti_dict, keys, info):
    for key in keys:
        if key not in soggetti_dict:
            soggetti_dict[key] = {
                'Ragione_Sociale': '',
                'Partita_Iva': '',
                'Codice_Fiscale': '',
                'Indirizzo_Spedizione': '',
                'Cap_Spedizione': '',
                'Comune_Spedizione': '',
                'Telefono_Soggetto': '',
                'Telefono_Secondario': '',
                'Email_Soggetto': '',
                'Pec_Soggetto': '',
                'Codice_Soggetto': '',
                'Numero affido': '',
                'Data affido': '',
                'Residuo ad oggi': ''
            }
        for k, v in info.items():
            if v and not soggetti_dict[key].get(k):
                soggetti_dict[key][k] = v


# Funzione per generare il dizionario dei soggetti
def genera_dizionario_soggetti(df1, df2, df3):
    soggetti_dict = {}

    # Popolamento del dizionario dai vari DataFrame
    for index, row in df1.iterrows():
        keys = []
        if row['Codice_Fiscale']:
            keys.append(row['Codice_Fiscale'])
        if row['Partita_Iva']:
            keys.append(row['Partita_Iva'])
        info = {
            'Ragione_Sociale': row.get('Ragione_Sociale'),
            'Partita_Iva': str(row.get('Partita_Iva')).removesuffix(".0"),
            'Codice_Fiscale': row.get('Codice_Fiscale'),
            'Indirizzo_Spedizione': row.get('Indirizzo_Spedizione'),
            'Cap_Spedizione': str(row.get('Cap_Spedizione')),
            'Comune_Spedizione': row.get('Comune_Spedizione'),
            'Telefono_Soggetto': str(row.get('Telefono_Soggetto')).removesuffix(".0"),
            'Telefono_Secondario': str(row.get('Telefono_Secondario')).removesuffix(".0"),
            'Email_Soggetto': row.get('Email_Soggetto'),
            'Pec_Soggetto': row.get('Pec_Soggetto'),
            'Codice_Soggetto': str(row.get('Codice_Soggetto'))
        }
        aggiorna_soggetto(soggetti_dict, keys, info)

    for index, row in df2.iterrows():
        keys = []
        if row['Codice fiscale']:
            keys.append(row['Codice fiscale'])
        if row['Partita IVA']:
            keys.append(row['Partita IVA'])
        info = {
            'Ragione_Sociale': row.get('Nome 1'),
            'Partita_Iva': str(row.get('Partita IVA')).removesuffix(".0"),
            'Codice_Fiscale': row.get('Codice fiscale'),
            'Indirizzo_Spedizione': row.get('Ind. di fatturaz. - Via'),
            'Cap_Spedizione': str(row.get('Ind. di fatturaz. - CAP')),
            'Comune_Spedizione': row.get('Ind. di fatturaz. - Localit?'),
            'Telefono_Soggetto': str(row.get('Numero telefonico')).removesuffix(".0"),
            'Telefono_Secondario': str(row.get('Telefono 2')).removesuffix(".0"),
            'Email_Soggetto': row.get('Email'),
            'Pec_Soggetto': row.get('PEC'),
            'Codice_Soggetto': str(row.get('BPartner'))
        }
        aggiorna_soggetto(soggetti_dict, keys, info)

    for index, row in df3.iterrows():
        keys = []
        if row['Codice fiscale']:
            keys.append(row['Codice fiscale'])
        if row['Partita IVA']:
            keys.append(row['Partita IVA'])
        info = {
            'Ragione_Sociale': row.get('Ragione sociale'),
            'Partita_Iva': str(row.get('Partita IVA')).removesuffix(".0"),
            'Codice_Fiscale': row.get('Codice fiscale'),
            'Telefono_Soggetto': str(row.get('Telefono primario')).removesuffix(".0"),
            'Codice_Soggetto': str(row.get('Soggetto')),
            'Numero affido': row.get('Numero affido'),
            'Data affido': str(row.get('Data affido')),
            'Residuo ad oggi': row.get('Residuo ad oggi')
        }
        aggiorna_soggetto(soggetti_dict, keys, info)

    return soggetti_dict


# Funzione per ottenere i dati di tutti i soggetti
def ottieni_dati_tutti_soggetti(soggetti_dict):
    return soggetti_dict


# Nuova funzione per convertire i dati in CSV
def converti_in_csv(soggetti_dict):
    # Definizione delle colonne del CSV
    colonne = [
        'Codice', 'Denominazione', 'Nome', 'Cognome', 'Città', 'Cap', 'Regione', 'Provincia',
        'Nazione', 'Indirizzo', 'C.F.', 'Partita iva', 'Telefono', 'Cellulare', 'Tipologia',
        'Email', 'PEC', 'Annotazioni', 'Luogo di nascita', 'Data di nascita', 'Codice b2b',
        'Tipo identificazione', 'Tipo documento', 'Numero documento', 'Data rilascio',
        'Autorita rilascio', 'Autorita comune', 'Autorita provincia', 'Professione', 'Sesso',
        'Iva esente', 'Iban'
    ]

    # Creazione di una lista di dizionari per le righe del CSV
    righe_csv = []
    for key, soggetto in soggetti_dict.items():
        riga = {
            'Codice': soggetto.get('Codice_Soggetto', ''),
            'Denominazione': soggetto.get('Ragione_Sociale', ''),
            'Nome': '',
            'Cognome': '',
            'Città': soggetto.get('Comune_Spedizione', ''),
            'Cap': soggetto.get('Cap_Spedizione', ''),
            'Regione': '',
            'Provincia': '',
            'Nazione': 'Italia',  # Default value
            'Indirizzo': soggetto.get('Indirizzo_Spedizione', ''),
            'C.F.': soggetto.get('Codice_Fiscale', ''),
            'Partita iva': soggetto.get('Partita_Iva', ''),
            'Telefono': soggetto.get('Telefono_Soggetto', ''),
            'Cellulare': soggetto.get('Telefono_Secondario', ''),
            'Tipologia': 'Non specificata',  # Default value
            'Email': soggetto.get('Email_Soggetto', ''),
            'PEC': soggetto.get('Pec_Soggetto', ''),
            'Annotazioni': f"Numero affido: {soggetto.get('Numero affido', '')}",
            'Luogo di nascita': '',
            'Data di nascita': '',
            'Codice b2b': soggetto.get('Codice_Soggetto', ''),
            'Tipo identificazione': '',
            'Tipo documento': '',
            'Numero documento': '',
            'Data rilascio': '',
            'Autorita rilascio': '',
            'Autorita comune': '',
            'Autorita provincia': '',
            'Professione': '',
            'Sesso': '',
            'Iva esente': '',
            'Iban': ''
        }
        righe_csv.append(riga)

        #print(json.dumps(soggetto, indent=2))

    # Creazione del DataFrame
    df_csv = pd.DataFrame(righe_csv, columns=colonne)

    # Convertire il DataFrame in CSV e restituirlo come stringa
    return df_csv.to_csv(index=False, sep=';')


if __name__ == "__main__":
    # Esempio di utilizzo
    df1_path = '../input_data/EXCEL 1 ANAGRAFICHE.csv'
    df2_path = '../input_data/EXCEL 2 FATTURE.csv'
    df3_path = '../input_data/EXCEL 3 PRATICHE.xlsx'

    df1 = process_file(df1_path)
    df2 = process_file(df2_path)
    df3 = process_file(df3_path)

    soggetti_dict = genera_dizionario_soggetti(df1, df2, df3)

    # Ottenere i dati di tutti i soggetti
    dati_tutti_soggetti = ottieni_dati_tutti_soggetti(soggetti_dict)

    # Salva i dati in un file JSON
    with open('dati_tutti_soggetti.json', 'w', encoding='utf-8') as f:
        json.dump(dati_tutti_soggetti, f, ensure_ascii=False, indent=4)

    print("Dati di tutti i soggetti salvati in 'dati_tutti_soggetti.json'.")

    # Convertire i dati in un file CSV
    output_csv_path = 'dati_tutti_soggetti.csv'
    converti_in_csv(dati_tutti_soggetti)#, output_csv_path)

    print(f"Dati di tutti i soggetti salvati in '{output_csv_path}'.")
