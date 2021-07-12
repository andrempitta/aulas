print('{:=^40}'.format(' TREINANDO O COMANDO BREAK'))
print('{:=^40}'.format(' TABUADA '))

n = (int(input('Digite o número para mostrar a tabuada dele: ')))
for t in range(1, 11):
    print(f'{n} X {t} = {n * t}')
print('='*20)
while True:
    n = (int(input('Digite o número para mostrar a tabuada dele: ')))
    if n < 0:
        break
    for t in range(1,11):
        print(f'{n} X {t} = {n*t}')

print('Ok, até a próxima!')

print('='*20)



# Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
# quando o número solicitado for negativo.