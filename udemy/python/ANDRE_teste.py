

# amigos = ['maria', 'julia', 'joão', 'andre']
# print([amigo.title() for amigo in amigos])


# conjunto = {'abacaxi', 'batata', 'abacaxi', 'arroz', 'cebola'}
# tupla = ('abacaxi', 'batata', 'abacaxi', 'arroz', 'cebola')
# lista = ['abacaxi', 'batata', 'abacaxi', 'arroz', 'cebola']
# print(conjunto)
# conjunto.add('arroz')
# print(conjunto)
# print(tupla)
# lista.append('batata')
# lista.append('batata')
# lista.append('batata')
# print(lista)


# jogo_da_velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1,4)]
# print(jogo_da_velha)

# for a in range(1, 4):
#     print([['*' for i in range(1, 4)]for j in range(1, 4)])


# dic = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# print(dic.keys)
# print(dic.get('c'))
# # dic.popitem()
# quadrado = {chave: valor ** 2 for chave, valor in dic.items()}
# print(quadrado) 

# numeros = [1, 2, 3, 4, 5]
# res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
# print(res)


# a = lambda x: (x*2)**2
# print(a(5))

# def conta(x):
#     return (x*2)**2
# print(conta(5))

# import math
# raios = [1, 2, 3, 4, 5]
# print(list(map(lambda x: math.pi * x**2, raios)))


# lista = (('berlin', 23), ('Brasil', 41), ('Argentina', 23), ('Inglaterra', 10))
# print(lista)
# fahrenheit = lambda x: (x[0], int((9/5 * x[1]) + 32))
# print(list(map(fahrenheit, lista)))


# import statistics
# dados = [1.3, 2.5, 0.8, 4.1, 4.3, 2.15, -0.1]
# ## media = statistics.mean(dados)
# ## print(media)
# ## retorno = filter(lambda x: x >= media, dados)
# retorno = filter(lambda x: x >= statistics.mean(dados), dados)
# print(list(retorno))

