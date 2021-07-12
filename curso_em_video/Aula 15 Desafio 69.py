print('{:=^40}'.format(' TREINANDO O COMANDO BREAK'))
print('{:=^40}'.format(' LER IDADE E SEXO '))
cont = mais18 = homens = mulheres = 0
while True:
    idade = int(input('Qual a idade pessoa? '))
    cont += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo [M/F]? ')).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade > 20:
        mulheres += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar cadastrando ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('')
print('♕'*22)
print(f'\033[33m{mais18}\033[m tem mais de 18 anos.')
print(f'\033[33m{homens}\033[m homens foram cadastrados.')
print(f'\033[33m{mulheres}\033[m mulheres tem mais de 20 anos.')
print('♕'*22)

# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.