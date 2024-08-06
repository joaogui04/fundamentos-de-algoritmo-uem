#criar enum do elevador q fica entre parado, subir e decer

from enum import Enum, auto

class Elevador(Enum):
    PARADO = auto()
    SUBINDO = auto()
    DESCENDO = auto()

# a condição sera qual o andar mais alto pois do andar mais alto vc vem atendendo todos os outros de cima para baixo pois 
def elevador_andar(andaratual:int, andarchamado:int) -> str:
    '''
    >>> elevador_andar(2,4)
    'SUBINDO'
    >>> elevador_andar(3,3)
    'PARADO'
    >>> elevador_andar(4,2)
    'DESCENDO'

    ''' 

    if andaratual < andarchamado:
        return Elevador.SUBINDO.name
    elif andaratual > andarchamado:
        return Elevador.DESCENDO.name
    else: # andaratual == andarchamado:
        return Elevador.PARADO.name
    




    
