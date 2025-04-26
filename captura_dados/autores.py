import csv
import os
#autores que trabalharam juntos
def extrair_autores(caminho_arquivo):
    grupos_autores = []

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        
        for i in range(len(linhas)):
            if '02: autores' in linhas[i].lower():
                if i + 1 < len(linhas):
                    linha_autores = linhas[i + 1].strip()
                    autores = [a.strip() for a in linha_autores.split(',') if a.strip()]
                    if autores:
                        grupos_autores.append(autores)
    return grupos_autores

caminho_arquivo_atual = 'resultados/resultado_20250321_202721.csv' # Atualizar

caminho_saida_acumulado = 'autores_todos.csv'

autores_atuais = extrair_autores(caminho_arquivo_atual)

arquivo_existe = os.path.exists(caminho_saida_acumulado)

with open(caminho_saida_acumulado, mode='a', newline='', encoding='utf-8') as arquivo_saida:
    escritor = csv.writer(arquivo_saida)
    if not arquivo_existe:
        escritor.writerow(['Artigo', 'Autores'])
    indice_inicial = sum(1 for _ in open(caminho_saida_acumulado, encoding='utf-8')) if arquivo_existe else 1
    for i, grupo in enumerate(autores_atuais, start=indice_inicial):
        escritor.writerow([i, '; '.join(grupo)])

caminho_saida_acumulado
