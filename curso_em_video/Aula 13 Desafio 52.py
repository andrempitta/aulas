print('\033[33m{:✶^40}\033[m'.format(' NÚMEROS PRIMOS '))
n = int(input('Digite um número: '))
total=0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[32m', end='')
        total+= 1
    else:
        print('\033[33m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n,total))
if total == 2:
    print('\033[32mEntão é um número primo!\033[m')
else:
    print('\033[37mEntão não é um número primo!\033[m')
print('↭✶↭')

# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.