
from enum import Enum, auto

class Tipos(Enum):
    BOBINA = auto()
    CHAPA = auto()
    PAINEL = auto()

from dataclasses import dataclass

@dataclass
class Pedido:
    quantidade: int
    Tipodepedido: Tipos
   
@dataclass
class Totalizacao:
    bobina: int
    chapa: int
    painel:int

@dataclass
class TipoProduto:
    Ruptura: Tipos

    #Analise 
    # Dada a demanda de pedidos de três tipos de produtos ira pegar os pedidos e somar com para descobrir qual é a total de pedidos. 

    #Tipos de dados
    # Tipos de produto, quantidade de produto dados em numeros positivos e totalizacão dado em numeros positivos 

T1: Totalizacao = Totalizacao(0 ,0 ,0)

def totaliza_pedidos(pedidos: list[Pedido]) -> Totalizacao:
    '''
    Produz uma estrutura que totaliza a demanda de cada produto
    a partir de *pedidos*.

    Exemplos
    >>> totaliza_pedidos([Pedido(0, Tipos.BOBINA)])
    Totalizacao(bobina=0, chapa=0, painel=0)

    >>> totaliza_pedidos([Pedido(100, Tipos.BOBINA), Pedido(50, Tipos.CHAPA), Pedido(30, Tipos.BOBINA), Pedido(20, Tipos.PAINEL), Pedido(15, Tipos.CHAPA), Pedido(17, Tipos.BOBINA)])
    Totalizacao(bobina=147, chapa=65, painel=20)
    '''
    for pedido in pedidos:
        if pedido.Tipodepedido == Tipos.BOBINA:
            T1.bobina = T1.bobina + pedido.quantidade
        if pedido.Tipodepedido == Tipos.CHAPA:
            T1.chapa = T1.chapa + pedido.quantidade
        if pedido.Tipodepedido == Tipos.PAINEL:
            T1.painel = T1.painel + pedido.quantidade


    return T1


    # Análise 
    # Caso a demanda for maior que o estoque deve mostrar quais os produtos teve ruptura.

    # Tipos de Dados
    # Estoque é dado em numeros positivos, demanda é dado em numeros positivos, são 3 produtos . 

def ha_ruptura(estoque: Totalizacao, demanda: Totalizacao) -> list[str]:
    '''
    Gera a partir do *estoque* e *demanda*, uma lista com os tipos de produtos
    com ruptura do estoque. Se não houver ruptura a lista deve ficar vazia.

    Exemplos
    >>> ha_ruptura(Totalizacao(100,100,100),Totalizacao(150,190,130))
    [TipoProduto(Ruptura='BOBINA'), TipoProduto(Ruptura='CHAPA'), TipoProduto(Ruptura='PAINEL')]

    >>> ha_ruptura(Totalizacao(100,100,100),Totalizacao(150,100,130))
    [TipoProduto(Ruptura='BOBINA'), TipoProduto(Ruptura='PAINEL')]

    >>> ha_ruptura(Totalizacao(100,100,100),Totalizacao(150,100,100))
    [TipoProduto(Ruptura='BOBINA')]

    >>> ha_ruptura(Totalizacao(100,100,100),Totalizacao(100,100,100))
    []
    ''' 
    ruptura = []

    if  demanda.bobina > estoque.bobina:
        ruptura.append(TipoProduto(Tipos.BOBINA.name)) 
    if  demanda.chapa > estoque.chapa:
        ruptura.append(TipoProduto(Tipos.CHAPA.name))
    if  demanda.painel > estoque.painel:
        ruptura.append(TipoProduto(Tipos.PAINEL.name))
    
    return ruptura

    


        
   

