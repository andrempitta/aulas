# MINHA SOLUÇãO
print('{:=^40}'.format(' TUPLAS '))
print(30*'=')
print('{:^30}'.format('LISTA'))
print(30*'=')

lista = ('Laranja', 2,
         'Abacate', 3.5,
         'Cenoura', 2.35,
         'Tomate', 2.4,
         'Beterraba', 5.3,
         'Água com gás', 4.25,
         'Barra de chocolate', 19.5,
         'Sorvete', 32.5)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>6.2f}')



# Exercício Python 076: Crie um programa que tenha uma tupla
# única com nomes de produtos e seus respectivos preços, na
# sequência. No final, mostre uma listagem de preços, organizando
# os dados em forma tabular.