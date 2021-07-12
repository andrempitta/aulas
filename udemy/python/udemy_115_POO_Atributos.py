"""
Programação Orientada a Objetos- POO

POO - Atributos:

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos nós conseguimos
representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em três grupos:
    - Atributos de Instância;
    - Atributos de classes;
    - Atributos Dinâmicos;

# Atributo de Instância: São atributos declarados dentro do método construtor.

# OBS: Método construtor: É um método especial utilizado para a construção do objeto.

Em Java um clase lâmpada incluidno seus atributos ficaria mais ou menos:

public Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }

    public int getVoltagem(){
        return this.voltagem;

    }
}

Em Python ficou estabelecido que todo atributo de uma clase é público
Ou seja, pode ser acessado em todo o projeto.
Caso queriamos demonstrar que determinado Atributo deve ser trado com
privado, ou seja, que deve ser acessado/utilisado somente dentro da
própria classe onde está declarado, utilisa-se '__' (duplo underscore)
antes de seu nome.

Isso é conhecido como 'name Mangling'

"""


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
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# ______________________________________________________________________________________
print()
# Lembre-se que isso é apenas uma conveção, ou seja, a linguagem python não vai impedir
# que façamos o acesso aos atributos.

user = Acesso('apitta@hotmail.com', '123456')

print(user.email)
# print(user.__senha) # AtributeError

print(dir(user))

print(user._Acesso__senha) # Temos acesso. Mas não deveriamos fazer este acesso. Isso é o ('name Mangling')
# ______________________________________________________________________________________

# ______________________________________________________________________________________
print()
user.mostra_senha()
user.mostra_email()

# O que significa Instânia de uma classe?
# Significa que ao criarmos uma instância/objeto de uma classe, todas as instâncias terão
# estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()
# ______________________________________________________________________________________

# ______________________________________________________________________________________
print()
# Atributo de Classe:

p1 = Produto('PlayStarion 4', 'Video game', 2300)
p2 = Produto('XBox S', 'Video game', 4500)

# Atributos de classe são atributos que são declarados diretamente na classe. Ou seja,
# fora do construtor. Geralmente já inicializamos um valor e este valor é compartilhado
# entre todas as instâncias da classe. Ou seja, ao invés de cada instância da Classe ter
# seus próprios valores como é o caso dos atributos de instância, com o atributo de Classe
# todas as instâncias terão o mesmo valor para este atributo.

# Refatorar a classe Produto:


class Produto:

    # Atributo de Classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0
    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


# ______________________________________________________________________________________
p3 = Produto('PlayStarion 4', 'Video game', 2300)
p4 = Produto('XBox S', 'Video game', 4500)

print(p3.imposto) # Acesso possível, porém, incorreto! Forma errada de ter acesso ao Atributo de Classe.
print(p4.imposto)
print(p3.valor)
print(p4.valor)

# Não precisamos criar uma instância de uma classe para fazer acesso  a um atributo de classe.

print(Produto.imposto) # Acesso correto de um Atributo de Classe.
print(p3.id)
print(p4.id)


# Em linguagem com o Java, os atributos conhecidos com Atriburos de Classe no Python são
# são chamados de atributos estáticos
# ______________________________________________________________________________________

# Atributos Dinâmicos -> Um atributo de instânia que pode ser criado em tempo de execução.

# OBS: O Atributo Dinâmico será esclusivo da instância que o criou.

p5 = Produto('PlayStarion 5', 'Video game', 5900)
p6 = Produto('Arroz', 'Mercearia', 5.3)

# Criando um atributo dinâmico 'em tempo de execução.

p6.peso = '5kg'
print(f'Produto:{p6.nome}, descrição:{p6.descricao}, valor:R${p6.valor}, peso:{p6.peso}.')

# Deletando atributos

print(p5.__dict__)
print(p6.__dict__)

# print(Produto.__dict__)

del p6.peso
del p6.valor
del p6.descricao

print(p5.__dict__)
print(p6.__dict__)





"""


class Lampada:

    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligado = False


    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def ligado(self):
        return self.__ligado




class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


class Int:
    pass

"""