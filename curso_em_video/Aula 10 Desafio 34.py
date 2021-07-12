salario=float(input('Qual o salário do funcionário? '))
if salario >= 1250:
    novo = salario * 1.1
else:
    novo = salario * 1.15
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario,novo))


# if salario >= 1250:
#    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario,salario*1.1))
# else:
#    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario,salario*1.15))



#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor
# do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores
# ou iguais, o aumento é de 15%.