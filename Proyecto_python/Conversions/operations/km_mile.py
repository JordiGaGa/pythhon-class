"""
km_mile.py: Módulo para Realizar las conversiones de Km a milla o viseversa (segun las espedificaciones del usuario).

Este módulo proporciona las funciones necesarias para poder transformar los datos de un array que contenga
una lista de distancias en Km y convertir dichos datos a millas o viseversa.

Funciones:
- km_to_mile(array): Devuelve un array conteniendo los datos de Km pasados a millas.
- mile_to_km(array): Devuelve un array conteniendo los datos de millas pasados a Km.
"""
# ===========================================================================
# =                            imports
# ===========================================================================

import numpy as np

# ===========================================================================
# =                            functions
# ===========================================================================

def km_to_mile(km_array):
    """
    Transforma los datos de un array de Km a millas.

    Args:
        km_array (array): Valores que se van a transformar de Km a millas.

    Returns:
        mile_array (array): Valores que se van a transformaron a millas.
    """
    mile_array = km_array / 1.609

    return mile_array

def mile_to_km(mile_array):
    """
    Transforma los datos de un array de millas a Km.

    Args:
        mile_array (array): Valores que se van a transformar de millas a Km.

    Returns:
        km_array (array): Valores que se van a transformaron a Km.
    """
    km_array = mile_array * 1.609

    return km_array
