import requests
import time
import random

# URL base da API CrossRef
base_url = "https://api.crossref.org/works"

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
    "Arquitetura de Software UFPB", "Software Architecture UFPB", 
    "Sistemas Distribuídos UFPB", "Distributed Systems UFPB", 
    "Segurança da Informação UFPB", "Information Security UFPB", 
    "Criptografia UFPB", "Cryptography UFPB", "Redes de Computadores UFPB", 
    "Computer Networks UFPB", "Computação em Nuvem UFPB", "Cloud Computing UFPB",
    "Computação Gráfica UFPB", "Computer Graphics UFPB", 
    "Interação Humano-Computador UFPB", "Human-Computer Interaction UFPB",
    "Realidade Virtual UFPB", "Virtual Reality UFPB", 
    "Realidade Aumentada UFPB", "Augmented Reality UFPB", 
    "Computação Quântica UFPB", "Quantum Computing UFPB", 
    "Otimização UFPB", "Optimization UFPB", 
    "Computação Paralela UFPB", "Parallel Computing UFPB"
]

# Número máximo de artigos por busca (limite da API CrossRef é 100)
num_artigos = 100  

# Quantidade máxima de tentativas em caso de erro
max_tentativas = 3  

# Percorre cada palavra-chave e realiza a busca
for palavra in palavras_chave:
    print(f"\n🔎 Buscando artigos para: {palavra}")
    
    # Define os parâmetros da busca
    params = {"query": palavra, "rows": num_artigos}
    
    tentativa = 0
    sucesso = False
    
    while tentativa < max_tentativas and not sucesso:
        try:
            # Faz a requisição GET
            response = requests.get(base_url, params=params, timeout=20)
            
            if response.status_code == 200:
                data = response.json()
                
                if "message" in data and "items" in data["message"]:
                    articles = data["message"]["items"]
                    
                    # Filtrar apenas os artigos que mencionam "UFPB"
                    artigos_ufpb = []
                    for article in articles:
                        title = article.get("title", ["Sem título"])[0]
                        link = article.get("URL", "Sem link disponível")
                        authors = article.get("author", [])

                        # Verifica se algum autor tem afiliação com "UFPB"
                        for author in authors:
                            if "affiliation" in author:
                                for aff in author["affiliation"]:
                                    if "UFPB" in aff.get("name", ""):
                                        artigos_ufpb.append((title, link))
                                        break
                    
                    # Exibe os resultados filtrados
                    if artigos_ufpb:
                        for title, link in artigos_ufpb:
                            print(f"Título: {title}")
                            print(f"Link: {link}")
                            print("-" * 50)
                    else:
                        print("Nenhum artigo da UFPB encontrado.")

                    sucesso = True  # Sai do loop de tentativas

                else:
                    print("Resposta inesperada da API.")
                    tentativa += 1
            else:
                print(f"Erro ao acessar a API: {response.status_code}")
                tentativa += 1

        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            tentativa += 1
        
        # Se a tentativa falhou, espera antes de tentar novamente
        if not sucesso and tentativa < max_tentativas:
            tempo_espera = round(random.uniform(10, 30), 2)
            print(f"Tentativa falhou. Tentando novamente em {tempo_espera} segundos...\n")
            time.sleep(tempo_espera)

    # Aguarda entre 20 e 40 segundos antes da próxima palavra-chave
    tempo_espera = round(random.uniform(20, 40), 2)
    print(f"Aguardando {tempo_espera} segundos antes da próxima busca...\n")
    time.sleep(tempo_espera)
