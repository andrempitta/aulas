# RESOLUCAO PROFESSOR

galera = list()
pessoa = dict()
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digitar apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy()) # .copy pois 'pessoa' é dicionario se fosse lista seria por fatiamento [:].
    while True:
        resp = str(input('Quer continuar? [s/n]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('=-'*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A idade média é de {media:5.2f} anos.')
print('As mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f' {p["nome"]}', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f' {k} - {v}', end='')
print()
print('<< ENCERRADO >>')

# print(galera)




"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
E) invadi o computador do papai (marcela)
F) quero um cachorrinho 
"""