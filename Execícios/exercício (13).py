from enum import Enum, auto

class Palavra(Enum):
    DUPLICADA = auto()
    NORMAL = auto()
def dupli(palavra:str) -> str:
    quant = len(palavra)
    metade = quant / 2 
    if metade % 2 != 0:
        quant = round(metade)
        if palavra[quant] == '-':
            return Palavra.DUPLICADA.name
        else:
            return Palavra.NORMAL.name
    else:
        if palavra[:quant] == palavra[quant:]:
            return Palavra.DUPLICADA.name
        else:
            return Palavra.NORMAL.name
