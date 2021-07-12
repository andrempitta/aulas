"""
Funções de maior grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma lingagem de programação suporta/permite o conceito HOF indica que podemos ter funções que retornam outras
funções como resultado ou mesmo que podemos passar funções como argumento para outras funções, e até mesmo criar variáveis
do tipo de funções nos nossos programas.

OBS: Na seção de funções, nós usamos isso.

Em Python as funções são Cidadões de Primeira Classe - First Class Citizen
"""

# Exemplo definindo as funções:

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def dividir(a, b):
    return a / b


def multiplicar(a, b):
    return a * b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções

print(calcular(3, 5, dividir))
print(calcular(3, 5, somar))
print(calcular(3, 5, subtrair))
print(calcular(3, 5, multiplicar))

# ______________________________________________________________________________________
# Nested Functions - Funções aninhadas


# No Python podemos ter funções dentro de funções que são conhecidas como Nested Function
# ou também com Inner Functions (Funções Internas)

# Exemplo:

"""

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai?', 'Suma daqui!', 'Gosto muito de você,', 'Agora não!', 'Não me perturbe,'))
    return humor() + ' ' + pessoa + '.'

print(cumprimento('Angela'))
print(cumprimento('Pedro'))
"""


# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice('hahahahahaha', 'kkkkkkkkkk', 'yayayayayayayaya')
    return rir

# Testando

rindo = faz_me_rir()

print(rindo)