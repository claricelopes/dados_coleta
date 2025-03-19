import time
from scholarly import scholarly
from nomes_professores import obter_nomes_professores

# Obtendo a lista de professores
professores = obter_nomes_professores()

def buscar_artigos(professor):
    print(f"\n🔍 Buscando artigos de {professor}...")

    search_query = scholarly.search_author(professor)
    try:
        while True:
            author = next(search_query)  # Pega o próximo autor encontrado
            
            # Verifica se o autor é da UFPB
            if "UFPB" in author.get('affiliation', ''):
                author_filled = scholarly.fill(author, sections=["publications"])
                artigos = [
                    (pub['bib']['title'], pub['bib'].get('year', 'Ano desconhecido'))
                    for pub in author_filled.get('publications', [])
                ]

                if artigos:
                    print(f"✅ Artigos de {professor} (UFPB):")
                    for titulo, ano in artigos:
                        print(f"   - {titulo} ({ano})")
                else:
                    print(f"⚠️ Nenhum artigo encontrado para {professor}.")
                break  # Sai do loop ao encontrar um professor da UFPB
    except StopIteration:
        print(f"❌ Nenhum perfil encontrado para {professor}.")
    except Exception as e:
        print(f"❌ Erro ao buscar {professor}: {str(e)}")
    
    # Evita bloqueios do Google Scholar
    time.sleep(10)


# Executando a busca professor por professor
for professor in professores:
    buscar_artigos(professor)


