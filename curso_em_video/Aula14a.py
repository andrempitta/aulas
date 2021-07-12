# Aula 14 - while
n=1
p = i = 0 # p=par e i=impar
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # para desconsiderar o 0 como número par!
        if n % 2 == 0:
            p = p + 1
        else:
            i += 1
print('Você lançou {} números pares e {} números impares!'.format(p,i))
print('Acabou')


#r = 'S'
#while r == 'S': # != é o simbolo de 'diferente de'
#    n=int(input('Digite um valor: '))
#    r = str(input('Quer continuar inserino valores [S/N]? ')).upper()
#print('Fim')



#for c in range(1, 10):
#    print(c)
#print('Fim')



#c=1
#while c <10:
#    print(c)
#    c = c + 1
#print('Fim')