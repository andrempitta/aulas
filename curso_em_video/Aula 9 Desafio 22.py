nome=str(input('Digite seu nome Completo ')).strip()
print('Analisando seu nome...')
print('\nSeu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
pnome=nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(pnome[0],len(pnome[0])))
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #não entendi bem porque no find usa (' ') para contar as letras da 1ª palavra da string



#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.