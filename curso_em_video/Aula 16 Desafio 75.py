# MINHA SOLUÇãO
print('{:=^40}'.format(' TUPLAS '))
print(30*'=')
print('{:^30}'.format('LER VALORES EM UMA TUPLA'))
print(30*'=')


numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: '))
           )
print('Você digitou os números: ', end='')
#for n in numeros:
#    print(n, end='')
#    if n != numeros[-1]:
#        print(',', end=' ')
#    else:
#        print('.', end='')
#    if n == 9:
print(f'Os númerso são {numeros}.')
print(f'\nO número 9 apareceu {numeros.count(9)} vezes.')
print(f'O número 3 apareceu na {numeros.index(3)+1}ª posição.')
for n in numeros:
    if n % 2 ==0:
        print(n, end=' ')



#    if n == 3:
#print(f'O número 3 apareceu na posição {numeros.index(3)}.')




# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.