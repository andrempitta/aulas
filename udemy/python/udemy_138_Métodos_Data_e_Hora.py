"""
Delta de Data e Hora

data_inicial = 15/05/1975 12:55:32.233445
data_final = 15/05/2021 10:25:12.223566
delta = data_final - data_inicial

"""
import datetime

# Mudança ocorrendo a meia noite combinada

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# ----------------------------------------------------------------------------------------------
print(f'-_'*30, end='\n\n')

# Formatando datas e horas com strfime() (string format time)
# dd/mm/yyy hora:min
hoje = datetime.datetime.today()

print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)

# ----------------------------------------------------------------------------------------------
print(f'-_'*30, end='\n\n')
"""
# Encontrar o dia da semana
print(manutencao.weekday())
# Vai de 0 segunda-feira até 6 domingo.

aniversario = input('Digite a data do seu aniversário: ')
aniversario_format = datetime.datetime.strptime(aniversario, '%d/%m/%Y')

if aniversario_format.weekday() == 0:
    print('Você nasceu numa segunda-feira!')
elif aniversario_format.weekday() == 1:
    print('Você nasceu numa terça-feira!')
elif aniversario_format.weekday() == 2:
    print('Você nasceu numa quarta-feira!')
elif aniversario_format.weekday() == 3:
    print('Você nasceu numa quinta-feira!')
elif aniversario_format.weekday() == 4:
    print('Você nasceu numa sexta-feira!')
elif aniversario_format.weekday() == 5:
    print('Você nasceu num sábado!')
elif aniversario_format.weekday() == 6:
    print('Você nasceu num domingo!')
"""

# ----------------------------------------------------------------------------------------------
print(f'-_'*30, end='\n\n')

def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'


print(formata_data(hoje))
# ----------------------------------------------------------------------------------------------
print(f'-_'*30, end='\n\n')


from textblob import TextBlob

# Atenção! textblob traduz através da internet !
def format_data_2(data):
     return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

print(format_data_2(hoje))

# ----------------------------------------------------------------------------------------------
print(f'-_'*30, end='\n\n')
"""
nascimento2 = datetime.datetime.strptime('10/04/1989', '%d/%m/%Y')
print(nascimento2)

nascimento3 = input('Qual a sua data de nascimento?: ')
nascimento3 = datetime.datetime.strptime(nascimento3, '%d/%m/%Y')
print(nascimento3)
"""
# ----------------------------------------------------------------------------------------------
print(f'-_'*30, end='\n\n')

# Somente a hora

almoco = datetime.time(12, 0, 0)
print(almoco)

# ----------------------------------------------------------------------------------------------
print(f'-_'*30, end='\n\n')

import timeit

# Marcando o tempo de execução com do nosso código com o timeit

# Loop For
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comphension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)

# ----------------------------------------------------------------------------------------------
print(f'-_'*30, end='\n\n')

import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

# print(teste(5))

print(timeit.timeit(functools.partial(teste, 2), number=10000))



