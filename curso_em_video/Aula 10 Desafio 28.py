from random import randint
from time import sleep
print('-=-'*18)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-'*18)
computador=randint(0,5)
jogador=int(input('Em que número pensei? '))
sleep(.5)
print('PROCESSANDO . . .')
sleep(2)
print('Muito bem você adinhou o número, parabéns!!!' if jogador == computador else 'Infelizmente você erro! Eu escolhi o número {}'.format(computador))




# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
