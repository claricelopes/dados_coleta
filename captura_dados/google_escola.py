from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() 

nomes = [
    "YURI MALHEIROS"
]

driver.get("https://scholar.google.com.br/?hl=pt")
time.sleep(2) 

for nome in nomes:
    try:
        search_box = driver.find_element(By.XPATH, '//*[@id="gs_hdr_tsi"]')
        search_box.clear()
        search_box.send_keys(nome)
        search_box.send_keys(Keys.ENTER) 
        time.sleep(3) 

        primeiro_link = driver.find_element(By.XPATH, '//*[@id="gs_res_ccl_mid"]/div[1]/h3/a')
        primeiro_link.click()

        time.sleep(3) 

        try:
            perfil_link = driver.find_element(By.XPATH, '//*[@id="gsc_sa_ccl"]/div/div/div/h3/a')
            perfil_link.click()
            time.sleep(3)  
        except:
            print(f"Perfil de {nome} não possui link para artigos.")

        artigos_links = driver.find_elements(By.XPATH, '//*[@id="gsc_a_b"]/tr/td[1]/a')

        for i in range(len(artigos_links)):
            try:
                artigos_links = driver.find_elements(By.XPATH, '//*[@id="gsc_a_b"]/tr/td[1]/a')

                artigos_links[i].click()
                time.sleep(3)  

                tabela_info = driver.find_element(By.XPATH, '//*[@id="gsc_oci_table"]')
                print(f"\nDetalhes do Artigo {i + 1}:")
                print(tabela_info.text)

                driver.back()
                time.sleep(3)

            except Exception as e:
                print(f"Erro ao acessar artigo {i + 1}: {str(e)}")

        driver.get("https://scholar.google.com.br/?hl=pt")
        time.sleep(2)

    except Exception as e:
        print(f"Erro ao buscar {nome}: {str(e)}")

driver.quit()
