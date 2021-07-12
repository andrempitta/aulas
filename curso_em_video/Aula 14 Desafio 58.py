print('{:=^40}'.format(' TREINANDO O COMANDO WHILE '))

from random import randint
from time import sleep

print('-=-'*19)
print('Vou pensar em um número de 0 a 10. Tente adivinhar...')
print('-=-'*19)
computador=randint(0,10)
jogador=int(input('Em que número pensei? '))
conta = 1
sleep(.5)
while computador != jogador:
    jogador = int(input('Não foi esse! Tente novamente: '))
    conta += 1
else:
    sleep(0.8)
    print('\nMuito bem! O número que pensei foi \033[34m{}\033[m. Você acertou na \033[34m{}ª\033[m tentativa!'.format(computador,conta))


#print('PROCESSANDO . . .')

#print('Muito bem você adinhou o número, parabéns!!!' if jogador == computador else 'Infelizmente você erro! Eu escolhi o número {}'.format(computador))


# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.