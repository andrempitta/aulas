from _dados import *
from acs.acs_repositorio_relatorios import *

a = '2021-07-27'
a = data_formato(a)
print(a)
print(type(a))


b = '2021-07-28'
b = data_formato(b)
print(b)
print(type(b))

print(a < b)