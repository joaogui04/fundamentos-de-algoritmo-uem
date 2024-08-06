#funcao q limita a quantidade de caracter  usado cortando os q passam no final em uma string e se tiver menor q o limite deixa o espaça em branco no final


def limitastr(frase:str, quantidade:int) -> str:
    '''
    pegar a *frase* caso ela passar a *quantidade* de catacter vou cortar a frase. se sobrar eu vou pegar *frase* e almentar " " para cada *quantidade* q sobrou.

    >>> limitastr("deixa acontecer", 10)
    'deixa acont'

    >>> limitastr("deixa", 10)
    'deixa     '

    '''
    numerofra = len(frase)
    if numerofra >= quantidade:
        return frase[:quantidade]
    else: # numerofra < quantidade:
        result  = quantidade - numerofra
        return frase + " " * result
    
