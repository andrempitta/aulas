print('{:=^40}'.format(' TREINANDO O COMANDO BREAK'))
print('{:=^40}'.format(' TABUADA '))

n = (int(input('Digite o número para mostrar a tabuada dele: ')))
for t in range(1, 11):
    print(f'{n} X {t} = {n * t}')
print('='*20)
while True:
    p = str(input('Gostaria de digitar outro número? [S/N]: ')).upper().strip()
    if p in 'Ss':
        n = (int(input('Digite o número para mostrar a tabuada dele: ')))
        for t in range(1,11):
            print(f'{n} X {t} = {n*t}')
    else:
        print('Ok, até a próxima!')
        break
print('='*20)



# Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
# quando o número solicitado for negativo.