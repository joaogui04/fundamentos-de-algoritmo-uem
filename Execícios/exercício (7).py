#criar uma enumeração q mostre as direçoes 

from enum import Enum, auto

class Direcoes(Enum):
    NORTE = auto()
    SUL = auto()
    LESTE = auto() 
    OESTE = auto()

#criar uma funcão q mostre a direção oposta

def oposto(lado:Direcoes) -> str:
    if lado == Direcoes.NORTE:
        return Direcoes.SUL.name
    if lado == Direcoes.SUL:
        return Direcoes.NORTE.name
    if lado == Direcoes.LESTE:
        return Direcoes.OESTE.name
    if lado == Direcoes.OESTE:
        return Direcoes.LESTE.name
    
#Criar  uma funcao q mostra a direçao a 90 graus

def noventa_graus(lado:Direcoes) -> str:
    if lado == Direcoes.NORTE:
        return Direcoes.LESTE.name
    if lado == Direcoes.SUL:
        return Direcoes.OESTE.name
    if lado == Direcoes.LESTE:
        return Direcoes.SUL.name
    if lado == Direcoes.OESTE:
        return Direcoes.NORTE.name
    
# Criar uma função q mostra o inverso da direção a 90 graus no sentido anti horario

    