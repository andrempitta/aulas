"""
List Comprehension (Compreensão de Lista??)
- Utilizando Lista Comprehension nós podemos gerar novas listas com dados
processados a partir de outro iterável.

# Sintaxe da List Comprehesion

[ dado for dado in iterávies]
"""

# Exemplos

numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)

"""
Para entender melhor o que está acontecendo devomos dividir a expressão em duas partes:
- A primeira parte: for numero in numeros
- A segunda parte: numero * 10
"""


res1 = [numero / 10 for numero in numeros]
print(res1)


def funcao(valor):
    return valor * valor

res3 = [funcao(numero) for numero in numeros]
print(res3)


#  - - - - - - - - - - - - - - - - - - - -

# List Comprehension vs Loop

# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)
print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in numeros])

# Refatorar mais:

# Loop
numeros_dobrados = []
for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in [1, 2, 3, 4, 5]])


# Outros Exemplos:
#1
nome = 'André Macedo Pitta'
print([letra.upper() for letra in nome])

#2

amigos = ['maria', 'julia', 'joão', 'andre']

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

print([caixa_alta(amigo) for amigo in amigos])

#3

amigos = ['maria', 'julia', 'joão', 'andre']

print([amigo.title() for amigo in amigos])


# ou (mais confuso) assim:
amigos = ['cristina', 'marta', 'maria', 'marcos', 'antonio']
print([amigo.replace(amigo[0], amigo[0].upper()) for amigo in amigos])

#4
print([numero * 3 for numero in range(1, 10)])

#5
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

#6
print([str(numero) for numero in [1, 2, 3, 4, 5]])

