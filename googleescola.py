import csv
import time
from scholarly import scholarly as sch

# Nome do arquivo CSV
arquivo_csv = "dados_coletados.csv"

# Adicionando termos de pesquisa
busca = ("Centro de Informática UFPB OR 'Center for Informatics UFPB' OR "
         "'Computação UFPB' OR 'Computer Science UFPB' OR "
         " 'Inteligência Artificial e Ciência de Dados' OR 'Artificial Intelligence UFPB' OR "
         "'Aprendizado de Máquina UFPB' OR 'Machine Learning UFPB' OR "
         "'Ciência de Dados UFPB' OR 'Data Science UFPB' OR "
         "'Visão Computacional UFPB' OR 'Computer Vision UFPB' OR "
         "'Processamento de Linguagem Natural UFPB' OR 'Natural Language Processing UFPB' OR "
         " 'Engenharia de Software e Sistemas' OR 'Software Engineering UFPB' OR "
         "'Desenvolvimento de Software UFPB' OR 'Software Development UFPB' OR "
         "'Arquitetura de Software UFPB' OR 'Software Architecture UFPB' OR "
         "'Sistemas Distribuídos UFPB' OR 'Distributed Systems UFPB' OR "
         " 'Redes e Segurança da Informação' OR 'Information Security UFPB' OR "
         "'Criptografia UFPB' OR 'Cryptography UFPB' OR "
         "'Redes de Computadores UFPB' OR 'Computer Networks UFPB' OR "
         "'Computação em Nuvem UFPB' OR 'Cloud Computing UFPB' OR "
         " 'Computação Gráfica e Interação Humano-Computador' OR 'Computer Graphics UFPB' OR "
         "'Interação Humano-Computador UFPB' OR 'Human-Computer Interaction UFPB' OR "
         "'Realidade Virtual UFPB' OR 'Virtual Reality UFPB' OR "
         "'Realidade Aumentada UFPB' OR 'Augmented Reality UFPB' OR "
         " 'Outras áreas' OR 'Computação Quântica UFPB' OR 'Quantum Computing UFPB' OR "
         "'Otimização UFPB' OR 'Optimization UFPB' OR "
         "'Computação Paralela UFPB' OR 'Parallel Computing UFPB'")

# Inicializando a busca
resultados_busca = sch.search_pubs(busca)

# Criando e abrindo o arquivo CSV para escrita
with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Título", "Autores", "Ano", "Link"])
    
    while True:
        try:
            # Pegando próximo artigo
            artigo = next(resultados_busca)
            titulo = artigo['bib']['title']
            autores = artigo['bib'].get('author', 'N/A')
            ano = artigo['bib'].get('pub_year', 'N/A')
            link = artigo.get('pub_url', 'Sem link disponível')
            
            # Escrevendo no CSV
            writer.writerow([titulo, autores, ano, link])
            
            # Exibindo no terminal
            print(f"Título: {titulo}")
            print(f"Autores: {autores}")
            print(f"Ano: {ano}")
            print(f"Link: {link}")
            print("-" * 50)
            
            # Tempo de espera para evitar bloqueios
            time.sleep(2)
            
        except StopIteration:
            print("Sem mais resultados disponíveis.")
            break

print(f"Coleta finalizada. Dados salvos em {arquivo_csv}")