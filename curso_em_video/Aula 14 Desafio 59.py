from os import system
from time import sleep
print('{:=^40}'.format(' TREINANDO O COMANDO WHILE '))
print('{:=^40}'.format(' MENU DE OPÇÕES '))

n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))
o = 0
while o != 5:
    print("""    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    o = int(input(' Qual é a sua opção? '))
    if o==1:
        print('{} + {} = {:.2f}'.format(n1,n2,n1 + n2))
    elif o==2:
        print('{} x {} = {:.2f}'.format(n1, n2, n1 * n2))
    elif o==3:
        if n1 > n2:
            print('O número maior é o {}.'.format(n1))
        elif n2 > n1:
            print('O número maior é o {}.'.format(n2))
    elif o == 4:
        print('informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif o == 5:
        print('Finalizando. . .')
        sleep(.5)
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
    # system('clear') # Limpa a tela

print('Fim do Programa! Obrigado!')


# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.