import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import math

def create_interactive_graph(similitudes):
    # Crear un grafo con NetworkX
    G = nx.Graph()

    # Contar la cantidad de similitudes por porcentaje
    similarity_counts = {}
    for (doc1, doc2), sim in similitudes:
        percentage = round(sim * 100)
        if percentage not in similarity_counts:
            similarity_counts[percentage] = []
        similarity_counts[percentage].append((doc1, doc2))

    # Agregar nodos al grafo
    for percentage, pairs in similarity_counts.items():
        G.add_node(percentage, size=len(pairs), pairs=pairs)

    # Agregar conexiones (edges) entre nodos
    percentages = list(similarity_counts.keys())
    for i in range(len(percentages)):
        for j in range(i + 1, len(percentages)):
            G.add_edge(percentages[i], percentages[j])

    # Crear una figura de Matplotlib
    fig, ax = plt.subplots(figsize=(10, 8))

    # Dibujar el grafo con mejoras visuales
    pos = nx.spring_layout(G, seed=42)  # Usa una disposición reproducible
    sizes = [G.nodes[node]['size'] * 20 for node in G.nodes]  # Escala ajustada
    colors = [node for node in G.nodes]  # Colores basados en los valores de los nodos
    cmap = plt.cm.viridis  # Mapa de colores atractivo

    nx.draw(
        G,
        pos,
        with_labels=True,
        ax=ax,
        node_size=sizes,
        node_color=colors,
        cmap=cmap,
        font_size=10,
        font_color="white",
        edge_color="lightgray",
        linewidths=1.5,
    )

    # Función para manejar clics en los nodos
    def on_click(event):
        if event.inaxes == ax:
            for node, (x, y) in pos.items():
                if (event.xdata - x) ** 2 + (event.ydata - y) ** 2 < 0.01:
                    pairs = G.nodes[node]['pairs']
                    show_details_window(node, pairs)
                    return

    # Función para mostrar detalles en una nueva ventana de Matplotlib
    def show_details_window(node, pairs):
        details_fig, details_ax = plt.subplots(figsize=(10, 6))
        details_ax.axis("off")
        details_ax.set_title(f"Detalles del Nodo: {node}%", fontsize=14)

        # Dividir las similitudes en tres columnas
        column_count = 3
        rows = math.ceil(len(pairs) / column_count)
        col1 = pairs[:rows]
        col2 = pairs[rows:2 * rows]
        col3 = pairs[2 * rows:]

        # Crear el texto para las tres columnas
        col1_text = "\n".join([f"{doc1} vs {doc2}" for doc1, doc2 in col1])
        col2_text = "\n".join([f"{doc1} vs {doc2}" for doc1, doc2 in col2])
        col3_text = "\n".join([f"{doc1} vs {doc2}" for doc1, doc2 in col3])

        # Mostrar las columnas en la ventana
        details_ax.text(0.2, 0.5, col1_text, ha="center", va="center", fontsize=8, wrap=True)
        details_ax.text(0.5, 0.5, col2_text, ha="center", va="center", fontsize=8, wrap=True)
        details_ax.text(0.8, 0.5, col3_text, ha="center", va="center", fontsize=8, wrap=True)

        plt.show()

    # Conectar el evento de clic
    fig.canvas.mpl_connect("button_press_event", on_click)

    # Mostrar el grafo
    plt.show()