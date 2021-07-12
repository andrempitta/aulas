print('-=-'*10)
print('Analisando Triângulos')
print('-=-'*10)
r1=float(input('Primeiro segmento: '))
r2=float(input('Segundo segmento: '))
r3=float(input('Terceiro segmento: '))

if r1<r2+r3 and r3<r1+r2 and r2<r3+r1:
    print("Os segumento PODEM formar um triângulo")
else:
    print('Os segmentos NÃO PODEM dormar um triângulo')

# Exercício Python 035: Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem ou não formar um triângulo.