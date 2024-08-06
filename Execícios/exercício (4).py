#Análise
#Função para calcular quanto de imposto o cidadão deve pegar sabendo q até 1000 dinheiros é 5% acima dos 1000 são 10% e acima de 5000 são 20%

#Definição de tipo de dado 
#
#O  dinheiro e imposto  será dado em float



def imposto(dinheiro:float) -> float:
    '''
Dado o valor de dinheiros que cidadão recebe irá mostrar quando vc deve pegar. 
Recebe o valor e calcula se for 6000 ele irá fazer 5% de 1000 + 10% de 4000 + 20% 1000 que vai ser quando vc deve pegar de imposto

Exemplo

>>> imposto(500.0)
25.0

>>> imposto(1000.0) 
50.0

>>> imposto(5000.0)
450.0

>>> imposto(6000.0)
650.0

    '''

    if dinheiro <= 1000.0:
        imposto = dinheiro * 0.05
        return imposto 

    elif dinheiro <= 5000.0:
        imposto = (1000.0 * 0.05) + ((dinheiro - 1000) * 0.10)
        return imposto

    else:
        imposto= 1000.0 * 0.05 + 4000.0 * 0.10 + (dinheiro - 5000.0) * 0.20
        return imposto 

