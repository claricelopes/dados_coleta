import pandas as pd
import matplotlib.pyplot as plt
#plota grafico com anos das publicacoes
df = pd.read_csv('anos_publicacao.csv')

contagem_anos = df['Ano'].value_counts().sort_index()

plt.figure(figsize=(12,6))
contagem_anos.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Número de Publicações por Ano', fontsize=16)
plt.xlabel('Ano', fontsize=14)
plt.ylabel('Quantidade de Publicações', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
