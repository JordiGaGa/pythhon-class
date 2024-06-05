"""
kg_lb.py: Módulo para Realizar las conversiones de Kg a libra o viseversa (segun las espedificaciones del usuario).

Este módulo proporciona las funciones necesarias para poder transformar los datos de un array que contenga
una lista de pesos en Kg y convertir dichos datos en libras o viseversa.

Funciones:
- kg_to_lb(array): Devuelve un array conteniendo los datos de Kg pasados a libras.
- lb_to_kg(array): Devuelve un array conteniendo los datos de libras pasados a Kg.
"""
# ===========================================================================
# =                            imports
# ===========================================================================

import numpy as np

# ===========================================================================
# =                            functions
# ===========================================================================

def kg_to_lb(kg_array):
    """
    Transforma los datos de un array de Kg a libras.

    Args:
        kg_array (array): Valores que se van a transformar de Kg a libras.

    Returns:
        lb_array (array): Valores que se van a transformaron a libras.
    """
    lb_array = kg_array * 2.205

    return lb_array

def lb_to_kg(lb_array):
    """
    Transforma los datos de un array de libras a Kg.

    Args:
        lb_array (array): Valores que se van a transformar de libras a Kg.

    Returns:
        kg_array (array): Valores que se van a transformaron a Kg.
    """
    kg_array = lb_array / 2.205

    return kg_array

# ===========================================================================
# =                            test
# ===========================================================================

if __name__ == "__main__":
    # Prueba de funcionalidad.
    test_array_kg = np.array([1, 2, 3, 4, 5])
    print(f"El array original: {test_array_kg} \npasado de kg a Libras: {kg_to_lb(test_array_kg)}")
    test_array_lb = kg_to_lb(test_array_kg)
    print(f"El array original: {test_array_lb} \npasado de libras a kg: {lb_to_kg(test_array_lb)}")
