import requests

# URL da API do Medium
API_URL = "https://api.medium.com/v1/users/{user_id}/publications"

# Substitua {user_id} pelo ID do usuário ou nome da publicação
user_id = "your_user_id_or_publication_id"  # Você precisará obter o ID do usuário ou da publicação

# Token de acesso (substitua com seu token real)
access_token = "your_access_token"  # Substitua pelo seu token de acesso

# Cabeçalhos para autenticação
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Fazendo a requisição para obter as publicações do usuário
response = requests.get(f"{API_URL.replace('{user_id}', user_id)}", headers=headers)

# Verificando a resposta
if response.status_code == 200:
    publications = response.json()
    print("Publicações encontradas:")
    for pub in publications['data']:
        print(f"Name: {pub['name']}")
        print(f"URL: {pub['url']}")
        print("-" * 40)
else:
    print(f"Erro ao acessar a API do Medium. Status Code: {response.status_code}")

