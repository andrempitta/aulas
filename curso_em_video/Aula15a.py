# Aula 15 - break

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}.'.format(s))
print(f'A soma vale {s}') # PEP - forma melhorada de format à partir da versão 3.6.?


