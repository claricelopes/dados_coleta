from scholarly import scholarly
import csv
import time

# Lista com os professores
professores = [
    {"nome": "THAIS GAUDÊNCIO", "user_id": "93u15fEAAAAJ"},
    {"nome": "GILBERTO FARIAS", "user_id": "N2wRsIoAAAAJ"},
    {"nome": "GLEDSON ELIAS", "user_id": "S1H198kAAAAJ"},
    {"nome": "TEOBALDO BULHÕES", "user_id": "T9vkFzQAAAAJ"},
    {"nome": "TIAGO PEREIRA DO NASCIMENTO", "user_id": "k5hP6gUAAAAJ"}
]

# Criar novo arquivo CSV com cabeçalho
with open("artigomais_com_ano.csv", "w", newline="", encoding="utf-8") as csvfile:
    campos = ["Professor", "Artigo", "Ano"]
    writer = csv.DictWriter(csvfile, fieldnames=campos)
    writer.writeheader()

# Coletar artigos dos professores
for prof in professores:
    nome = prof["nome"]
    user_id = prof["user_id"]

    print(f"\n📚 Coletando artigos de {nome}...")
    try:
        autor = scholarly.search_author_id(user_id)
        autor = scholarly.fill(autor, sections=["publications"])
    except Exception as e:
        print(f"❌ Erro ao acessar perfil de {nome}: {e}")
        continue

    dados_csv = []

    for i, pub in enumerate(autor.get("publications", [])):
        try:
            print(f"→ Coletando artigo {i + 1}: {pub['bib']['title']}")
            artigo_completo = scholarly.fill(pub)
            titulo = artigo_completo.get("bib", {}).get("title", "Sem título")
            ano = artigo_completo.get("bib", {}).get("pub_year", "Sem ano")
            dados_csv.append({"Professor": nome, "Artigo": titulo, "Ano": ano})

            # Pausa entre requisições
            time.sleep(3)

            # Pausa maior a cada 10 artigos
            if (i + 1) % 10 == 0:
                print("⏸ Pausa de 30 segundos...")
                time.sleep(30)

        except Exception as e:
            print(f"⚠️ Erro ao coletar artigo {i + 1}: {e}")
            continue

    if not dados_csv:
        dados_csv.append({"Professor": nome, "Artigo": "Nenhuma publicação encontrada", "Ano": "Sem ano"})

    with open("artigomais_com_ano.csv", "a", newline="", encoding="utf-8") as csvfile:
        campos = ["Professor", "Artigo", "Ano"]
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writerows(dados_csv)

    print(f"✅ {len(dados_csv)} artigo(s) de {nome} salvos no novo CSV.")

print("\n🎉 Coleta finalizada!")
print("Os dados foram salvos no arquivo 'artigomais_com_ano.csv'.")
print("Verifique o arquivo para mais detalhes.")