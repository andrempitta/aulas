# MINHA SOLUÇãO
print('{:=^40}'.format(' TUPLAS '))
print('{:=^40}'.format(' TUPLAS '))
print(30*'=')
print('{:^30}'.format('BANCO ANDRÉ'))
print(30*'=')

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
          'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
          'quatoreze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
          'dezenove','vinte')

while True:
    n=(int(input('Digite um número entre 0 e 20: ')))
    if 0 <= n <= 20:
        break
    print('Tente novamente! ', end='')

print(f'Você digitou o número {numero[n]}.')

resp = ' '
while resp != 'SN':
    resp = str(input('Você quer continuar [S/N]? ')).upper().strip()
    if resp == 'N':
        break
    if resp == 'S':
        while True:
            n=(int(input('Digite um número entre 0 e 20: ')))
            if 0 <= n <= 20:
                break
            print('Tente novamente! ', end='')

        print(f'Você digitou o número {numero[n]}.')

# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com
# uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo
# teclado (entre 0 e 20) e mostrá-lo por extenso.