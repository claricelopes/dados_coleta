from scholarly import scholarly
import csv
import time
import unicodedata

# Lista com os professores
professores = [
    {"nome": "THAIS GAUDÊNCIO", "user_id": "93u15fEAAAAJ"},
    {"nome": "GILBERTO FARIAS", "user_id": "N2wRsIoAAAAJ"},
    {"nome": "GLEDSON ELIAS", "user_id": "S1H198kAAAAJ"},
    {"nome": "TEOBALDO BULHÕES", "user_id": "T9vkFzQAAAAJ"},
    {"nome": "TIAGO PEREIRA DO NASCIMENTO", "user_id": "k5hP6gUAAAAJ"}
]

# Função para normalizar strings (remover acentos e colocar em minúsculas)
def normalize(text):
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    return text.lower().strip()

# Abrir CSV de saída e escrever cabeçalho
with open("coautores_artigos.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Artigo", "Coautor"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Para cada professor, buscar suas publicações
    for prof in professores:
        nome = prof["nome"]
        user_id = prof["user_id"]
        prof_norm = normalize(nome)

        print(f"\n📚 Coletando co-autores de {nome}...")
        try:
            autor = scholarly.search_author_id(user_id)
            autor = scholarly.fill(autor, sections=["publications"])
        except Exception as e:
            print(f"❌ Erro ao acessar perfil de {nome}: {e}")
            continue

        # Iterar pelas publicações
        for i, pub in enumerate(autor.get("publications", []), start=1):
            try:
                # Preenche detalhes da publicação
                artigo_completo = scholarly.fill(pub)
                titulo = artigo_completo.get("bib", {}).get("title", "Sem título")
                authors_str = artigo_completo.get("bib", {}).get("author", "")

                # Divide a string de autores e filtra apenas os co-autores
                # A lista geralmente está no formato "Autor1 and Autor2 and Autor3"
                coautores = []
                for autor_str in authors_str.split(" and "):
                    autor_str = autor_str.strip()
                    if autor_str and normalize(autor_str) != prof_norm:
                        coautores.append(autor_str)
                
                # Se não houver co-autores, registra entrada informativa
                if not coautores:
                    writer.writerow({
                        "Artigo": titulo,
                        "Coautor": "Nenhum coautor encontrado"
                    })
                    print(f"→ [{i}] {titulo} — nenhum coautor")
                else:
                    for co in coautores:
                        writer.writerow({
                            "Artigo": titulo,
                            "Coautor": co
                        })
                    print(f"→ [{i}] {titulo} — {len(coautores)} coautores adicionados")

                # Pausa entre requisições para não sobrecarregar o Google Scholar
                time.sleep(3)
                if i % 10 == 0:
                    print("⏸ Pausa de 30 segundos...")
                    time.sleep(30)

            except Exception as e:
                print(f"⚠️ Erro ao processar publicação {i}: {e}")
                continue

print("\n🎉 Coleta de co-autores finalizada!")
print("Os dados foram salvos em 'coautores_artigos.csv'.")
