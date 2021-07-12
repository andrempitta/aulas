l=float(input('Qual a largura da parde em mentros? '))
h=float(input('Qual a alutra da parde em metros? '))
a=l*h
t=a/2
print('Você precisará de {:.2f} litros de tinta para pintar os {:.2f}m2 de parede.'.format(t,a))