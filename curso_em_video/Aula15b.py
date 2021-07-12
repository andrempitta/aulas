# Aula 15 - break

nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.')  # PEP - forma melhorada de format à partir da versão PYTHON 3.6+
print('O {} tem {} anos.'.format(nome, idade)) # PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) # a partir do PYTHON 2

salario = 987.35
print(f'O {nome:^10} tem {idade:20} anos e ganha R${salario:^20.2f}.') # Formatação representa-se dessas formas
