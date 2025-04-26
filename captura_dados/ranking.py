import pandas as pd
import re
#professores que mais publicaram
with open('analise.txt', 'r', encoding='utf-8') as file: # Atualizar
    linhas = file.readlines()

dados = []

padrao = re.compile(r'^\s*\d+\s+(.*?)\s+(\d+)\s*$')

for linha in linhas:
    match = padrao.match(linha)
    if match:
        nome = match.group(1).strip()
        quantidade = int(match.group(2))
        dados.append({"Professor": nome, "Quantidade de Artigos": quantidade})

df = pd.DataFrame(dados)

ranking = df.sort_values(by="Quantidade de Artigos", ascending=False).head(10)

print("Top 10 Professores com mais publicações:")
print(ranking.reset_index(drop=True))
