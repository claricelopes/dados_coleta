import requests
from bs4 import BeautifulSoup
import time
import random

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

# Função para fazer scraping no Medium com tempo de espera

def buscar_artigos_medium(palavras_chave):
    artigos_encontrados = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    for palavra in palavras_chave:
        url = f"https://medium.com/search?q={palavra.replace(' ', '%20')}"
        print(f"Buscando artigos para: {palavra}")
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                artigos = soup.find_all('div', class_='postArticle')
                
                for artigo in artigos:
                    titulo_tag = artigo.find('h3')
                    titulo = titulo_tag.get_text() if titulo_tag else 'Sem título disponível'
                    
                    link_tag = artigo.find('a', {'href': True})
                    link = link_tag['href'] if link_tag else 'Sem link disponível'
                    
                    resumo_tag = artigo.find('p')
                    resumo = resumo_tag.get_text() if resumo_tag else 'Sem resumo disponível'
                    
                    artigos_encontrados.append({
                        'Título': titulo,
                        'Link': link,
                        'Resumo': resumo
                    })
            else:
                print(f"Erro ao acessar {url} - Código {response.status_code}")
        
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
        
        # Aguarda um tempo aleatório entre 5 e 15 segundos para evitar bloqueios
        tempo_espera = random.uniform(5, 15)
        print(f"Aguardando {tempo_espera:.2f} segundos antes da próxima busca...")
        time.sleep(tempo_espera)
        
    return artigos_encontrados

# Executando a busca
artigos = buscar_artigos_medium(palavras_chave)

# Exibindo os artigos encontrados
for artigo in artigos:
    print(f"Título: {artigo['Título']}")
    print(f"Link: {artigo['Link']}")
    print(f"Resumo: {artigo['Resumo']}")
    print("-" * 50)
