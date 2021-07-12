"""
Nas funções podemos ter nessa ordem:

- Parâmetros obrigatórios;
- *args;
- Parâmetros não obrigatórios;
- **kwargs;

"""
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Casado')
    else:
        print('Solteiro')
    print(kwargs)
    print()

minha_funcao(8, 'Juliana')
minha_funcao(12, 'Pedro', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, Java=False, Phyton=True)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def soma_tudo(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_tudo(*lista)
soma_tudo(*tupla)
soma_tudo(*conjunto)


dicionario = dict(a=1, b=2, c=3)

soma_tudo(**dicionario)

"""
Os nomes das chaves do dicionário devem ser os mesmos da função. Caso contrário, dará erro TypeError:
Exemplo:

dicionario = dict(d=1, e=2, f=3)

soma_tudo(**dicionario)

"""