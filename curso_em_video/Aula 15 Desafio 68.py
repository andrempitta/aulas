# MINHA SOLUCAO
from random import randint
from time import sleep
print('{:=^40}'.format(' TREINANDO O COMANDO BREAK'))
print('{:=^40}'.format(' PAR OU ÍMPAR '))
print('')
print('-='*20)
# nome = 'VAMOS JOGAR PAR OU ÍMPAR'
# print(f'{nome:^20}')
print('{:>30}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('-='*20)
while True:
    njogador = int(input('Digite um valor: '))
    m = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    # computador = randint(0,1)
    ncomputador = randint(0,10) # 0 é Par e 1 é Impar
    if m == 'P':
        jogador = 0
        computador = 1
    if m == 'I':
        jogador = 1
        computador = 0
    mão = njogador + ncomputador
    if mão % 2 == 0:
        poi = 'PAR'
    else:
        poi = 'IMPAR'
    if jogador == 0: print('PAR. Ok!')
    if jogador == 1: print('IMPAR. Ok!')
    sleep(1)
    print('--' * 20)
    print(f'Você escolheu {njogador} e eu {ncomputador}. Total: {mão}.\nDeu {poi}!')
    if mão % 2 == 0 and jogador == 0:
        print('--' * 20)
        print('{:>20}'.format('VOCÊ GANHOU! Parabéns e até a próxmia!'))
        break
    if mão % 2 == 0 and jogador == 1:
        print('--' * 20)
        print('{:>20}'.format('EU GANHEI!'))
    if mão % 2 == 1 and jogador == 1:
        print('--' * 20)
        print('{:>20}'.format('VOCÊ GANHOU!  Parabéns e até a próxmia!'))
        break
    if mão % 2 == 1 and jogador == 0:
        print('--' * 20)
        print('{:>20}'.format('EU GANHEI!'))
    print('--'*20)



# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.