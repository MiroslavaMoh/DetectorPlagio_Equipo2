"""
Archivo el cual extrae los archivos.txt a partir de la carpeta documentos (en variable path), 
se puede modificar para escoger una subcarpeta en su lugar.

"""
import os

def load_documents_from_folder(folder_path):
    docs = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                docs[filename] = f.read()
    return docs


carpeta = "./documentos/prueba_media"