"""
Listas aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java/PHP) possuem uma estrutura chamada array:
    - Unidimensionais (Array/Vetores);
    - Multidimensionais (Matrizes);

Em Python temos as listas

numeros = [1, 2, 3, 4, 5]

"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

print(listas)
print(type(listas))
print(listas[0])
print(listas[0][1]) # 2
print(listas[2][1]) # 8
print(listas[2][-2]) # 8
print(listas[2][-3]) # 7

print()
# Iternado com loops em lista aninhada
for lista in listas:
    for num in lista:
        print(num, end=' ')
print()

print()
# List Comprehension
[[print(num, end=' ') for num in lista] for lista in listas]
print()

# Gerando um tabuleiro ou Matriz 3 x 3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)
print()

# Gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1,4)] for valor in range(1, 4)]
print(velha)
print()
# Gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])
print()