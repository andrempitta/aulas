"""
Programação Orientada a Objetos- POO

Método super()

O método se refere a Super Classe:


"""

class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')

class Gato(Animal):

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)  # Possível mas não recomendado
        super().__init__(nome, especie)
        super().faz_som('auauauauauauau')
        self.__raca = raca


felix = Gato('Felix', 'Felino', 'Angorá')
felix.faz_som('miau')
