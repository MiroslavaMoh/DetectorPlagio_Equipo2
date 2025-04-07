from itertools import combinations


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

