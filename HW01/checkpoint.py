def numero_binario(numero:int):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    # Check Integer number
    if not isinstance(numero, int):

        return None

    # Check Positive Number
    if numero < 0:

        return None

    def descomponer(numero:int, binario:int=0, posicion:int=0):

        cociente, residuo = divmod(numero, 2)
        binario += residuo * 10 ** posicion
        posicion += 1

        if cociente == 0:

            return binario
        
        return descomponer(cociente, binario, posicion)
    
    return descomponer(numero)
    
def binario_numero(binario:int):
    r"""
    Esta función recibe como parámetro un número binario entero y lo devuelve en su 
    representación base 10. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero retorna nulo.
    """
    numero = 0
    # Check Integer number
    if not isinstance(binario, int):

        return None
    
    binario = str(binario)
    n = len(binario) - 1
    for i, digito in enumerate(binario):

        numero += int(digito) * 2 ** (n-i)
    
    return numero
    
def decimal_binario(decimal:float):
    r"""
    Esta función recibe como parámetro un numero decimal base 10 y retorna su representación
    en el sistema binario
    """
    _integer, decimal = divmod(decimal, 1)
    binario_integer = numero_binario(int(_integer))

    def _decimal_binario(decimal:float, binario_decimal:str=""):

        decimal *= 2
        _integer, decimal = divmod(decimal, 1)
        binario_decimal += str(int(_integer))

        if decimal == 0:

            return str(binario_integer) + "." + binario_decimal
        
        return _decimal_binario(decimal, binario_decimal)
        
    binario_decimal = _decimal_binario(decimal)

    return binario_decimal