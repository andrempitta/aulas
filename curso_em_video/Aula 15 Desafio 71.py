# MINHA SOLUÇãO
print('{:=^40}'.format(' TREINANDO O COMANDO BREAK'))
print('{:=^40}'.format(' CAIXA AUTOMÁTICO '))
print(30*'=')
print('{:^30}'.format('BANCO ANDRÉ'))
print(30*'=')
valor = int(input('Que valor você quer sacar? '))
c = 50; v = 20; d = 10; u = 1
nc = nv = nd = nu = rc = rv = rd = ru = 0
if valor >= 50:
    nc = valor // c
    rc = valor % c
    if rc != 0:
        nv = rc // v
        rv = rc % v
    if rv != 0:
        nd = rv // d
        rd = rv % d
    if rd != 0:
        nu = rd / u
if valor < 50:
    nv = valor // v
    rv = valor % v
    if rv != 0:
        nd = rv // d
        rd = rv % d
    if rd != 0:
        nu = rd / u
if valor < 10:
    nu = valor / u
#if nc = 0:

print('Você retirou:')
if nc != 0:
    print(f'\033[34m{nc}\033[m notas de R$50,00.')
if nv != 0:
    print(f'\033[34m{nv}\033[m notas de R$20,00.')
if nd != 0:
    print(f'\033[34m{nd}\033[m notas de R$10,00.')
if nu != 0:
    print(f'\033[34m{nu:.0f}\033[m notas de R$1,00.')


#if rc != 0:
#    print('rc ',rc)
#if rv != 0:
#    print('rv ',rv)
#if rd != 0:
#    print('rd ',rd)
#if ru != 0:
#    print('ru ',ru)

#print(nd)
#print(nu)

# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.