"""
Preservado metadados com wraps

Metadados -> São dados intrínsecos ao arquivo

wraps -> São funções que envolvem elementos com diversas finalidades

"""

"""
# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        #Eu sou uma função (logar) dentro da outra
        print(f'Você está chamndo {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    #Soma dois números
    return a + b

print(soma.__name__)
print(soma.__doc__)
"""

# Resolução do Problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)  # faz com que o __nome__ e __doc__ sejam informados corretamente
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro da outra"""
        print(f'Você está chamndo {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b

print(soma.__name__)
print(soma.__doc__)


