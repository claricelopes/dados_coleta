import pandas as pd
import os

# Caminho onde estão os arquivos CSV
caminho_base = "C:/Users/vinic/dados_coleta"

# Lista com os nomes dos arquivos
nomes_arquivos = [
    "artigos_20250407_225939.csv",
    "artigos_20250407_230047.csv",
    "artigos_20250407_230120.csv",
    "artigos_20250407_230305.csv",
    "artigos_20250407_230323.csv",
    "artigos_20250407_230338.csv",
    "artigos_20250407_230357.csv",
    "artigomais.csv"
]

# Junta os caminhos completos
arquivos_csv = [os.path.join(caminho_base, nome) for nome in nomes_arquivos]

# Lê todos os CSVs da lista e concatena
dataframes = [pd.read_csv(arquivo) for arquivo in arquivos_csv]
df_concatenado = pd.concat(dataframes, ignore_index=True)

# Salva em um novo arquivo (também com caminho completo)
saida = os.path.join(caminho_base, "artigos_completo.csv")
df_concatenado.to_csv(saida, index=False)

print("✅ CSV final criado com sucesso:", saida)
