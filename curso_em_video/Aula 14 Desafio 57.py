print('{:=^40}'.format(' TREINANDO O COMANDO WHILE '))
s = str(input('Qual o sexo [M/F]: ')).upper().strip()
while s not in 'MF':
    s = str(input('Dado incorreto. Digite novamente [M/F]: ')).strip().upper()
if s == 'M':
    print('Sexo Masculino registrado com sucesso!')
elif s == 'F':
    print('Sexo Feminino registrado com sucesso!')

# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.