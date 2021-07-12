"""
Decoradores com diferentes assinaturas

Para resolver usa-se o padrão de projeto chamdo Decorator Patern

A assinatura de uma função é representada pelo seu retorno, nome e parámetros de entrada.

"""

# Relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome.upper())
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}.'

print(saudacao('andré'))


def gritar2(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar2
def saudacao2(nome):
    return f'Olá, eu sou o {nome}.'


@gritar2
def ordenar(principal, acompanhamento):
    return f'Olá, eu gosto de {principal}, acompanhado de {acompanhamento}, por favor.'


print(saudacao2('andré'))
print(ordenar('Picanha', 'batata frita'))


# OBS: Vale lembrar que podemos usar parâmetros nomeados

print(ordenar(acompanhamento='Batata', principal='Picanha'))

#___________________________________________________________________

# Decorator com arqumentos:

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto. O primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna



@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma(num1, num2):
    return num1 + num2


# Testando

print(soma(10, 12)) # 22

print(soma(1, 21)) # 22 erro

print(comida_favorita('pizza', 'cachorro-quente'))
print(comida_favorita('cachorro-quente', 'pizza'))