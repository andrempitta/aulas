# MINHA SOLUÇãO
print('{:=^40}'.format(' TUPLAS '))
print(30*'=')
print('{:^30}'.format('NUMEROS ALEATORIOS MAIOR E MENOR'))
print(30*'=')

from random import randint

numeros = (randint(0,10), randint(0,10),randint(0,10),randint(0,10),randint(0,10))
# print(f'Sortiei os números {numeros}.')

print('Os números sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print('')
print(f'O maior número sorteado foi o {max(numeros)}')
print(f'O menor número sorteado foi o {min(numeros)}')

# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.