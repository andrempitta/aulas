"""
Força tipo de dados com Decorators

"""



def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_arg = []
            for (valor, tipo) in zip(args, tipos):
                novo_arg.append(tipo(valor))
            return funcao(*novo_arg, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)
repete_msg('ai ai ', '2')



@forca_tipo(float, float)
def divide(a, b):
    return a/b

print(divide('10.2', '5.3'))