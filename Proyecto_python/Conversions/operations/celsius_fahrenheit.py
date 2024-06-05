"""
celsius_fahrenheit.py: Módulo para Realizar las conversiones de °Celcius a °Fahrenheit  o viceversa
(segun las espedificaciones del usuario).

Este módulo proporciona las funciones necesarias para poder transformar los datos de un array que contenga
una lista de temperaturas en °Celcius y convertir dichos datos en °Fahrenheit o viseversa.

Funciones:
- C_to_F(array): Devuelve un array conteniendo los datos de °Celcius pasados a °Fahrenheit.
- F_to_C(array): Devuelve un array conteniendo los datos de °Fahrenheit pasados a °Celcius.
"""
# ===========================================================================
# =                            imports
# ===========================================================================

import numpy as np

# ===========================================================================
# =                            functions
# ===========================================================================

def C_to_F(C_array):
    """
    Transforma los datos de un array de °Celcius a °Fahrenheit.

    Args:
        C_array (array): Valores que se van a transformar de °Celcius a °Fahrenheit.

    Returns:
        F_array (array): Valores que se van a transformaron a °Fahrenheit.
    """
    F_array = (C_array * 9/5) + 32 

    return F_array

def F_to_C(F_array):
    """
    Transforma los datos de un array de °Fahrenheit a °Celcius.

    Args:
        F_array (array): Valores que se van a transformar de °Fahrenheit a °Celcius.

    Returns:
        C_array (array): Valores que se van a transformaron a °Celcius.
    """
    C_array = (F_array - 32) * 5/9

    return C_array
