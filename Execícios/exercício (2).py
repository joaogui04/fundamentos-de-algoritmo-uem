#Analise 
#fazer um sistema de reserva que verifica se 2 reservas são comflitantes no horario 
#Tipo de Dados:
# horario: dado em tipo composto
# conflito dado em Enum Reservas
from dataclasses import dataclass
@dataclass
class Horario:
    comeca: float
    termina: float

from enum import Enum, auto
class Reservas(Enum):
    conflito = auto()
    DISPONIVEL = auto()


def conflito(horarios1: Horario, horarios2: Horario) -> str:
    '''
    A funcão vai comparar os 2 começas e o menor vai pegar o *horario1.termina* e ver se é menor com *horario2.começa* caso for então n averá conflito 
    mas caso for maior então averá conflito 

    horarios1 = Horario(8, 12)
    horarios2 = Horario(13,18)
    >>> conflito(horarios1, horarios2)
    DISPONIVEL
    
    horarios1 = Horario(8, 12)
    horarios2 = Horario(11,13)
    >>> conflito(horarios1, horarios2)
    conflito

    horarios1 = Horario(13, 18)
    horarios2 = Horario(8,12)
    >>> conflito(horarios1, horarios2)
    DISPONIVEL

    horarios1 = Horario(11, 13)
    horarios2 = Horario(8, 12)
    >>> conflito(horarios1, horarios2)
    conflito
    '''
    if horarios1.comeca < horarios2.comeca:
        if horarios1.termina <= horarios2.comeca:
            return Reservas.DISPONIVEL.name
        else:
            return Reservas.conflito.name
    
    else:
        if horarios1.comeca >= horarios2.termina:
            return Reservas.DISPONIVEL.name
        else:
            return Reservas.conflito.name


