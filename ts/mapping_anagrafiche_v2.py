import json
import pandas as pd

# Funzione per processare i file caricati
def process_file(file_path):
    file_type = file_path.split('.')[-1]
    if file_type == 'csv':
        df = pd.read_csv(file_path, delimiter=';', on_bad_lines='skip').fillna('')
    elif file_type == 'xlsx':
        df = pd.read_excel(file_path).fillna('')
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
                'Email_Soggetto': '',
                'Pec_Soggetto': '',
                'Codice_Soggetto': '',
                'Numero affido': ''
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
            'Partita_Iva': row.get('Partita_Iva'),
            'Codice_Fiscale': row.get('Codice_Fiscale'),
            'Indirizzo_Spedizione': row.get('Indirizzo_Spedizione'),
            'Cap_Spedizione': row.get('Cap_Spedizione'),
            'Comune_Spedizione': row.get('Comune_Spedizione'),
            'Telefono_Soggetto': row.get('Telefono_Soggetto'),
            'Email_Soggetto': row.get('Email_Soggetto'),
            'Pec_Soggetto': row.get('Pec_Soggetto'),
            'Codice_Soggetto': row.get('Codice_Soggetto')
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
            'Partita_Iva': row.get('Partita IVA'),
            'Codice_Fiscale': row.get('Codice fiscale'),
            'Indirizzo_Spedizione': row.get('Ind. di fatturaz. - Via'),
            'Cap_Spedizione': row.get('Ind. di fatturaz. - CAP'),
            'Comune_Spedizione': row.get('Ind. di fatturaz. - Localit?'),
            'Telefono_Soggetto': row.get('Numero telefonico'),
            'Email_Soggetto': row.get('Email'),
            'Pec_Soggetto': row.get('PEC'),
            'Codice_Soggetto': row.get('BPartner')
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
            'Partita_Iva': row.get('Partita IVA'),
            'Codice_Fiscale': row.get('Codice fiscale'),
            'Telefono_Soggetto': row.get('Telefono primario'),
            'Codice_Soggetto': row.get('Soggetto'),
            'Numero affido': row.get('Numero affido')
        }
        aggiorna_soggetto(soggetti_dict, keys, info)

    return soggetti_dict

# Funzione per ottenere i dati di un soggetto unico
def ottieni_dati_soggetto(codice_fiscale_partita_iva, soggetti_dict):
    return soggetti_dict.get(codice_fiscale_partita_iva, {})

# Funzione per ottenere i dati di tutti i soggetti
def ottieni_dati_tutti_soggetti(soggetti_dict):
    return soggetti_dict

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
