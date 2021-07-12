"""
O parâmetro *args em funções coloca s valores extras informados com entrada em
uma tupla. Lembrando que tuplas são imutávies.

"""



def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros(1, 2, 3, 6, 7, 8, 14))


lista=(1, 2, 3, 4)
print(soma_todos_numeros(*lista)) # O asteriscos representa o desempacotamento da lista
