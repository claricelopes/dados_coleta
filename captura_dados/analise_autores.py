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

# Criar o grafo
G = nx.Graph()
G.add_edges_from(coautores)

centralidade_grau = nx.degree_centrality(G)
centralidade_betweenness = nx.betweenness_centrality(G)
centralidade_closeness = nx.closeness_centrality(G)
centralidade_eigenvector = nx.eigenvector_centrality(G, max_iter=1000)

def mostrar_top10(centralidade, nome):
    top10 = sorted(centralidade.items(), key=lambda x: x[1], reverse=True)[:10]
    print(f"\nTop 10 - {nome}:")
    for autor, valor in top10:
        print(f"{autor}: {valor:.4f}")

def criar_dataframe_top10(centralidade, nome_medida):
    top10 = sorted(centralidade.items(), key=lambda x: x[1], reverse=True)[:10]
    df = pd.DataFrame(top10, columns=['Autor', 'Valor'])
    df['Centralidade'] = nome_medida
    return df

mostrar_top10(centralidade_grau, 'Centralidade Grau')
mostrar_top10(centralidade_betweenness, 'Centralidade Betweenness')
mostrar_top10(centralidade_closeness, 'Centralidade Closeness')
mostrar_top10(centralidade_eigenvector, 'Centralidade Eigenvector')

df_grau = criar_dataframe_top10(centralidade_grau, 'Grau')
df_betweenness = criar_dataframe_top10(centralidade_betweenness, 'Betweenness')
df_closeness = criar_dataframe_top10(centralidade_closeness, 'Closeness')
df_eigenvector = criar_dataframe_top10(centralidade_eigenvector, 'Eigenvector')

df_top10 = pd.concat([df_grau, df_betweenness, df_closeness, df_eigenvector])

plt.figure(figsize=(14,8))
sns.barplot(data=df_top10, x='Valor', y='Autor', hue='Centralidade', dodge=True, palette='viridis')

plt.title('Comparação Top 10 Autores por Medidas de Centralidade', fontsize=16)
plt.xlabel('Valor da Centralidade', fontsize=14)
plt.ylabel('Autor', fontsize=14)
plt.legend(title='Medida de Centralidade')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
