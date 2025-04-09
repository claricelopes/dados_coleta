import csv
import re
from collections import Counter

stopwords = set([
    'de', 'da', 'do', 'e', 'a', 'o', 'em', 'com', 'para', 'por', 'na', 'no',
    'das', 'dos', 'as', 'os', 'uma', 'um', 'sobre', 'que', 'se', 'entre', 
    'for', 'of', 'in', 'the', 'and', 'to', 'an', 'on', 'with'
])

arquivo_csv = 'artigos_20250407_225939.csv'

titulos = []

with open(arquivo_csv, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        titulo = row['Artigo'].strip()
        if titulo.lower() != 'nenhuma publicação encontrada':
            titulos.append(titulo.lower())

texto = ' '.join(titulos)

texto = re.sub(r'[^\w\s]', '', texto)

palavras = texto.split()

palavras_filtradas = [p for p in palavras if p not in stopwords]

contagem = Counter(palavras_filtradas)

print("Top 20 palavras mais frequentes nos títulos:")
for palavra, frequencia in contagem.most_common(20):
    print(f"{palavra}: {frequencia}")
