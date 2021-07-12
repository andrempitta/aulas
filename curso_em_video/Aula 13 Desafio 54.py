maior = 0
menor = 0
v=9
for c in range(1,v):
    n=int(input('Digite a idade da {}ª pessoa: '.format(c)))
    if n >= 21:
        n = 1
    else:
        n = 0
    maior += n
menor = v-1 - maior
print('Maior de idade: {}\nMenor de idade: {}'.format(maior,menor))