maior=0
menor=0
v=6
for p in range(1,v):
    peso=float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é: {}kg \nO menor peso é: {}kg'.format(maior,menor))

# retornar qual é o maior peso e qual é o menor.