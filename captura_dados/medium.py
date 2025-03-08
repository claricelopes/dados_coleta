import requests
from bs4 import BeautifulSoup

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

# Função para fazer scraping no Medium
def buscar_artigos_medium(palavras_chave):
    artigos_encontrados = []
    
    for palavra in palavras_chave:
        # URL de busca no Medium
        url = f"https://medium.com/search?q={palavra.replace(' ', '%20')}"
        
        # Fazendo a requisição para a URL
        response = requests.get(url)
        
        if response.status_code == 200:
            # Usando BeautifulSoup para analisar a página
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Encontrando os artigos na página
            artigos = soup.find_all('div', class_='postArticle')
            
            for artigo in artigos:
                # Extraindo o título, link e resumo
                titulo = artigo.find('h3')
                if titulo:
                    titulo = titulo.get_text()
                else:
                    titulo = 'Sem título disponível'
                
                # Buscando o link para o artigo
                link = artigo.find('a', {'href': True})
                if link:
                    link = link['href']
                else:
                    link = 'Sem link disponível'
                
                # Buscando o resumo do artigo
                resumo = artigo.find('p')
                if resumo:
                    resumo = resumo.get_text()
                else:
                    resumo = 'Sem resumo disponível'
                
                # Adicionando os dados do artigo à lista
                artigos_encontrados.append({
                    'Título': titulo,
                    'Link': link,
                    'Resumo': resumo
                })
        else:
            print(f"Erro ao acessar {url}")

    return artigos_encontrados

# Executando a busca
artigos = buscar_artigos_medium(palavras_chave)

# Exibindo os artigos encontrados
for artigo in artigos:
    print(f"Título: {artigo['Título']}")
    print(f"Link: {artigo['Link']}")
    print(f"Resumo: {artigo['Resumo']}")
    print("-" * 50)
