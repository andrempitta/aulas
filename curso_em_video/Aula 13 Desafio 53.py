print('\033[34m{:✶^40}\033[m'.format(' PALÍNDROMO '))

frase=str(input('Escreva uma frase (sem acentuação): ')).lower().strip().split()
junto=''.join(frase)
invertido=''.join(junto[::-1])

print(junto)
print(invertido)

if junto == invertido:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')


# for letra in range(len(junto) - 1, -1, -1):
# inverso += jonto[letra]
# print(junto,inverso)


# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.