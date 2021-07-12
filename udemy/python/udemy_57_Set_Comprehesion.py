"""
Set Comprehensio
O SET/CONJUNTO NÃO TEM ORDEM NEM REPETE VALORES

lista = [1, 2, 3]
tupla = (1, 2, 3) # 1, 2, 3
set/conjunto = {1, 2, 3}      <----------------- O SET/CONJUNTO NÃO TEM ORDEM NEM REPETE VALORES
dicionário = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxe:
{valor for valor in interável}

"""
# Exemplos:

numeros = {numero for numero in range(1, 11)}
print(numeros)
print()


# Outros Exemplos:

numeros2 = {x ** 2 for x in range(10)}
print(numeros2)
print()

# DESAFIO, transformar a estrutura acima em dicionário:

numeros2 = {x: x ** 2 for x in range(10)}
print(numeros2)
print()

# úlitmo exemplo:
letras = {letras for letras in 'André Macedo Pitta'}
print(letras, end=" ")