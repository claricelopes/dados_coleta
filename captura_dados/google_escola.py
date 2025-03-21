import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import datetime
driver = webdriver.Chrome() 

dados = []

nomes = [
    # "ADRIANA CARLA DAMASCENO",
    # "ALAN KELON OLIVEIRA DE MORAES",
    # "ALISSON VASCONCELOS DE BRITO",
    # "ALVARO FRANCISCO DE CASTRO MEDEIROS",
    # "ANA PAULA PINTADO WYSE",
    # "ANAND SUBRAMANIAN",
    # "ANDREA VANESSA ROCHA",
    # "ANDREI DE ARAUJO FORMIGA",
    # "ANTONIO JOSE BONESS DOS SANTOS",    
    # "LUCIANO SALES BARROS", #10 
    # "BRUNO JEFFERSON DE SOUSA PESSOA",
    # "APARECIDO JESUINO DE SOUZA",  
    # "BRUNO PETRATO BRUCK",  
    # "CAMILA MARA VITAL BARROS",  
    # "CARLOS ALBERTO NUNES MACHADO",  
    # "CARLOS EDUARDO COELHO FREIRE BATISTA",  
    # "CHRISTIAN AZAMBUJA PAGOT",  
    # "CLAUIRTON DE ALBUQUERQUE SIEBRA",  
    # "DANIELA COELHO BATISTA GUEDES PEREIRA",  
    # "DANIELLE ROUSY DIAS RICARTE",  #20
    # "DERZU OMAIA",  
    # "ED PORTO BEZERRA",  
    # "ELIZABET MARIA SPOHR DE MEDEIROS",  
    # "EUDISLEY GOMES DOS ANJOS",  
    # "EWERTON MONTEIRO SALVADOR",  
    # "FELIPE ANTONIO GARCIA MORENO",  
    # "FERNANDO MENEZES MATOS",  
    # "FRANCISCO DE ASSIS COUTINHO SOUTO",  
    # "GILBERTO FARIAS DE SOUSA FILHO",  
    # "GIORGIA DE OLIVEIRA MATTOS",  #30
    # "GLEDSON ELIAS DA SILVEIRA",  
    # "GUIDO LEMOS DE SOUZA FILHO",  
    # "GUSTAVO CHARLES PEIXOTO DE OLIVEIRA",  
    # "GUSTAVO HENRIQUE MATOS BEZERRA MOTTA",  
    # "HAMILTON SOARES DA SILVA",  
    # "HUGO LEONARDO DAVI DE SOUZA CAVALCANTE",  
    # "IGUATEMI EDUARDO DA FONSECA",  
    # "JAIRO ROCHA DE FARIA",  
    # "JAN SOKOLOWSKI",  
    # "JOSE ANTONIO GOMES DE LIMA",  #40
    # "JOSE MIGUEL AROZTEGUI MASSERA",  
    # "JOSILENE AIRES MOREIRA",  
    # "KELY DIANA VILLACORTA VILLACORTA",  
    # "LEANDRO CARLOS DE SOUZA",  
    # "LEONARDO VIDAL BATISTA",  
    # "LILIANE DOS SANTOS MACHADO",  
    # "LINCOLN DAVID NERY E SILVA",  
    # "LUCIDIO DOS ANJOS FORMIGA CABRAL",  
    # "MARDSON FREITAS DE AMORIM",  
    # "MOISES DANTAS DOS SANTOS",  #50
    # "NATASHA CORREIA QUEIROZ LINO",  
    # "RAONI KULESZA",  
    # "ROBERTO QUIRINO DO NASCIMENTO",  
    # "RUY ALBERTO CORREA ALTAFIM",  
    # "RUY ALBERTO PISANI ALTAFIM",  
    # "SERGIO DE CARVALHO BEZERRA",  
    # "TATIANA ARAUJO SIMOES",  
    # "TEOBALDO LEITE BULHÕES JUNIOR",  
    # "TIAGO PEREIRA DO NASCIMENTO",  
     "THAIS GAUDENCIO DO REGO",  #60
     "TIAGO MARITAN UGULINO DE ARAUJO",
     "VALDECIR BECKER ",
     "VIVEK NIGAM",  
     "VITOR MENEGHETTI UGULINO DE ARAUJO",
     "YURI MALHEIROS ",
     "YUSKA PAOLA COSTA AGUIAR" #66
]

