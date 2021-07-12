# RESOLUCAO PROFESSOR
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for n in range(1, tot + 1):
        partidas.append(int(input(f'Quantos gols ele fez na partida {n}?: ')))
    jogador['gols'] = partidas[:]
    jogador['saldo'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Voce quer continuar incluindo jogadores? [s/n]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
         break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('_' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('_' * 40)
while True:
    busca = int(input('Qual jogador vc quer analisar? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGAR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('Volte sempre!')







#print('-='*30)
#print(jogador)
#print('-='*30)

#for i, v in enumerate(jogador["gols"]):
#    print(f'    => Na partida {i}, fez {v} gols.')
#print(f'\nFoi um total de {jogador["saldo"]} gols')
#print('-='*30)



"""
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato.
"""