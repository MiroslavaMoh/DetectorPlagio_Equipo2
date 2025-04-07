import os
import hashlib
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np

def graficar_similitudes(similitudes, docs):
    # Crear una matriz de similitudes vacía
    n_docs = len(docs)
    matriz_similitudes = np.zeros((n_docs, n_docs))

    # Mapear los nombres de los documentos a índices
    doc_to_index = {doc: i for i, doc in enumerate(docs)}

    # Rellenar la matriz de similitudes con los valores
    for (doc1, doc2), sim in similitudes:
        i = doc_to_index[doc1]
        j = doc_to_index[doc2]
        matriz_similitudes[i][j] = sim
        matriz_similitudes[j][i] = sim  # Dado que la similitud es simétrica

    # Graficar el mapa de calor
    plt.figure(figsize=(8, 6))
    plt.imshow(matriz_similitudes, cmap='hot', interpolation='nearest')
    plt.colorbar(label="Similitud")

    # Configurar etiquetas de los ejes
    plt.xticks(np.arange(n_docs), docs, rotation=90)
    plt.yticks(np.arange(n_docs), docs)
    
    # Título del gráfico
    plt.title("Similitudes entre documentos")
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.savefig("similitudes.png")  # Guarda el gráfico como un archivo PNG

def get_ngrams(text, n=3):
    words = text.split()
    return [' '.join(words[i:i+n]) for i in range(len(words) - n + 1)]

def hash_ngram(ngram):
    return hashlib.blake2b(ngram.encode('utf-8'), digest_size=4).hexdigest()

def load_documents_from_folder(folder_path):
    docs = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                docs[filename] = f.read()
    return docs

def get_hashed_shingles(text, n=3):
    ngrams = get_ngrams(text, n)
    return set(hash_ngram(ng) for ng in ngrams)

def jaccard_similarity(set1, set2):
    inter = len(set1 & set2)
    union = len(set1 | set2)
    return inter / union if union else 0

def comparar_documentos(docs_hashed):
    similitudes = []
    for (doc1, hash1), (doc2, hash2) in combinations(docs_hashed.items(), 2):
        sim = jaccard_similarity(hash1, hash2)
        similitudes.append(((doc1, doc2), sim))
    return similitudes

def top_n_similares(similitudes, N=5):
    # Ordena con Merge Sort (usamos sort() que es Timsort ≈ MergeSort en Python)
    similitudes.sort(key=lambda x: x[1], reverse=True)
    return similitudes[:N]

# ==== Main ====

carpeta = "./documentos/prueba_media"
n = 3  # tamaño de n-gramas
N_top = 50  # número de pares más similares

print("Cargando documentos...")
docs = load_documents_from_folder(carpeta)

print("Generando hashes...")
docs_hashed = {nombre: get_hashed_shingles(texto, n=n) for nombre, texto in docs.items()}

print("Comparando documentos...")
similitudes = comparar_documentos(docs_hashed)

print(f"\n🏆 Top {N_top} pares más similares:")
for (doc1, doc2), sim in top_n_similares(similitudes, N_top):
    if sim * 100 > 70:
        print(f"{doc1} vs {doc2} → \033[31m{sim * 100:.2f}% similares\033[0m")
    elif sim * 100 > 30:
        print(f"{doc1} vs {doc2} → \033[33m{sim * 100:.2f}% similares\033[0m")
    else:
        print(f"{doc1} vs {doc2} → \033[32m{sim * 100:.2f}% similares\033[0m")

# Llamar a la función para graficar
graficar_similitudes(similitudes, docs)