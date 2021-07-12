"""
Programação Orientada a Objetos- POO

POO - Métodos (funções) -> Representam os comportamentos dos objetos. Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em python dividimos os Métodos em 2 grupos: Método de instância de Método de Classe.

# Método de instância

# O método dunder int __int__ é o método especial chamado construtor e sua função é
construir o objeto à partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

OBS: Os métodos/funções dunder em python são chamados de métodos mágicos.
ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder (underline no início e no fim da palavra)
não é aconselhado pois o Python possue vários métodos com essa forma de nomenclatura o que pode provocar mudança no
comportamento dessas funções mágicas internas da linguagem. Então, evite ao máximo, de preferença nunca crie.

Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por underlines.

"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade ):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, produto, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__produto = produto
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp  # encryptar a senha da Classe Usuario.

"""
class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
"""
# ______________________________________________________________________________________

"""
p1 = Produto('PlayStation 4', 'Video game', 2300)
print(p1.desconto(20))
print(Produto.desconto(p1, 20))

# ______________________________________________________________________________________

# ______________________________________________________________________________________
user1 = Usuario('Angelina', 'Jolie', 'angelinajolie@gmail.com', '123')
user2 = Usuario('Felicity', 'Jones', 'felicityjones@gmail.com', '321')

print(user1.nome_completo())
print(Usuario.nome_completo(user1)) # outra forma de acessar

print(user2.nome_completo())

print(f'A senha do user1: {user1._Usuario__senha}')
print(f'A senha do user2: {user2._Usuario__senha}')
# ______________________________________________________________________________________
"""

# Métodos de Classe:

class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @staticmethod
    def teste():
        return '1234'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


# ______________________________________________________________________________________
user = Usuario('André', 'Pitta', 'apitta@hotmail.com', '123456')
user2 = Usuario('Ludmila', 'Pitta', 'ludmila@hotmail.com', '123456')
Usuario.conta_usuarios() # maneira correta
user.conta_usuarios() # maneira incorreta


# ______________________________________________________________________________________
# Usando a função com o cryp

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')
if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere!')
    exit(42)
print('Usuário criado com sucesso!')

senha = input('Informe a senha: ')

if user.checa_senha(senha):
    print('Acesso autorizado')
else:
    print('Acesso negado!')
print(f'Senha User Criptografada: {user._Usuario__senha}')   # Acesso errado!




