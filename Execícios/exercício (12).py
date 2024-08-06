from dataclasses import dataclass
@dataclass
class Diass:
    dia: int
    mes: int
    ano: int

def ultimo(ultano: Diass) -> bool:
    '''
    ultano = Diass(31, 12, 2004)
    >>> ultimo(ultano)
    True
    ultano = Diass(2, 3, 2004)
    >>> ultimo(ultano)
    False
    '''
    if ultano.dia == 31:
        if ultano.mes == 12:
            return True
        else:
            return False
    else:
        return False


def qual_vem_antes(data1: Diass ,data2: Diass) -> bool:
    '''
    Funcão pega as 2 datas e retorna true se a *data1* for antes da *data2*

    data1 = Diass(21, 2, 2004)
    data2 = Diass(21, 1, 2004)
    >>> qual_vem_antes(data1,data2)
    False

    data1 = Diass(12, 1, 2004)
    data2 = Diass(21, 1, 2004)
    >>> qual_vem_antes(data1,data2)
    True 

    data1 = Diass(21, 1, 2004)
    data2 = Diass(21, 1, 2005)
    >>> qual_vem_antes(data1,datas2)
    True

    '''
    if data1.ano < data2.ano:
        return True
    elif data1.ano > data2.ano:
        return False
    else:
        if data1.mes < data2.mes:
            return True
        elif data1.mes > data2.mes:
            return False
        else:
            if data1.dia < data2.dia:
                return True
            else:
                return False
            




