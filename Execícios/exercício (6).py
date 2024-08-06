#fazer uma funcão para descobrir de um numero inteiro está mais proximo de 0 ou de 100 
from enum import Enum, auto

class Mais(Enum):
    CEM = 100
    ZERO = 0


def maisperto(numero:int) -> int:
    '''
>>> maisperto(20).name
0

>>> maisperto(50).name 
100

>>> maisperto(80).name
100

    '''
    if numero == 50:
        return Mais.CEM.value
    elif numero > 50:
        return Mais.CEM.value
    else: # numero < 50:
        return Mais.ZERO.value

