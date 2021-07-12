# MINHA PROFESSOR
def escreva(msg):
    tam = len(msg) + 4
    print('˜' * tam)
    print(f'  {msg}')
    print('˜' * tam)

escreva('André Macedo Pitta')
escreva('Marcela Linda da Silva Chavier Fonseca')
frase = input(f' Escreva uma frase: ')
escreva(frase)

"""
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""