a=int(input('Primeiro valor: '))
b=int(input('Segundo valor: '))
c=int(input('Terceiro valor: '))
# verificar quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# verificar quem é maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O menor valor é {}.'.format(menor))
print('O maior valor é {}.'.format(maior))


# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.