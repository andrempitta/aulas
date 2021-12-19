from functools import singledispatch

class Pedra: pass
class Papel: pass
class Tesoura: pass

@singledispatch
def jokenpo(p1, p2):
    print(p1, p2)

@jokenpo.register(Pedra)
def pedra_entrada(p1, p2):
    return 'Pedra' if isinstance(p2, Tesoura) else 'Papel' if isinstance(p2, Papel) else 'Empate'

