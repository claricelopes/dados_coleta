import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('pares_autores.csv')

G = nx.Graph()
for index, row in df.iterrows():
    G.add_edge(row['Source'], row['Target'])

num_componentes = nx.number_connected_components(G)
print(f"Número de componentes conectados: {num_componentes}")

maior_componente = max(nx.connected_components(G), key=len)
print(f"Tamanho da maior componente: {len(maior_componente)}")

clustering_medio = nx.average_clustering(G)
print(f"Coeficiente de agrupamento médio: {clustering_medio:.2f}")

grau_medio = sum(dict(G.degree()).values()) / G.number_of_nodes()
print(f"Grau médio: {grau_medio:.2f}")

import matplotlib.pyplot as plt

graus = [grau for _, grau in G.degree()]

plt.figure(figsize=(10,6))
plt.hist(graus, bins=30, color='skyblue', edgecolor='black')
plt.title('Distribuição do Grau de Conexões entre Pesquisadores')
plt.xlabel('Número de Colaborações (Grau)')
plt.ylabel('Número de Pesquisadores')
plt.grid(True)
plt.show()
