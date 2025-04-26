import pandas as pd
#numero de artigos de cada professor
nome_arquivo_artigos = 'artigos_20250407_230338.csv'  # Atualizar

df = pd.read_csv(nome_arquivo_artigos)

todos_os_professores = df['Professor'].unique()

df_validos = df[df['Artigo'] != 'Nenhuma publicação encontrada']

contagem = df_validos['Professor'].value_counts().reset_index()
contagem.columns = ['Professor', 'Quantidade de Artigos']

df_todos = pd.DataFrame({'Professor': todos_os_professores})
df_final = pd.merge(df_todos, contagem, on='Professor', how='left').fillna(0)

df_final['Quantidade de Artigos'] = df_final['Quantidade de Artigos'].astype(int)

print(df_final)

df_final.to_csv('quantidade_artigos_por_professor.csv', index=False, encoding='utf-8')
