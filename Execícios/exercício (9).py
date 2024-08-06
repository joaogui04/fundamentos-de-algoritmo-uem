#analise
#determinar se o aluno vai recevber laurea academica baseado se ele teve 2/3 de suas notas acima de 9.0 
#Tipos de dados 
#notas do aluno dado em float e positivo
 
def receba(lista: list[float]) -> bool:

    rece = False
    t1 = 0 
    tamanho_lista = len(lista)
    tamanh = tamanho_lista * 2/3
    tamanho = round(tamanh)
    for nota in lista:
        if nota >= 9.0:
            t1 = t1 + 1
    if t1 >= tamanho:
        rece = True 
    return rece