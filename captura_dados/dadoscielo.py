import requests
import time
import random
import csv

# Nome do arquivo CSV
arquivo_csv = "dados_coletados.csv"

# URL base da API CrossRef
url_base = "https://api.crossref.org/works"

# Lista de palavras-chave relacionadas ao CI da UFPB
palavras_chave = [
    "Centro de Informática UFPB", "Center for Informatics UFPB", 
    "Computação UFPB", "Computer Science UFPB", 
    "Inteligência Artificial UFPB", "Artificial Intelligence UFPB", 
    "Ciência de Dados UFPB", "Data Science UFPB", 
    "Machine Learning UFPB", "Visão Computacional UFPB", 
    "Computer Vision UFPB", "Processamento de Linguagem Natural UFPB", 
    "Natural Language Processing UFPB", "Engenharia de Software UFPB", 
    "Software Engineering UFPB", "Desenvolvimento de Software UFPB", 
]

# Número máximo de artigos por busca (limite da API CrossRef é 100)
max_artigos = 100  

# Quantidade máxima de tentativas em caso de erro
max_tentativas = 3  

# Criar e inicializar o arquivo CSV com cabeçalho
with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Título", "Ano", "Autores", "Link"])

# Percorre cada palavra-chave e realiza a busca
for palavra in palavras_chave:
    print(f"\n🔎 Buscando artigos para: {palavra}")
    
    parametros = {"query": palavra, "rows": max_artigos}
    tentativa = 0
    sucesso = False
    
    while tentativa < max_tentativas and not sucesso:
        try:
            resposta = requests.get(url_base, params=parametros, timeout=20)
            
            if resposta.status_code == 200:
                dados = resposta.json()
                
                if "message" in dados and "items" in dados["message"]:
                    artigos = dados["message"]["items"]
                    
                    with open(arquivo_csv, mode="a", newline="", encoding="utf-8") as arquivo:
                        escritor = csv.writer(arquivo)
                        
                        for artigo in artigos:
                            titulo = artigo.get("title", ["Sem título"])[0]
                            link = artigo.get("URL", "Sem link disponível")
                            autores = artigo.get("author", [])
                            ano = artigo.get("published-print", {}).get("date-parts", [[None]])[0][0] or \
                                  artigo.get("published-online", {}).get("date-parts", [[None]])[0][0]
                            
                            nomes_autores = [f"{autor.get('given', '')} {autor.get('family', '')}".strip() for autor in autores if autor.get('given') or autor.get('family')]
                            
                            for autor in autores:
                                if "affiliation" in autor:
                                    for afiliacao in autor["affiliation"]:
                                        if "UFPB" in afiliacao.get("name", ""):
                                            escritor.writerow([titulo, ano if ano else "Desconhecido", ", ".join(nomes_autores) if nomes_autores else "Desconhecido", link])
                                            break
                    sucesso = True
                else:
                    print("Resposta inesperada da API.")
                    tentativa += 1
            else:
                print(f"Erro ao acessar a API: {resposta.status_code}")
                tentativa += 1
        
        except requests.exceptions.RequestException as erro:
            print(f"Erro na requisição: {erro}")
            tentativa += 1
        
        if not sucesso and tentativa < max_tentativas:
            tempo_espera = round(random.uniform(10, 30), 2)
            print(f"Tentativa falhou. Tentando novamente em {tempo_espera} segundos...\n")
            time.sleep(tempo_espera)
    
    tempo_espera = round(random.uniform(20, 40), 2)
    print(f"Aguardando {tempo_espera} segundos antes da próxima busca...\n")
    time.sleep(tempo_espera)
