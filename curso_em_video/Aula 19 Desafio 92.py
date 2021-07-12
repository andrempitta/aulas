# RESOLUCAO PROFESSOR

from datetime import datetime
dados = dict()

dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Qual o ano da contratação?: '))
    dados['salario'] = int(input('Qual o salário?: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-='*20)
for k, v in dados.items():
    print(f' - {k}: {v}')





"""
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira
de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for 
diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""