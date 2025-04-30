import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('autores_todos.csv')

coautores = []
for autores in df['Autores'].dropna():
    lista_autores = [a.strip() for a in autores.split(';')]
    for i in range(len(lista_autores)):
        for j in range(i + 1, len(lista_autores)):
            coautores.append((lista_autores[i], lista_autores[j]))

G = nx.Graph()
G.add_edges_from(coautores)

centralidade_grau = nx.degree_centrality(G)
centralidade_betweenness = nx.betweenness_centrality(G)
centralidade_closeness = nx.closeness_centrality(G)
centralidade_eigenvector = nx.eigenvector_centrality(G, max_iter=1000)

df_centralidade = pd.DataFrame({
    'Autor': list(centralidade_grau.keys()),
    'Grau': list(centralidade_grau.values()),
    'Betweenness': list(centralidade_betweenness.values()),
    'Closeness': list(centralidade_closeness.values()),
    'Eigenvector': list(centralidade_eigenvector.values())
})

plt.figure(figsize=(14, 10))
num_nos = G.number_of_nodes()
print("Número de nós:", num_nos)

plt.subplot(2, 2, 1)
sns.histplot(df_centralidade['Grau'], kde=True, bins=30, color='skyblue')
plt.title('Centralidade de Grau')

plt.subplot(2, 2, 2)
sns.histplot(df_centralidade['Betweenness'], kde=True, bins=30, color='salmon')
plt.title('Centralidade de Betweenness')

plt.subplot(2, 2, 3)
sns.histplot(df_centralidade['Closeness'], kde=True, bins=30, color='seagreen')
plt.title('Centralidade de Closeness')

plt.subplot(2, 2, 4)
sns.histplot(df_centralidade['Eigenvector'], kde=True, bins=30, color='gold')
plt.title('Centralidade de Eigenvector')

plt.tight_layout()
plt.show()
