"""
Programação Orientada a Objetos- POO

Herança (Inheritanvce) Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma Classe herdar de múltiplas Classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

OBS: A herança múltipla pode ser feito de duas maneiras.
    - Multiderivação Direta
    - Multiderivação Indireta


# Multiderivação Direta

class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass

# Multiderivação Indireta



class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass


OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará todos os
atributos e métodos das Super Classes.

"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu {self._Animal__nome} sou da terra!'


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super().__init__(nome)


# Testando:

baleia = Aquatico('Wally')

print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

pinguim = Pinguim('Tux')
print(pinguim.andar())
print(pinguim.nadar())
print(pinguim.cumprimentar())  # Eu sou Tux da Terra / Eu sou Tux do Mar ????? ->  Method Resolution Order - MRO