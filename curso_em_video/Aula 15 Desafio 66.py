print('{:=^40}'.format(' TREINANDO O COMANDO BREAK'))
print('{:=^40}'.format(' TREINO WHILE E BREAK '))

cont = soma = 0
while True:
    n = (int(input('Digite um número: [Digite 999 para parar] ')))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} números e a soma deles é {soma:.2f}')




# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição
# de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre elas (desconsiderando o flag).