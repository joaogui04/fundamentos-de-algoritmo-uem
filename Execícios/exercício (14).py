def converterBinariodeDecimal(x: float) -> str:
    '''
    >>> converterBinariodeDecimal(524555)
    '1001110'
    >>> converterBinariodeDecimal(102)
    '1100110'
    >>> converterBinariodeDecimal(215)
    '11010111'
    >>> converterBinariodeDecimal(404)
    '110010100'
    >>> converterBinariodeDecimal(808)
    '1100101000'
    >>> converterBinariodeDecimal(5429)
    '1010100110101'
    >>> converterBinariodeDecimal(16383)
    '11111111111111'
    
    '''
    result = ""
    while x > 1:
        if x % 2 < 1:
            result = result + "0"
        else:   
            result = result + "1"
        x = x / 2
    if x == 1:
        result = result + "1"
    
    # Invertendo a string result
    result = result[::-1]

    return result


