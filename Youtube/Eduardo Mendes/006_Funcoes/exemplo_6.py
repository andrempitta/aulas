from typing import Callable, Dict
from numbers import Number

calc: Dict[str, Callable] = {
    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y,
}


def soma(x: Number, y: Number) -> Number:
    """ Soma dois números """
    return x + y

def sub(x: Number, y: Number) -> Number:
    """ Subtrai dois números """
    return x - y

def mult(x: Number, y: Number) -> Number:
    """ Multiplica dois números """
    return x * y

def div(x: Number, y: Number) -> Number:
    """ Divide dois números """
    return x / y


calc_nomeado: Dict[str, Callable] = {
    'soma': soma,
    'sub': sub,
    'mult': mult,
    'div': div,
}