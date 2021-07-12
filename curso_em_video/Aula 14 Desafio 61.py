print('{:=^40}'.format(' TREINANDO O COMANDO WHILE '))
print('{:=^40}'.format(' PROGRESSÃO ARITMÉTICA '))

t=int(input('\nDigite o 1º termo da PA: '))
r=int(input('Digite a razão da PA: '))
print('')
i=10
s=t
while i > 0:
    print('{} '.format(s), end='')
    i -= 1
    s += r
m=str(input('\n \nGostaria de incluir mais termos? [S/N]: ')).strip().upper()
if m not in 'SN':
    m1 = str(input('Dado incorreto. Digite novamente [S/N]: ')).strip().upper()
    if m1 == 'S':
        i2=int(input('Mais quantos termos você quer? '))
        print('')
        while i2 > 0:
            print('{} '.format(s), end='')
            i2 -= 1
            s += r
    if m1 == 'N':
        print('Ok! Até a próxima!')
if m == 'S':
    i2 = int(input('Mais quantos termos você quer? '))
    print('')
    while i2 > 0:
        print('{} '.format(s), end='')
        i2 -= 1
        s += r
else:
    print('')
    print('Ok! Até a próxima!')


#print('Ok! Até a próxima!')



# for c in range(t,n,r):
#    print(c, end=' ')
# print('\nFIM')

# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e
# a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.