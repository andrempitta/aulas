n=str(input('Digite seu nome completo ')).strip()
print('Muito prazer em te conhecer!')
nome=n.split()
print('Seu primeiro nome é {}.'.format(nome[0]))
print('E seu último nome é {}.'.format(nome[len(nome)-1]))


# Exercício Python 027: Faça um programa que leia o nome completo
# de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.