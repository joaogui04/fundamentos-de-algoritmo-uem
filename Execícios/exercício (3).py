#fazer uma funcao para dectectar se o numero é positivo ou negativo ou 0
#se for 0 vai devolver 0 se for posit
from enum import Enum, auto

def surpresa(numero: int) -> int:
    '''
    >>> supresa(0)
    0
    >>> supresa(-2)
    -1
    >>> supresa(4)
    1
    
    '''
    if numero == 0: 
        return 0
    elif numero > 0: 
        return 1
    else:
        return -1 