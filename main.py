import xml.etree.ElementTree as ET
import pandas as pd
import os

def xml_to_dict(xml_file):
    """
    Converte un singolo file XML nel formato fornito in un dizionario.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = {}
    for child in root:
        for grandchild in child:
            tag_name = grandchild.tag
            text = grandchild.text if grandchild.text else ''
            data[tag_name] = text  # Sovrascrive se il tag appare più volte
    return data

def process_xml_files(directory, output_excel_file="output.xlsx"):
    """
    Elabora tutti i file XML nella directory specificata e crea un unico file Excel.
    """
    all_data = []
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            filepath = os.path.join(directory, filename)
            try:
                data = xml_to_dict(filepath)
                all_data.append(data)
            except Exception as e:
                print(f"Errore durante l'elaborazione di '{filename}': {e}")

    if all_data:
        df = pd.DataFrame(all_data)
        try:
            df.to_excel(output_excel_file, index=False)
            print(f"File '{output_excel_file}' creato con successo.")
        except Exception as e:
            print(f"Errore durante la scrittura del file Excel: {e}")
    else:
        print("Nessun file XML trovato o elaborato correttamente.")


folder_path = "./data/cifa"  # or replace with your actual folder path

# Esegui la funzione per elaborare i file XML nella directory corrente
process_xml_files(folder_path)

# Per specificare un nome diverso per il file excel:
# process_xml_files(folder_path, output_excel_file="nome_file_output.xlsx")