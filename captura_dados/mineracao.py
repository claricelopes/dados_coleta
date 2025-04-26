import pandas as pd
import datetime
# nome do professor e nome de cada artigo
caminho_arquivo = 'resultados/resultado_20250321_202721.csv' # Atualizar

with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    linhas = f.readlines()

dados = []
professor_atual = None
coletando_artigos = False

for linha in linhas:
    linha = linha.strip()

    if linha.startswith("Professor Pesquisado:"):
        professor_atual = linha.replace("Professor Pesquisado:", "").strip()
        coletando_artigos = True

    elif linha.startswith("Resposta: Nome não encontrado"):
        dados.append({
            'Professor': professor_atual,
            'Artigo': 'Nenhuma publicação encontrada'
        })
        coletando_artigos = False

    elif coletando_artigos and "1:" in linha:
        titulo_artigo = linha.split("1:", 1)[1].strip()
        dados.append({
            'Professor': professor_atual,
            'Artigo': titulo_artigo
        })

df = pd.DataFrame(dados)

print(df.head(20))

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

nome_arquivo = f"artigos_{timestamp}.csv"

df.to_csv(nome_arquivo, index=False, encoding='utf-8')
