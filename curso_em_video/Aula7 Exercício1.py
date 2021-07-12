n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma é {}, a multiplicação {}. \nDivisão é {:.3f}'.format(s,m,d), end='')
print(' a divisão inteira {} e potência {}.'.format(di,e))
