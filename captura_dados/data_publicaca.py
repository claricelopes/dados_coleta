import csv
import os

arquivo_saida = 'datas_publicacao.csv'

if not os.path.exists(arquivo_saida):
    with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Data de Publicação'])

def extrair_datas(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        
        for i in range(len(linhas)):
            if linhas[i].strip() == '03: Data de publicação':
                if i + 1 < len(linhas):
                    data_publicacao = linhas[i+1].strip()
                    with open(arquivo_saida, mode='a', newline='', encoding='utf-8') as f_out:
                        writer = csv.writer(f_out)
                        writer.writerow([data_publicacao])
                    print(f'Data adicionada: {data_publicacao}')

import glob

arquivos = glob.glob('resultados/resultado_20250321_202721.csv') # Atualizar

for arquivo in arquivos:
    extrair_datas(arquivo)

print('Processamento concluído!')
