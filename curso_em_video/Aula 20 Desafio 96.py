# MINHA PROFESSOR
def área(larg, comp):
    a = larg * comp
    print(f'A largura de um terreno de {larg}m de largura por {comp}m de comprimento é {a}m2')


print(' Controle de Terrenos')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)

"""
Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre
 a área do terreno.
"""