📊 Projeto: Dados dos Trabalhos Acadêmicos do Centro de Informática da UFPB


#Integrantes

-Clarice Lopes 

-Felipe Medeiros

-Vinícius Mangueira


#Tema do Projeto

Este projeto tem como objetivo coletar, analisar e visualizar dados dos trabalhos acadêmicos produzidos pelo Centro de Informática da Universidade Federal da Paraíba (UFPB). A pesquisa inclui artigos  vinculados ao centro, permitindo uma melhor compreensão das áreas de estudo e colaborações institucionais.


#Abordagem de Coleta de Dados

Para obter os dados necessários, utilizamos a seguinte abordagem:

Scraping: Extração automatizada de informações do site Google Scholar, utilizando Selenium.

#Tecnologias Utilizadas

Linguagem: Python

#Pré Requisitos 

Para rodar o script de coleta de dados é necessário ter:
-Selenium 
-Pandas

#Resultado

O resultado do script é um arquivo csv com informações coletadas em cada artigo disponível vinculado ao nome do professor pesquisado. Dentre as informações:
      -Professor Pesquisado: contendo o nome do professor que está sendo pesquisado,
      -Título do Artigo: título do artigo coletado no momento,
      -Autores: este campo contém os nomes dos autores que colaboraram para o artigo,
      -Data de Publicação: campo data com dia, mês e ano de publicação,
      -Conferência: onde o artigo foi publicado,
      -Páginas: número de páginas correspondente,
      -Editora: especificação da editora encarregada,
      -Descrição: campo que mostra um resumo do artigo em questão,
      -Total de Citações: número de citações que o trabalho possui,
      -Resposta: campo de controle para professores que possuem perfil no site (google scholar), podendo ter valor atribuido "OK", em caso de sucesso e "Nome não encontrado", caso contrario. 

#Exemplo de saida, arquivo csv
![image](https://github.com/user-attachments/assets/04d0dc2c-8df3-4527-ba3f-a74be7232dd9)

#Sobre a coleta

Para obter os artigos produzidos pelos professores do Centro de Infomática nós utilizamos um script python que navega até o site Google Scholar e pesquisa os nomes passados em uma lista,
a partir disso através dos XPATHs do html do site os dados desejados são guardados. Após a coleta as informações são salvas em um arquivo csv que está disponível no Google Drive, nesse caminho: https://drive.google.com/drive/folders/1FzNxWKGSvls2wSOYpPdSy_WcuWQH6c_m?usp=drive_link


