"""
Utilizando Lambdas

Conhecidas por expressões ou simplesmente Lambdas são funções sem nome, ou seja,
funções anonimas.

"""

# Função em Python:

def funcao(x):
    return 3 * x + 1

print(funcao(7))
print(funcao(4))

print()

# Expressão Lambdas:
lambda x: 3 * x + 1

# E como utilizar a expressão lambda

calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))
print()
# Podemos ter expressões lambdas com múltiplas entradas:

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('andré', 'pitta'))
print(nome_completo('  andré', ' PITTA   '))
print()


amar = lambda : 'Como não amar Python?!'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x2, ..., xn: <expressão>

print(amar())
print(uma(6))
print(duas(3, 2))
print(tres(3, 4, 5))
print()
"""
Se passarmos mais de argumentos que o pedido pelo função teremos TypeError
"""

# Outro exemplo:

autores = ['Issac Assimov', 'Pedro Paulo', 'Paulo Coelho', 'John Cooke', 'Alexandre Duma', 'H. G. Wells', 'Arthur C. Clark', 'Orson Scott Card']
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

# Funções Quadraticas
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    """
    Retorna a função f(x) = a * x ** 2 + b * x + c
    """
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))