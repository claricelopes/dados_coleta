import pandas as pd
import itertools
# gera os pares de autores que ja trabalharam juntos
df = pd.read_csv('autores_todos.csv')

colaboracoes = []

for autores_str in df['Autores']:
    autores = [a.strip() for a in autores_str.split(';') if a.strip()]
    for par in itertools.combinations(autores, 2):
        colaboracoes.append(par)

df_colaboracoes = pd.DataFrame(colaboracoes, columns=['Source', 'Target'])

df_colaboracoes.to_csv('autores_colaboracoes_para_gephi.csv', index=False)
