print('{:=^40}'.format(' TREINANDO O COMANDO WHILE '))
print('{:=^40}'.format(' FIBONACCI '))

# 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13

n=int(input('Quantos números da sequência de fibonacci você deseja mostrar? '))
t1 = 0
t2 = 1
print('{} ⇢ {}'.format(t1,t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' ⇢ {}'.format(t3), end='')
    cont += 1
    t1=t2
    t2=t3
print(' ⇢ FIM')



# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci.