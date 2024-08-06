
from dataclasses import dataclass
from enum import Enum , auto

class Produtos(Enum):
    PAPEL = auto()
    PAPELAO = auto()
    PAINEIS = auto()

@dataclass
class Venda:
    produto: Produtos
    quantidade: int
    valorDaVenda: float
    custo: int 

@dataclass
class Receita:
    bruto: float   
    liquido: float
    
@dataclass
class LucroPorVendedor:
    vendedor: str
    lucro: float

    #Análise
    # Calcular a Receita bruta e receita liquida dado os Relatorios de Venda 

    #Tipos de Dados
    #Quantidade de produtos,  Valor de venda , custo do produto, todos dados em numeros positivos,  e os produtos dados como tipos enumerados 

def determineReceita(relatorio: list[Venda]) -> Receita:
    '''
    Gera apartir de *relatorio* a Receita bruta e receita liquida, produz uma *Receita* como resultado. 
    Calcula quanto é a Receita bruta fazendo a quantidade vezes o preço de venda, Calcula quanto é a Receita liquida fazendo a quantidade vezes o preço de custo e dps subtrai com a Receita Bruta.
    
    Exemplos
    >>> determineReceita([Venda(Produtos.PAPEL, 0, 55.0, 50.0), Venda(Produtos.PAPELAO, 0, 50.0, 40.0)])
    Receita(bruto=0.0, liquido=0.0)

    >>> determineReceita([Venda(Produtos.PAPEL, 100, 55.0, 50.0), Venda(Produtos.PAPELAO, 400, 50.0, 40.0)])
    Receita(bruto=25500.0, liquido=4500.0)

    >>> determineReceita([Venda(Produtos.PAPEL, 100, 55.0, 50.0), Venda(Produtos.PAPELAO, 400, 50.0, 40.0)])
    Receita(bruto=25500.0, liquido=4500.0)

    >>> determineReceita([Venda(Produtos.PAPEL, 100, 55.0, 50.0), Venda(Produtos.PAPELAO, 400, 50.0, 40.0), Venda(Produtos.PAINEIS, 200, 100.0, 75.0)])
    Receita(bruto=45500.0, liquido=9500.0)

    >>> determineReceita([Venda(Produtos.PAPEL, 100, 55.0, 50.0)])
    Receita(bruto=5500.0, liquido=500.0)
    
    '''
    receita = Receita(0,0)
    for venda in relatorio:
        receita.bruto =  receita.bruto + (venda.quantidade * venda.valorDaVenda)
        receita.liquido = receita.liquido + venda.custo * venda.quantidade 

    receita.liquido = receita.bruto - receita.liquido
    
    return receita

    #Analise
    # Função que descobre quais os 3 vendedores que mais tiveram lucro de uma lista. Dada uma lista sem nenhuma repetiçao de vendedor.

    #Tipos de Dados
    # Nome do vendedor, lucro do vendedor     
  
def tresmelhores(lista_de_funcionarios: list[LucroPorVendedor]) -> list[LucroPorVendedor]:
    '''
    Para cada *funcionario* na *lista_de_funcionarios* ele vai ver se a lista *melhores* está com menos de 3, se estiver ele vai adicionar *funcionario* em *melhores*,
    caso *melhores* for maior ou igual a 3 então eu chamo uma função que descobre quem vai ser o o menor em *melhores* e vou chamar ele de *vendedor_menor_lucro* 
    se *funcionario* for maior que *vendedor_menor_lucro* ele coloca *funcionarios* dentro da lista *melhores* no lugar de *vendedor_menor_lucro*

    '''
    melhores = []
    for funcionario in lista_de_funcionarios:
        if len(melhores) < 3:
            melhores.append(funcionario)
        else:    
            vendedor_menor_lucro = menorvalor(melhores)
            if funcionario.lucro > vendedor_menor_lucro.lucro:
                indice = melhores.index(vendedor_menor_lucro)
                melhores[indice] = funcionario                                                      
    return melhores


    #Analise
    # Descobre o menor valor de uma lista. 

    #Tipos de Dados
    # Lista de Nome do vendedor e quantidade em reais de lucro. 
    
def menorvalor(lista: list[LucroPorVendedor]) -> LucroPorVendedor:
    '''
    
    Primeiro ele define o *menor* como o primeiro elemento de *lista* dps ele testa se os outros elementos da lista são menores que ele,
    se algum elemento da *lista* for menor então esse elemento será o novo *menor*,
    caso não exista um numero menor que *menor* então o primeiro elemento da *lista* será o menor.

    '''
    menor = lista[0] 
    for item in lista:
        if item.lucro < menor.lucro:
            menor = item
    return menor














    
            



















        








    









