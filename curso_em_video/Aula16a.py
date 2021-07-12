# Aula 16 - tupla

lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer comida {comida}')
print('')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {(lanche[cont])} na posição {cont}.')
print('')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')