# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:35:35 2020

@author: eduardo.vitcop
"""
from datetime import datetime

def fecha_valida(nuevo_valor):
    """ 
    Devueve TRUE si el dato es una fecha valida 
    
    >>> fecha_valida("25/11/2019")
    True
    
    >>> fecha_valida("")
    False
    
    """
    try:
        datetime.strptime(nuevo_valor, '%d/%m/%Y')
        return True
    except:
        return False
    


def mes_valido(mes):
    """ Valida numero de mes entero entre 1 y 12
    
    
    >>> mes_valido(0)
    False
    
    >>> mes_valido("")
    False
    
    >>> mes_valido("1")
    True
    
    >>> mes_valido("12")
    True
    
    >>> mes_valido("13")
    False
    
    """
    if not mes:
        return False
    if mes.isdigit():
        return 0 < int(mes) < 13
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()