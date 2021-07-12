# MINHA SOLUÇãO

maior = menor = cont = 0
maiornome = ()
menornome = ()
galera = list()
dado = list()
p = ()
while p != 'N':
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    galera.append(dado[:])
    if dado[1] > maior:
        maior = dado[1]
        maiornome = dado[0]
    if cont == 0:
        menor = dado[1]
        menornome = dado[0]
    else:
        if dado[1] < menor:
            menor = dado[1]
            menornome = dado[0]
    cont += 1
    dado.clear()
    p = input('Quer continuar? [S/N]: ').upper()
print('')
print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi {maior}. Peso de {maiornome}.')
print(f'menor peso foi {menor}. Peso de {menornome}.')