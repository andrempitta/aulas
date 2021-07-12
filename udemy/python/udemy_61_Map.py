"""
Map

Com Map fazemos mapeamento de valores para função.
"""

import math

def area(r):
    """Calcula a área de um circulo com raio r"""
    return math.pi * (r ** 2)
print(area(2))
print()


raios = [2, 3, 4, 5, 7, 10]
areas = []
for r in raios:
    areas.append((area(r)))
print(areas)
print()

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável. Retorna um Map Object.

areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))
print()

# Forma 3 Map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))
# Após a utilização da função map() depois da primeira utilização do resultado ele ZERA.

"""
Para fixar a função map():
Temos dados iteráveis:
dado: a1, a2, ... , an
Temos a função:
função: f(x)
Utilizamos a função map(f, dados) onde irá mapear cada elemento dos dados e aplicar a função:
O Map Object: f(a1), f(a2), f(...), f(an)

"""

# Mais exemplos:

cidades = [('Berlim', 29),('Cairo', 29),('Los Angeles', 20), ('Tokio', 17), ('Nova York', 13), ('Londres', 22)]
celsius = lambda dado: (dado[0], f'{dado[1]}°C')
print(list(map(celsius, cidades)))
print()

# f = 9/5 * c + 32 <- coverter para Fahrenheit
c_para_f = lambda dado: (dado[0], f'{9/5 * dado[1] + 32:.2f}°F')
print(list(map(c_para_f, cidades)))
print()

