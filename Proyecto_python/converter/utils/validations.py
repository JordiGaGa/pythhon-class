"""
validations.py: Módulo para realizar validaciones de formatos de archivos en el paquete Conversions.

Este módulo proporciona funciones útiles para validar:
- El formato del archivo, ya sea que este...
    - Tenga todos los datos en una sola linea.
    - Tenga la informacion separada mediante saltos de linea.
- El archivo contenga unicamente valores numericos (ya sea enteros o flotantes)

Funciones:
- not_empty(file_path): Revisa que el archivo no este vacio.
- type_file(file_path): Busca el formato en el que se almacena el archivo, si es linear o contiene 
                          saltos de lineas.

Los errores de validación levantan excepciones para permitir una gestión de errores adecuada en las funciones de llamada.

Autores: Jocelyn Trujillo Gutierrez y Jordi Garcia Garces
Versión: 1.0
"""

# ===========================================================================
# =                            imports
# ===========================================================================

import os
import re

# ===========================================================================
# =                            functions
# ===========================================================================

def not_empty(file_path):
    """
    Valida que el archivo no este vacio.

    Args:
        file_path (str): Path del archivo a validar.

    Returns:
        bool: True si el archivo contiene informacion.

    Raises:
        ValueError: Si el archivo esta vacio.
    """
    if os.path.getsize(file_path) == 0:
        raise ValueError("El archivo esta vacio.")
    return True

def type_file(file_path):
    """
    Verifica que el archivo solo contenga datos numericos y la manera
    en que estos se organizan.

    Args:
        file_path (str): Path del archivo a validar.

    Returns:
        bool: True si el formato es linear, False si esta separado por
              saltos de linea.

    Raises:
        ValueError: Si el archivo no sigue el formato adecuado para su uso.
    """
    try:
        with open(file_path, 'r') as file:
            not_empty(file_path)
            for line in file:
                if re.match(r"^\d+(\s+\d+)+$", line):
                    if line.endswith('\n'):
                        raise ValueError("El archivo no tiene el formato esperado")
                    return True
                if re.search(r"[A-Za-z,]", line):
                    raise ValueError("El archivo contiene caracteres no válidos (letras o , ).")
        return False
    except Exception as e:
        raise e
