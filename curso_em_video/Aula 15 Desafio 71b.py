# RESOLUÇÃO GUSTAVO GUANABARA
print('{:=^40}'.format(' TREINANDO O COMANDO BREAK'))
print('{:=^40}'.format(' CAIXA AUTOMÁTICO '))
print(30*'=')
print('{:^30}'.format('BANCO ANDRÉ'))
print(30*'=')
valor = int(input('Que valor você quer sacar? '))
total = valor
ced = 50
totalced = 0
print('Você sacou:')
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'\033[34m{totalced}\033[m cédulas de \033[32mR${ced}\033[m.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break






# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.