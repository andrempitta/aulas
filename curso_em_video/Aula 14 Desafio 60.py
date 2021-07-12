print('{:=^40}'.format(' TREINANDO O COMANDO WHILE '))
print('{:=^40}'.format(' CALCULO FATORIAL '))

from math import factorial

f = int(input('Digite 1 número para calcular o seu fatorial: '))
# x = factorial(f)
c = f
x = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    x *= c
    c -= 1
print('{}'.format(x), end=' ')
print('\nO fatorial de {}! é {}.'.format(f, x))
#    resultado = resultado*(f-1)*f
# print(resultado)


# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