driver.get("https://scholar.google.com.br/?hl=pt")
print("inicio")
time.sleep(2) 

for nome in nomes:
    try:
        search_box = driver.find_element(By.XPATH, '//*[@id="gs_hdr_tsi"]')
        search_box.clear()
        search_box.send_keys(nome)
        search_box.send_keys(Keys.ENTER)

        time.sleep(3)

        try:
            primeiro_link = driver.find_element(By.XPATH, '//*[@id="gs_res_ccl_mid"]/div[1]/h3/a')
            primeiro_link.click()
        except NoSuchElementException:
            dados.append({"Professor Pesquisado": nome, "Resposta": "Nome não encontrado"})
            continue

        time.sleep(3)

        try:
            perfil_link = driver.find_element(By.XPATH, '//*[@id="gsc_sa_ccl"]/div/div/div/h3/a')
            perfil_link.click()
            time.sleep(3)
        except:
            print(f"Perfil de {nome} não possui link para artigos.")

        max_tentativas = 10  # Limite de cliques para evitar loop infinito
        tentativas = 0

        while tentativas < max_tentativas:
            try:
                botao_mostrar_mais = driver.find_element(By.ID, "gsc_bpf_more")
                
                # Verifica se o botão existe e está visível antes de tentar clicar
                if botao_mostrar_mais.is_displayed():
                    botao_mostrar_mais.click()
                    time.sleep(2)
                    tentativas += 1
                else:
                    print("Botão não está visível. Encerrando loop.")
                    break
            except (NoSuchElementException, ElementClickInterceptedException):
                print("Botão não encontrado ou não pode ser clicado. Encerrando loop.")
                break
        print("Loop encerrado.")

        artigos_links = driver.find_elements(By.XPATH, '//*[@id="gsc_a_b"]/tr/td[1]/a')

        if not artigos_links:
            print(f"Nenhum artigo encontrado para {nome}.")
            dados.append({"Autor": nome, "Erro": "Nenhum artigo encontrado"})
            continue
        print("capturando dados")
        for i in range(len(artigos_links)):
            try:
                artigos_links = driver.find_elements(By.XPATH, '//*[@id="gsc_a_b"]/tr/td[1]/a')

                titulo_artigo = artigos_links[i].text

                artigos_links[i].click()
                time.sleep(3)

                try:
                    tabela = driver.find_elements(By.XPATH, '//*[@id="gsc_oci_table"]/div')

                    valores = [campo.text.strip() for campo in tabela]
                    valores += [""] * (7 - len(valores))
                               
                    artigo = {
                        "Professor Pesquisado": nome,
                        "01": titulo_artigo,
                        "02": valores[0],
                        "03": valores[1],
                        "04": valores[2],
                        "05": valores[3],
                        "06": valores[4],
                        "07": valores[5],
                        "08": valores[6],
                        "Resposta": "OK"
                    }
                    dados.append(artigo)

                except NoSuchElementException:
                    print(f"Não foi possível capturar os detalhes do artigo {i + 1}.")

                driver.back()
                time.sleep(3)

            except Exception as e:
                print(f"Erro ao acessar artigo {i + 1}: {str(e)}")

        driver.get("https://scholar.google.com.br/?hl=pt")
        time.sleep(2)

    except Exception as e:
        print(f"Erro ao buscar {nome}: {str(e)}")

driver.quit()

df = pd.DataFrame(dados)

csv_string = ""
for _, row in df.iterrows():
    for col in df.columns:
        csv_string += f"{col}: {row[col]}\n"
    csv_string += "\n"

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
with open(f'resultado_{timestamp}.csv', "w", encoding="utf-8") as f:
    f.write(csv_string)

print('fim')