""" Funções parciais """
from operator import add, mul, sub, itemgetter
from functools import partial, reduce
from typing import OrderedDict

soma_2 = partial(add, 2)

reduce(add, [1, 2, 3, 4, 5, 6])
reduce(mul, [1, 2, 3, 4, 5, 6])

a = [1, 2, 3, 4, 5, 6]

somatorio = partial(reduce, mul)
print(somatorio(a))

# -------
soma_2 = partial(add, 2)
mul_2 = partial(mul, 2)

mul_2_all = partial(map, mul_2)

b = mul_2_all(a)
print(list(b))


ordenar_1 = partial(sorted, key=itemgetter(1))

print(ordenar_1([ 'ab', 'aa', 'ac']))

