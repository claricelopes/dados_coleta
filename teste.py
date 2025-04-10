from scholarly import scholarly
import time

def extrair_nomes_perfis(user_ids):
    nomes = []
    
    for user_id in user_ids:
        try:
            # Buscar o perfil do usuário pelo ID
            perfil = scholarly.search_author_id(user_id)
            if perfil:
                nome = perfil.get('name', 'Nome não encontrado')
            else:
                nome = 'Perfil não encontrado'
        except Exception as e:
            nome = f'Erro ao acessar o perfil {user_id}: {str(e)}'
        
        nomes.append(nome)
        
        # Aguardar alguns segundos entre as requisições para evitar bloqueios
        time.sleep(5)
    
    return nomes

# Lista de IDs dos perfis do Google Scholar
user_ids = [
    "o3IaIqgAAAAJ",
    "x2kDq8sAAAAJ",
    "S2lG9qUAAAAJ",
    "D7TvPxEAAAAJ",
    "eOy6-gwAAAAJ",
    "03yOfsUAAAAJ",
    "g5hC8PcAAAAJ",
    "j-GWmOQAAAAJ",
    "A710q_4AAAAJ",
    "uWRPCo4AAAAJ",
    "EtTIx5kAAAAJ",
    "mlXLxsIAAAAJ",
    "mhkED-YAAAAJ",
    "uy0CrH2tvhIC",
    "K7bui-gAAAAJ",
    "Fsqs3eEAAAAJ",
    "mw1CHjMAAAAJ",
    "fIZH1VgAAAAJ",
    "zhfOE78AAAAJ",
    "pzBf11IAAAAJ",
    "D69q_U0AAAAJ",
    "etiXS3YAAAAJ",
    "7xj7_eIAAAAJ",
    "k5hP6gUAAAAJ",
    "93u15fEAAAAJ",
    "41TafCsAAAAJ",
    "IUgIAGUAAAAJ",
    "I_wEMfsAAAAJ",
    "EQ0pvXUAAAAJ",
    "OVCYPnwAAAAJ",
    "T9vkFzQAAAAJ",
    "zhfOE78AAAAJ",
    "_vNl6lAAAAAJ",
    "mhkED-YAAAAJ",
    "330ic4MAAAAJ",
    "vOTINpcAAAAJ",
    "8qIExvcAAAAJ"
]

# Chamar a função e imprimir os resultados
nomes = extrair_nomes_perfis(user_ids)
for nome in nomes:
    print(nome)

