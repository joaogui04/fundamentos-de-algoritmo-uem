from dataclasses import dataclass
@dataclass
class Tipo:
    gasto: float
    recebimento: float

def doacao(inicial: float, lista: list[Tipo]) -> int:
    contagem = 0
    for x in lista:
        rec = x.recebimento
        gas = x.gasto
        top = rec + gas
        inicial = inicial + top
        if inicial < 0:
            contagem + 1
    return contagem * 10
