from random import randint
from time import sleep
print('-=-'*6)
print('     \033[1;35mJOKEMPÔ\033[m')
print('-=-'*6)
sleep(.6)
print('\nSuas opções: \n[ 0 ] \033[1;36mPEDRA\033[m\n[ 1 ] \033[1;31mPAPEL\033[m\n[ 2 ] \033[1;35mTESOURA\033[m')
j = int(input('\nQual é a sua jogada? ')) # j de jogador
c = randint(0,2) # c de computador
c = str(c)
j = str(j)

mão={'0':'\033[1;36mPEDRA\033[m',
     '1':'\033[1;31mPAPEL\033[m',
     '2':'\033[1;35mTESOURA\033[m'}

sleep(1)
if c==j:
    print('\nNós dois escolhemos {}!.\n'.format(mão[c]))
else:
    print('\nVocê escolheu {} e eu escolhi {}.\n'.format(mão[j],mão[c]))

c=int(c)
j=int(j)
if c==0 and j==1 or c==1 and j==2 or c==2 and j==0:
    print('\033[1;42mVOCÊ GANHOU DE MIM!! PARABÉNS!!!!\033[m')
elif c==j:
    print('Então empatamos!!!')
else:
    print('\033[1;41mEu GANHEI!!! kkk!!!\033[m')



# Exercício Python 035: Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem ou não formar um triângulo.