x=int(input('\nDigite um número qualquer que retornarei os números múltiplos de 3 nesse intervalo: '))
s = 0
cont = 0
print('Os números são:')
for n in range(1,x+1):
    if n % 3 == 0:
        print( n, end=' ')
        s+=n # Pode ser expresso assim: s = s + n
        cont = cont + 1 # Pode ser expresso assim: cont += 1
    else:
        print('', end='')
print('\n')
print('Nesse intervalo tem {} números.'.format(cont))
print('E a soma desses múltiplos de 3 é: {}.'.format(s))
print('\n')
print('FIM')






# Exercício Python 048: Faça um programa que calcule a soma entre todos os
# números que são múltiplos de três e que se encontram no intervalo de 1 até 500.