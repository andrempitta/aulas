# RESOLUCAO PROFESSOR
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(0,6),
        'jogador2': randint(0,6),
        'jogador3': randint(0,6),
        'jogador4': randint(0,6),
        'jogador5': randint(0,6),
        'jogador6': randint(0,6)}

ranking = list()

print('Valores sorteados:')

for k, v in jogo.items():
    print(f'{k} - {v}')
    sleep(1)
print(f'-=' * 30)
print('Ranking os Jogadores:')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)











"""
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham
 resultados aleatórios. Guarde esses resultados em um dicionário em Python.
 No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

"""