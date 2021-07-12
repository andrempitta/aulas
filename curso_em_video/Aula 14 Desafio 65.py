print('{:=^40}'.format(' TREINANDO O COMANDO WHILE '))
print('{:=^40}'.format(' QUER CONTINUAR? [S/N] '))

# SOLUÇÃO GUSTAVO GUANABARA
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N]? ')).upper().strip()[0] # [0] para considerar só a primeira letra
média = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant,média))
print('O maior valor foi {} e o menor foi {}.'.format(maior,menor))

# MINHA SOLUÇÃO

# maior = soma = 0
# cont=1
# n=int(input(' Digite um número: '))
# p=str(input('Quer continuar? [S/N] ')).upper().strip()
# soma += n
# if maior < n: maior = n
# while p == 'S':
#     n = int(input(' Digite um número: '))
#     soma += n
#     cont += 1
#     if maior < n: maior = n
#     p = str(input('Quer continuar? [S/N] ')).upper().strip()
# média=soma/cont
# print('Você digitou {} números e a média foi {}.'.format(cont,média))
# print('O maior número que você digitou foi: {}.'.format(maior))


# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.