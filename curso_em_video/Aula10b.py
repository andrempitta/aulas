# Aula 10
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Sua média é {:.2f} '.format(m))
print('Muito bem! Você ficou acima da média!' if m>=6 else 'Infelizmente você ficou abaixo da média. Estude mais!')


