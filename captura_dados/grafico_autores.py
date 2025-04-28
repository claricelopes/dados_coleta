import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('captura_dados/autores_todos.csv')

edges = []
for autores in df['Autores'].dropna():
    autores_list = [autor.strip() for autor in autores.split(';')]
    for i in range(len(autores_list)):
        for j in range(i + 1, len(autores_list)):
            edges.append((autores_list[i], autores_list[j]))

G = nx.Graph()
G.add_edges_from(edges)

degree_centrality = nx.degree_centrality(G)

top_30 = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:30]
top_30_nodes = set([autor for autor, centralidade in top_30])

G_top30 = G.subgraph(top_30_nodes)

plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G_top30,  k=1.0, seed=42)
nx.draw_networkx_nodes(G_top30, pos, node_color='skyblue', node_size=700)
nx.draw_networkx_edges(G_top30, pos, edge_color='gray')
nx.draw_networkx_labels(G_top30, pos, font_size=6, font_family='sans-serif')

plt.title('Rede de Coautoria - Top 30 Autores Mais Centrais', fontsize=16)
plt.axis('off')
plt.show()
