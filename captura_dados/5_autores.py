import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import networkx as nx

df = pd.read_csv('captura_dados/autores_todos.csv')

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

def top5_df(centralidade, nome):
    dados = sorted(centralidade.items(), key=lambda x: x[1], reverse=True)[:5]
    return pd.DataFrame(dados, columns=['Autor', 'Valor']).assign(Medida=nome)

df_centralidades = pd.concat([
    top5_df(centralidade_grau, 'Grau'),
    top5_df(centralidade_betweenness, 'Betweenness'),
    top5_df(centralidade_closeness, 'Closeness'),
    top5_df(centralidade_eigenvector, 'Eigenvector')
])

sns.set(style="whitegrid")
g = sns.catplot(
    data=df_centralidades,
    x='Valor', y='Autor',
    col='Medida',
    kind='bar',
    col_wrap=2,
    height=4, aspect=2,
    sharex=False
)

g.set_titles("{col_name} Centralidade")
g.set_axis_labels("Valor", "Autor")
for ax in g.axes.flat:
    ax.set_ylabel("Autor")
    ax.set_xlabel("Valor")
    ax.tick_params(axis='y', labelsize=9)

plt.tight_layout()
plt.show()
