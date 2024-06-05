"""
file_io.py: Funciones para manejar operaciones de entrada/salida de archivos con cifras 
que representen unidades ya sea de kilometros o millas, grados celcius o fahrenheit y 
libras o kilogramos.

Este modulo provee funcionalidades para leer y transformar los datos introducidos a
travez de un archivo en una array de numpy con la cual se realizaran distintas operaciones.
Tambien permite generar un archivo con los datos de un arrays.

Funciones:
    l_file_to_matrix(file_name) - Lee un archivo con la lista de datos numericos de 
                                  manera linear y almacena los datos en un array.
    nl_file_to_matrix(file_name) - Lee un archivo con la lista de datos numericos de 
                                   manera no linear y almacena los datos en un array.
    matrix_to_file(file_name, matrix) - Almacena los datos de un par de arrays dentro de un archivo.
    
Ejemplos de uso estan disponibles en el bloque principal del modulo.

Autores: Jocelyn Trujillo Gutierrez y Jordi Garcia Garces
Versión: 1.0
"""

# ===========================================================================
# =                            imports
# ===========================================================================

import numpy as np

# ===========================================================================
# =                            meta-info
# ===========================================================================

__author__ = "Jocelyn Trujillo Gutierrez y Jordi Garcia Garces"
__version__ = "1.0"

# ===========================================================================
# =                            main functions
# ===========================================================================

def l_file_to_array(file_name):
    """
    Lee una lista de datos numericos (organizados de manera lineal)
    introducidos a partir de un archivo.
    
    Args:
        file_name (str): El nombre del archivo del cual se extraeran los 
                         datos.
        
    Returns:
        matriz (array): Array de numpy que almacena los datos introducidos 
        dentro del archivo.
    """

    with open(file_name, 'r') as file:
        line = file.readline()
    
    array = np.array([int(num) for num in line.strip().split()])
    return array


def nl_file_to_array(file_name):
    """
    Lee una lista de datos numericos (organizados de manera no lineal)
    introducidos a partir de un archivo.
    
    Args:
        file_name (str): El nombre del archivo del cual se extraeran los 
                         datos.
        
    Returns:
        matriz (array): Array de numpy que almacena los datos introducidos 
        dentro del archivo.
    """

    with open(file_name, 'r') as file:
        data = file.readlines()
    
    array = np.array([int(number.strip()) for number in data])
    return array

def arrays_to_file(file_name, array_1, array_2):
    """
    Junta 2 arrays datos y los imprime dentro de un mismo archivo.
    
    Args:
        filename (str): El nombre del archivo donde se almacenaran los datos.
        matrix_1 (array): La secuencia de ADN a escribir.
        
    Raises:
        IOError: Si no se puede escribir en el archivo.
    """
    try:
        matrix = np.column_stack((array_1, array_2))
        with open(file_name, 'a') as file:
            for row in matrix:
                file.write(f"{row[0]}\t{row[1]}\n")
    except IOError:
        raise IOError("No se pudo escribir en el archivo.")
