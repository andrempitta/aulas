import random
a1=input('Digite o nome do 1º aluno: ')
a2=input('Digite o nome do 2º aluno: ')
a3=input('Digite o nome do 3º aluno: ')
a4=input('Digite o nome do 4º aluno: ')
a5=input('Digite o nome do 5º aluno: ')
a6=input('Digite o nome do 6º aluno: ')
lista=[a1,a2,a3,a4,a5,a6]
random.shuffle(lista)
print('A ordem da lista será:')
print((lista))
print('A ordem alfabética dessa lista é:')
print(sorted(lista))
