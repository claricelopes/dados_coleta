from scholarly import scholarly as sch

# Adicionando termos de pesquisa
busca = ("Centro de Informática UFPB OR 'Center for Informatics UFPB' OR "
         "'Computação UFPB' OR 'Computer Science UFPB' OR "
         "🧠 'Inteligência Artificial e Ciência de Dados' OR 'Artificial Intelligence UFPB' OR "
         "'Aprendizado de Máquina UFPB' OR 'Machine Learning UFPB' OR "
         "'Ciência de Dados UFPB' OR 'Data Science UFPB' OR "
         "'Visão Computacional UFPB' OR 'Computer Vision UFPB' OR "
         "'Processamento de Linguagem Natural UFPB' OR 'Natural Language Processing UFPB' OR "
         "💻 'Engenharia de Software e Sistemas' OR 'Software Engineering UFPB' OR "
         "'Desenvolvimento de Software UFPB' OR 'Software Development UFPB' OR "
         "'Arquitetura de Software UFPB' OR 'Software Architecture UFPB' OR "
         "'Sistemas Distribuídos UFPB' OR 'Distributed Systems UFPB' OR "
         "🖥️ 'Redes e Segurança da Informação' OR 'Information Security UFPB' OR "
         "'Criptografia UFPB' OR 'Cryptography UFPB' OR "
         "'Redes de Computadores UFPB' OR 'Computer Networks UFPB' OR "
         "'Computação em Nuvem UFPB' OR 'Cloud Computing UFPB' OR "
         "📊 'Computação Gráfica e Interação Humano-Computador' OR 'Computer Graphics UFPB' OR "
         "'Interação Humano-Computador UFPB' OR 'Human-Computer Interaction UFPB' OR "
         "'Realidade Virtual UFPB' OR 'Virtual Reality UFPB' OR "
         "'Realidade Aumentada UFPB' OR 'Augmented Reality UFPB' OR "
         "🎛️ 'Outras áreas' OR 'Computação Quântica UFPB' OR 'Quantum Computing UFPB' OR "
         "'Otimização UFPB' OR 'Optimization UFPB' OR "
         "'Computação Paralela UFPB' OR 'Parallel Computing UFPB'")

resultados_busca = sch.search_pubs(busca)

with open("resultados/googleescola.txt", "w", encoding="utf-8") as arquivo:
    for i in range(100): 
        try:
            artigo = next(resultados_busca)
            titulo = artigo['bib']['title']
            autores = artigo['bib'].get('author', 'N/A')
            ano = artigo['bib'].get('pub_year', 'N/A')
            link = artigo.get('pub_url', 'Sem link disponível')

            resultado = (f"Título: {titulo}\n"
                         f"Autores: {autores}\n"
                         f"Ano: {ano}\n"
                         f"Link: {link}\n"
                         f"{'-' * 50}\n")
            arquivo.write(resultado)

        except StopIteration:
            print("Sem mais resultados disponíveis.")
            break
