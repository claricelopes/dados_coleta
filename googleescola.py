from scholarly import scholarly as sch

# Adicionando termos em inglês na busca
busca = "Centro de Informática UFPB OR 'Center for Informatics UFPB'"
resultados_busca = sch.search_pubs(busca)

for i in range(100): 
    try:
        artigo = next(resultados_busca)
        titulo = artigo['bib']['title']
        autores = artigo['bib'].get('author', 'N/A')
        ano = artigo['bib'].get('pub_year', 'N/A')
        link = artigo.get('pub_url', 'Sem link disponível')

        print(f"Título: {titulo}")
        print(f"Autores: {autores}")
        print(f"Ano: {ano}")
        print(f"Link: {link}")
        print("-" * 50)
    
    except StopIteration:
        print("Sem mais resultados disponíveis.")
        break
