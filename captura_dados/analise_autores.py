import pandas as pd
import networkx as nx

df = pd.read_csv('captura_dados/autores_todos.csv')

coautores = []
for autores in df['Autores'].dropna():
    lista_autores = [a.strip() for a in autores.split(';')]
    for i in range(len(lista_autores)):
        for j in range(i + 1, len(lista_autores)):
            coautores.append((lista_autores[i], lista_autores[j]))

# Criar o grafo
G = nx.Graph()
G.add_edges_from(coautores)

# Calculando as centralidades
centralidade_grau = nx.degree_centrality(G)
centralidade_betweenness = nx.betweenness_centrality(G)
centralidade_closeness = nx.closeness_centrality(G)
centralidade_eigenvector = nx.eigenvector_centrality(G, max_iter=1000)

def mostrar_top10(centralidade, nome):
    top10 = sorted(centralidade.items(), key=lambda x: x[1], reverse=True)[:10]
    print(f"\nTop 10 - {nome}:")
    for autor, valor in top10:
        print(f"{autor}: {valor:.4f}")

mostrar_top10(centralidade_grau, 'Centralidade Grau')
mostrar_top10(centralidade_betweenness, 'Centralidade Betweenness')
mostrar_top10(centralidade_closeness, 'Centralidade Closeness')
mostrar_top10(centralidade_eigenvector, 'Centralidade Eigenvector')
