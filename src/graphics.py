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
    plt.savefig("resultados/similitudes.png")  # Guarda el gráfico como un archivo PNG
