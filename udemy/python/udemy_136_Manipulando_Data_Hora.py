"""
Data e Hora


"""

import datetime

evento = datetime.datetime(2021, 4, 13)
print(evento)
print(type(evento))

nascimento = input('Qual a data do seu aniversário? (dd/mm/yyyy): ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

# ------------------------------------------------------------------------------------
print()
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

print()
print(dir(evento))
# ------------------------------------------------------------------------------------
