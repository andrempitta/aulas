# Aula 16 - tupla

lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(sorted(lanche)) # comando sorted não altera a Tupla mas coloca em ordem
print(lanche)

print('')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print('')
print(c.count(5)) # vai contar quantos 5 aparecem na tupla c
print('')
print(c.index(8)) # retorna em que posção o 8 se encontra na Tupla (começa contando com 0!)
print(c.index(5, 2)) # retorna a posição do 5 à partir da posição 2 ignorando a posição 0 e 1!