# RESOLUCAO PROFESSOR
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for n in range(1, tot + 1):
    partidas.append(int(input(f'Quantos gols ele fez na partida {n}?: ')))
jogador['gols'] = partidas[:]
jogador['saldo'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador["gols"]):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'\nFoi um total de {jogador["saldo"]} gols')
print('-='*30)



"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato.
"""