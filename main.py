from src.load_folder import load_documents_from_folder
from src.hash_text import get_hashed_shingles
from src.comparison import comparar_documentos, top_n_similares
from src.graphics import graficar_similitudes
from src.graph import create_interactive_graph

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

create_interactive_graph(similitudes)