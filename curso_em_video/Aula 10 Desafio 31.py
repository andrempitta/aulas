d=float(input('Qual a distância (em km) da sua vaigem? '))
print('Você está prestes a começar uma viagem de {:.0f}Km.'.format(d))
preço = d * 0.5 if d<=200 else d * 0.45
print('Sua passagem custará R${:.2f}'.format(preço))




#if d<=200:
#    print('Sua passagem custará {:.2f}'.format(d * 0.5))
#else:
#    print(''Sua passagem custará' {:.2f}'.format(d*0.45))




# print('Sua passagem custará {:.2f}'.format(d*0.5) if d<=200 else 'Sua passagem custará {:.2f}'.format(d*0.45))



# Exercício Python 031: Desenvolva um programa que pergunte a distância de
# uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.