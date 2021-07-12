
v=float(input('Qual a velocidade do seu veículo? '))
print('Muito bem! Você está dentro do limite de velocidade!' if v <= 80 else 'Infelizmente você foi multado em R${:.2f} por estar {}km/h acima da velocidade máxima!'.format((v-80)*7,(v-80)))

# Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.