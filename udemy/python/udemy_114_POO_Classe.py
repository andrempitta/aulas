"""
Programação Orientada a Objetos- POO

POO - Classe:

Em POO, Classes nada mais são do que modelos de objetos do mundo real sendo representados
computacionalmente,

Imagine que você queira fazer um sistema para poder automatizar o controle das lâmpadas da
sua casa.

Classes podem conter:

    - Atributos -> Representam as característica do objeto. Ou seja, pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente  iríamos
    querer saber se a lâmpada é 110 ou 220v, qual a cor, qual a luminozidade, etc.;

    - Metodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que esses objetos
    podem realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito
    provavelmente iriamos querer representar no nosso sistema é o de ligar e desligar a lâmpada.


Em python para definirmos uma classe usamos a palavra reservada 'class'.

Utilizamos a palavar 'pass' em Python quando temos um bloco de código que ainda não está implementado.

OBS: Quando nomeamos nossas classes em Python, utilisamos por convenção o nome com inicial em maiúsculo.
Se o nome for composto, utiliza-se as iniciais de ambas as palavras em maiúsculo, todas juntas.

Dica Geek, em computação não utilizamos: Acentuação, caracteres especiais, espaços ou similares para
nomes de classes, atributos, métodos, arquivos, diretorios, etc.

OBS: Quando estamos planejando um software e definimos quais clases teremos que ter no sistema, chamamos
estes obejtos que serão mapeados para classes de 'entidade'
"""


numero = 10
preco = 234.23
nome = 'Felicity Jones'
"""
print(type(numero))
print(type(preco))
print(type(nome))
"""

# como representar uma lâmpada?
# Criando uma classe!



class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligado = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos ou Privados


class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha


user = Acesso('apitta@hotmail.com', '123456')


print(user.email)
print(user.__senha) # AtributeError