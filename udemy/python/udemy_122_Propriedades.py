"""
Programação Orientada a Objetos- POO

Propriedades - Properties

Em linguagem de programação com Java, ao declararmos atributos privados nas Classes
costumamos criar métodos públicos para manipulação desses atributos. Estes métodos
são conhecidos por getters e setters, ondem o getter retorna o valor do atributo e
o setter altera o volor do atributo.




class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo {self.__saldo} de titular {self.__titular}'

    def sacar(self, valor):
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


    def get_numero(self):
        return self.__numero

#    def set_numero(self, numero):
#        self.__numero = numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

#    def set_saldo(self, saldo):
#        self.__saldo = saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

conta1 = Conta('Joaquim', 1000, 5000)
conta2 = Conta('Pedro', 400, 3000)

print(conta1.extrato())
print(conta2.extrato())

print(conta1.__dict__)

conta1.set_limite(10000)

print(conta1.__dict__)



"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor


    def extrato(self):
        return f'Saldo {self.__saldo} de titular {self.__titular}'

    def sacar(self, valor):
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Joaquim', 1000, 5000)
conta2 = Conta('Pedro', 400, 3000)

print(conta1.extrato())
print(conta2.extrato())

print(conta1.saldo)

print(conta1.__dict__)
print(conta2.__dict__)

soma = conta1.saldo + conta2.saldo
print(f'Total saldo contas: {soma}')

# limite.setter
print()
print(conta1.__dict__)
conta1.limite = 7654  # limite atuando como setter
print(conta1.__dict__)
print(conta1.limite)  # limite atuando como getter

print(conta1.valor_total)
print(conta2.valor_total)