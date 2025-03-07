import requests

# Defina a URL base da API SciELO
base_url = "https://api.scielo.org"

# Exemplo de pesquisa, você pode substituir "Computer Science UFPB" por qualquer outro termo
search_query = "Computer%20Science%20Department%20UFPB"
url = f"{base_url}/api/v1/search/?q={search_query}"

# Realiza a requisição GET para obter os resultados
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Converte a resposta para JSON
    for article in data['results']:
        title = article['title']
        link = article['link']
        print(f"Título: {title}")
        print(f"Link: {link}")
        print("-" * 50)
else:
    print(f"Erro: {response.status_code}")

