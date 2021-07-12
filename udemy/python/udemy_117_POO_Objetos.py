"""
Programação Orientada a Objetos- POO

Objetos -> Instâncias das classes. Ou seja, após o mapeamento do objeto do mundo real para
sua representação computacional, devemos  poder criar quantos objetos quantos forem necessário.
Podemos pensar nos objetos/instâncias de uma classe como variáveis do tipo definido na classe.

"""

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:  # É o mesmo que -> if self.__ligada == True:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz: Oi!')

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        return f'Nome:{self.__cliente._Cliente__nome} CPF:{self.__cliente._Cliente__cpf}'


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def mostra_email(self):
        return self.__email

cli1 = Cliente('André', '26.435.344-3')

cc1 = ContaCorrente(5000, 1000, cli1)

print(cc1.mostra_cliente())

cc1._ContaCorrente__cliente.diz() # Acesso de maneira errada



"""

lamp1 = Lampada('branco', 220, 60)

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')
lamp1.ligar_desligar()
print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')
lamp1.ligar_desligar()
print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 1000)

user1 = Usuario('Andre', 'Pitta', 'apitta@hotmail.com', '1234')

print(type('André Macedo'))
print(type(10))
print(type(user1))

print(user1.mostra_email())
"""


