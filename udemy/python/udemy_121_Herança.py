"""
Programação Orientada a Objetos- POO

Herança (Inheritanvce)

A idéia da herança é o reaproveitamento de código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.


Cliente:
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionário:
    - nome;
    - sobrenome;
    - cpf;
    - matrícula;

Existe alguma entidade genérica o suficiente para encapsular os atributos
e métodos comuns a outras entidades?


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Angelina', 'Jolie', '25.123.123-09', 100000)
funcionario1 = Funcionario('João', 'Pedro', '21.335.223-01', 1234)


print(cliente1.nome_completo())
print(funcionario1.nome_completo())

OBS: Quando uma classe herda de outra classe, ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdade é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é conhecida por:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe filha;
    - Classe específica;

 # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    #Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da Super Classe
        self.__renda = renda

class Funcionario(Pessoa):
    #Funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da Super Classe
        self.__matricula = matricula


cliente1 = Cliente('Angelina', 'Jolie', '25.123.123-09', 100000)
funcionario1 = Funcionario('João', 'Pedro', '21.335.223-01', 1234)


print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)


Sobrescrita de Métodos ocorre quando reescrevemos/reimplementamos um método presente na Super Classe em
Classe Filha.

"""

# Sobrescrita de Métodos (Overriding)

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da Super Classe
        self.__renda = renda

class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da Super Classe
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())  # Executa nome_completo da Super Classe.
        print(self._Pessoa__cpf)  # Retorna o atributo cpf em Pessoa
        return f'Funionário: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Angelina', 'Jolie', '25.123.123-09', 100000)
funcionario1 = Funcionario('João', 'Pedro', '21.335.223-01', 1234)


print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)