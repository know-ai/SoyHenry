def numero_binario(numero:int):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    binario = list()

    def descomponer(numero:int):
        """
        Wrapper function to 
        """
        cociente, residuo = divmod(numero, 2)

        binario.insert(0, str(residuo))

        if cociente == 0:

            return int("".join(binario))
        
        return descomponer(cociente)

    # Check Integer number
    if not isinstance(numero, int):

        return None
    
    else:

        # Check Positive Number
        if numero < 0:

            return None
        
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
    
    else:
        
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
    binario_decimal = list()

    def _decimal_binario(decimal:float):
        
        decimal *= 2

        _integer, decimal = divmod(decimal, 1)

        binario_decimal.append(str(int(_integer)))

        if decimal == 0:

            return "".join(binario_decimal)
        
        return _decimal_binario(decimal)
        
    binario_decimal = _decimal_binario(decimal)

    return str(binario_integer) + "." + binario_decimal