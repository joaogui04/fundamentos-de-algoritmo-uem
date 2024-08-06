def ming(pac:int, precopac:float, precoalb:float, tamanho: int) -> float:
    quantospack = tamanho / pac
    arred = round(quantospack)
    if quantospack > arred:
        arred = arred + 1
    valortotalpac = arred * precopac
    result = valortotalpac + precoalb
    return result
