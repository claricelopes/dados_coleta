import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open('palavras_chave.csv', encoding='utf-8') as f:
    linhas = f.readlines()

linhas = linhas[1:]

palavras = []
frequencias = []

for linha in linhas:
    if ';' in linha:
        palavra, freq = linha.strip().split(';')
        palavras.append(palavra.strip())
        frequencias.append(int(freq.strip()))

frequencias_dict = dict(zip(palavras, frequencias))

wordcloud = WordCloud(width=1200, height=600, background_color='white',
                      colormap='viridis').generate_from_frequencies(frequencias_dict)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()