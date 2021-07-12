print('{:=^40}'.format(' TREINANDO O COMANDO BREAK'))
print('{:=^40}'.format(' LOJA DE SUPERMERCADO '))
cont = total = maisdemil = maisbarato = 0
barato = ''
while True:
    produto=str(input('Nome do produto: '))
    preço=float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
            maisdemil += 1
    if cont == 1 or preço < maisbarato: # Usando o or ... evita repetir o comando da lina 15 à 18
        maisbarato = preço
        barato = produto
#    else:
#        if preço < maisbarato:
#            maisbarato = preço
#            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total gasto na compra foi de \033[33mR${total:.2f}\033[m.')
print(f'\033[33m{maisdemil}\033[m produto(s) custa(m) mais de R$1.000,00.')
print(f'O produto mais barato é \033[33m{barato}\033[m que custa R$\033[33m{maisbarato:.2f}\033[m.')
print('{:-^40}'.format('FIM DO PROGRAMA'))


# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.