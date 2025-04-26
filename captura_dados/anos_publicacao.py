import csv
import re
# pega so o ano das datas coletadas
arquivo_entrada = 'datas_publicacao.csv'
arquivo_saida = 'anos_publicacao.csv'

anos_extraidos = []

with open(arquivo_entrada, mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)

    for linha in reader:
        if linha:
            data = linha[0]
            match = re.search(r'(\d{4})', data)
            if match:
                ano = match.group(1)
                anos_extraidos.append([ano])

with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(['Ano'])
    writer.writerows(anos_extraidos)

print('Arquivo com apenas os anos criado com sucesso!')
