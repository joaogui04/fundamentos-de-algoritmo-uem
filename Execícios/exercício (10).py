from dataclasses import dataclass
@dataclass
class Resolucao:
    largura: int 
    altura: int

from enum import Enum, auto
class Tipoderesolucao(Enum):
    Dezesseispornove = auto()
    Quatroportres= auto()

def pixels(resolucao: Resolucao) -> float:
    '''
    Descobrir quantos megapixel tem a resolucao dado q altura vezes lagura dividido por 1 milhão vai ser a quantidade de megapixel 

        resolucao = Resolucao(1920, 1080)
    >>> pixels(resolucao)
        2.0736

        resolucao = Resolucao(1200, 1200)
    >>> pixels(resolucao)
        1.44
 
    '''
    return (resolucao.altura * resolucao.largura) / 1000000

def Verifica_tela(tela: Resolucao, resolucao:Resolucao) -> bool:
    '''
    verificar se a imagem pode ser exibida na tela  sem qualquer tipo de reduçao de tamanho ou rotação  

    tela = Resolucao(1920 , 1080)
    resolucao = Resolucao (1200, 1200) 
    >>> Verifica_tela(tela, resolucao)
    True

    tela = Resolucao(1920, 1080)
    resolucao = Resolucao(2560, 1080)
    >>> Verifica_tela(tela, resolucao)
    False

    '''
    tamanho_tela = (tela.altura * tela.largura) / 1000000
    tamanho_resolucao = (resolucao.altura * resolucao.largura) / 1000000

    if tamanho_tela > tamanho_resolucao:
        return True
    else:
        return False

def Resolucao_Tela(tela: Resolucao) -> str:
    '''
 Funcão fala se sua resolução é 16:9 ou 4:3 


    tela = Resolucao(1920 , 1080)
    >>> Resolucao_Tela(tela)
    Dezesseispornove
    
    tela = Resolucao(1024 , 768)
    >>> Resolucao_Tela(tela)
    Quatroportres
        
    tela = Resolucao(1024 , 768)
    >>> Resolucao_Tela(tela)
    Quatroportres

    tela = Resolucao(2560 , 1440)
    >>> Resolucao_Tela(tela)
    Dezesseispornove

    '''
    if (tela.largura * 9) / 16 == tela.altura:
        return Tipoderesolucao.Dezesseispornove.name
    elif (tela.largura * 3 ) / 4 == tela.altura:
        return Tipoderesolucao.Quatroportres.name
    else:
        raise ValueError("N tenho essa resolução")