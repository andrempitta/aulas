"""
Dictionary Comprehensio


Se quisermos criar uma lista fazemos:

lista = [1, 2, 3]

Se quisermos criar uma tupla:

tupla = (1, 2, 3) # 1, 2, 3

Se quisermos criar um conjunto:

conjunto = {1, 2, 3}

Se quisermos criar um dicionário:

dicionário = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxe:
{chave:valor for valor in interável}

"""
# Exemplos:
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items() }
print(quadrado)
print()


numbers = [1, 2, 3, 4, 5, 9, 8, 1, 10] # Reparar que não repeto números, o último 1 não aparece no resultado!
quadrados = {valor: valor ** 2 for valor in numbers}
print(quadrados)
print()


chaves = 'abdcde'
valores = [1, 2, 3, 4, 5, 6]
#print({chaves[i]: valores[i] for i in range(0, len(chaves))})
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
print()


# Exemplo com lógica condicional
numbers = [1, 2, 3, 4, 5, 9, 8, 1, 10]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numbers}
print(res)
print()