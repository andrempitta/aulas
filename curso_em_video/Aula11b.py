# Aula 11

print('\033[1;31;43mOlá Mundo\033[m')
print('')
print('\033[7;30;43mOlá Mundo\033[m')
print('')
a=float(input('1º número: '))
b=float(input('2º número: '))

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))

#

nome='André'

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('\nOlá Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'],nome,cores['limpa']))


#print('\033[0;30;41m TESTE \033[m')
#print('\033[4;33;44m TESTE \033[m')
#print('\033[1;35;43m TESTE \033[m')
#print('\033[30;42m TESTE \033[m')
#print('\033[m TESTE')
#print('\033[7;30m TESTE \033[m')