"""
Programação Orientada a Objetos- POO

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico
utilizando classes.

Encapsular -> cápsula

            classe
-------------------------------
/                             /
/     atributos e métodos     /
/_____________________________/

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa contendo
um atributo privado chamodo __nome e um método privado
chamado __falar().

Esses elementos privados só devem/deveriam ser acessados
dentro da classe, mas o Python não bloqueia esse acesso
fora da classe. Com o Python acontece um fenômeno chamada
Name Mangling que faz uma alteração na forma de se acessar
os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome
instancia.Pessoa__falar()


Abstração em PPO é o ato de expor apenas os dados relevantes de uma classe, escondendo
atributos e métodos privados de usuário.

"""

"""
class Conta:

    contador = 400
    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1


    def extrato(self):
        return f'Saldo {self.saldo} do {self.titular} com limite de {self.limite}.'


    def depositar(self, deposito):
        self.saldo += deposito

    def sacar(self, saque):
        self.saldo -= saque



# Testar

cc1 = Conta('André', 1000, 5000)

print(cc1.numero)
print(cc1.titular)
print(cc1.saldo)
print(cc1.limite)

cc1.numero = 1
cc1.titular = 'Antonio'
cc1.saldo = 100000
cc1.limite = 1000000000

print(cc1.__dict__)
"""

class Conta:

    contador = 400
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1


    def extrato(self):
        print(f'Saldo {self.__saldo} do titular {self.__titular} com limite de {self.__limite}.')


    def depositar(self, deposito):
        if deposito > 0:
            self.__saldo += deposito
        else:
            print('Você precisa informar um valor maior que Zero!')


    def sacar(self, saque):
        if saque > 0:
            if saque > self.__saldo:
                print('Saldo insuficiente!')
            else:
                self.__saldo -= saque
        else:
            print('Você precisa informar um valor maior que Zero!')


    def transefir(self, valor, conta_destino):
        # 1) Remover o valor da conta de origem:
        self.__saldo -= valor
        self.__saldo -= 10  # taxa de transferência
        # 2) Adicionando o valor da conta de destino:
        conta_destino.__saldo += valor


# Testando
"""
cc1 = Conta('André', 1000, 5000)

print(cc1.__dict__)

print(cc1._Conta__titular)  # Name Mangling | não se deve fazer!
cc1._Conta__titular = 'Antonio'

print(cc1.__dict__)

cc1.depositar(-300)
print(cc1.__dict__)
cc1.sacar(10000)
print(cc1.__dict__)
"""

cc1 = Conta('André', 1000, 5000)
cc2 = Conta('Marcos', 300, 5000)

cc1.extrato()
cc2.extrato()

cc1.transefir(100, cc2)

cc1.extrato()
cc2.extrato()