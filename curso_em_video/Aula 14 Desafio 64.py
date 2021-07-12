print('{:=^40}'.format(' TREINANDO O COMANDO WHILE '))
print('{:=^40}'.format(' 999 PRA PARAR '))


cont = número = total = 0
número = int(input('Digite um número [999 para parar]: '))
while not número == 999:
    total += número
    cont += 1
    número = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma desses números é igual a {}.'.format(cont,total))
# Para desconsiderar o 999 pões o flag (que pega a variável) fora do while e também no final do while!


# Como eu fiz
#cont = -1
#número = total = -999
#while not número == 999:
#    número = int(input('Digite um número [999 para parar]: '))
#    total += número
#    cont += 1
#print('Você digitou {} números e a soma desses números é igual a {}.'.format(cont,total))



# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).