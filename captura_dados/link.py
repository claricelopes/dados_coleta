import pandas as pd

df = pd.read_csv('captura_dados/autores_todos.csv', header=None, names=['Artigo', 'Autores'])

print(df.head())

def obter_coautores(autores_str):
    autores = autores_str.split(';')
    autores = [autor.strip() for autor in autores]
    coautores = []
    for i in range(len(autores)):
        for j in range(i + 1, len(autores)):
            coautores.append(tuple(sorted([autores[i], autores[j]])))
    return coautores

df['Coautores'] = df['Autores'].apply(obter_coautores)

print(df[['Artigo', 'Coautores']].head())

import networkx as nx

# Criar o grafo
G = nx.Graph()

for coautores in df['Coautores']:
    G.add_edges_from(coautores)

print(list(G.edges())[:10])

componentes_conectadas = list(nx.connected_components(G))

print([len(component) for component in componentes_conectadas])

centralidade = nx.degree_centrality(G)

top_10_autores = sorted(centralidade.items(), key=lambda x: x[1], reverse=True)[:10]
print(top_10_autores)
