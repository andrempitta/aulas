n=int(input('Digite um número que te mostrarei todos os pares inteiros desse intervalo: '))

for c in range(2,n+1,2):
    print('.', end='')
    print(c, end=' ') # end=' ' é para não ir para outra linha, colococando a sequência linar e não em coluna.
print('FIM')

# Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.