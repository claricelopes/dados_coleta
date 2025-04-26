
from collections import defaultdict
import matplotlib.pyplot as plt
# gera grafico com as palavras que mais aparecem nos titulos dos artigos
dados = """
poroso: 24
móvel: 23
análise: 20
modelo: 18
suporte: 18
problema: 17
mídia: 17
fluxo: 15
combustão: 13
aprendizagem: 13
controle: 13
planejamento: 12
solução: 11
abordagem: 11
trifásico: 10
sistema: 9
gerenciamento: 9
vento: 9
microrrede: 9
problema: 62
problema: 38
roteamento: 36
veículo: 34
pesquisa: 26
ensino: 22
programação: 22
sistema: 21
heurística: 21
híbrido: 19
iterado: 18
algoritmo: 17
análise: 16
análise: 15
modelos: 15
digitais: 34
sociais: 13
televisão: 12
sistema: 12
redes: 12
Programas: 12
análise: 11
redes: 11
monitoramento: 10
aprendizagem: 10
arquitetura: 9
informação: 9
virtuais: 9
análise: 9
sistema: 8
digitais: 8
ferramenta: 8
virtuais: 131
realidade: 72
treinamento: 65
avaliação: 47
realidade: 38
confuso: 33
avaliação: 32
saúde: 30
simuladores: 29
on-line: 28
imagens: 28
jogos: 27
médico: 25
baías: 25
problema: 25
ensino: 24
digitais: 27
baseado: 23
televisão: 23
estudo: 22
canais: 16
rede: 15
sistema: 15
ferroeletretos: 15
usp: 15
distribuição: 13
piezoeletretos: 13
tubular: 13
elétrica: 13
candidatos: 13
planejamento: 12
dados: 12
impulso: 12
suporte: 11
digitais: 48
sistema: 42
TV: 64
audiovisual: 29
Programas: 25
segurança: 25
avaliação: 24
análise: 24
sinal: 23
brasileiro: 22
idioma: 18
análise: 17
máquina: 16
protocolos: 16
segurança: 16
sistema: 15
interativo: 15
em direção: 14
redes: 33
digitais: 30
redes: 25
óptico: 21
Modelo: 20
sistema: 17
estudo: 13
sistema: 12
serviços: 12
distribuição: 12
vídeo: 12
sem fio: 12
sensor: 12
brasileiro: 11
ferramenta: 11
acesso: 11
"""

frequencia = defaultdict(int)
for linha in dados.strip().splitlines():
    if ':' in linha:
        palavra, valor = linha.split(':')
        palavra = palavra.strip().lower()
        valor = int(valor.strip())
        frequencia[palavra] += valor

top_25 = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)[:25]

top_25_lista = "\n".join([f"{palavra}: {valor}" for palavra, valor in top_25])

plt.figure(figsize=(12, 8))
palavras, valores = zip(*top_25)
plt.barh(palavras[::-1], valores[::-1], color='skyblue')
plt.xlabel('Frequência')
plt.title('Top 25 Palavras Mais Frequentes')
plt.tight_layout()

print(top_25_lista)
plt.show()
