print('{:=^40}'.format(' PROGRESSÃO ARITMÉTICA '))
print('{:=^40}'.format(' 10 TERMOS DE UMA PA '))
t=int(input('\nDigite o 1º termo da PA: '))
r=int(input('Digite a razão da PA: '))
termos=10
n=t+termos*r
s=0
for c in range(t,n,r):
    print(c, end=' ')
print('\nFIM')


# s + r

# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.