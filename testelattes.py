from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def extrair_artigos_lattes(url):
    # Configurar o WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Executar sem abrir o navegador
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    print(f"Acessando URL: {url}")
    driver.get(url)
    time.sleep(5)  # Tempo maior para garantir carregamento da página

    artigos = []
    try:
        # Buscar os artigos pelo XPath correto
        secao_artigos = driver.find_elements(By.XPATH, "//div[contains(@class, 'artigo-completo')]")
        print(f"Encontrados {len(secao_artigos)} artigos.")

        for artigo in secao_artigos:
            try:
                titulo = artigo.find_element(By.TAG_NAME, "b").text  # Título do artigo
                autores = artigo.find_element(By.TAG_NAME, "i").text  # Lista de autores

                # Extrair detalhes (periódico, volume, ano)
                detalhes = artigo.text  # Pegar todo o texto para análise
                
                artigos.append({
                    "titulo": titulo,
                    "autores": autores,
                    "detalhes": detalhes
                })
                print(f"Artigo extraído: {titulo}")
            
            except Exception as e:
                print("Erro ao processar um artigo:", e)
    except Exception as e:
        print("Erro ao extrair artigos:", e)
    
    driver.quit()
    return artigos

# Exemplo de uso:
curriculo_url = "https://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K1234567Y8"  # Substituir pelo link correto
artigos = extrair_artigos_lattes(curriculo_url)
for artigo in artigos:
    print(artigo)
