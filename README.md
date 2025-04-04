~Detector de Plagio con Tablas Hash y Similitud de Jaccard
Este repositorio contiene un proyecto de detector de plagio diseñado para analizar archivos de texto de gran tamaño y cantidad. El sistema se basa en las siguientes tecnologías y principios:

🔍 ¿Cómo funciona?
    >Se utiliza la similitud de Jaccard para comparar el contenido de los textos y medir el grado de similitud entre ellos.

    >Los datos se almacenan y gestionan mediante tablas hash, permitiendo un acceso rápido y eficiente durante la comparación.

    >Para mejorar el rendimiento y reducir el uso de memoria, especialmente en conjuntos de datos grandes, se integran técnicas basadas en Bloom Filters.

📊 Procesamiento y visualización
    >Una vez calculadas las similitudes, los resultados se ordenan según su nivel de autenticidad utilizando el algoritmo de Merge Sort.

    >Para facilitar el análisis, los resultados más relevantes (es decir, los archivos que presentan mayor similitud entre sí) se visualizan mediante grafos.

    >Solo se muestran un número definido de comparaciones, enfocándose en aquellas que presentan mayor similitud, facilitando la detección de posibles plagios.