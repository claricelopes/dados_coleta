from scholarly import scholarly as sch

busca = "Centro de Informática UFPB"
resultados_busca = sch.search_pubs(busca)

for i in range(100): 
    artigo = next(resultados_busca)  
    print(f"Título: {artigo['bib']['title']}")
    print(f"Autores: {artigo['bib'].get('author', 'N/A')}")
    print(f"Ano: {artigo['bib'].get('pub_year', 'N/A')}")
    print(f"Link: {artigo.get('pub_url', 'Sem link disponível')}")
    print("-" * 50)
