"""
conversions.py: Script para realizar los cambios de unidad de un archivo con una secuencia de numeros
                ya sea de km a milla, celsius a fahrenheit, kg a libra o cualquiera de los anteriores
                en el otro sentido.

Este script lee un archivo, almacena la informacion en un array de numpy y transforma los datos de dicho
array a otra unidad, posteriormente junta tanto los datos introducidos como los datos con los recien 
calculados, finalmente regresa un archivo con un nombre predeterminado por el codigo.

Uso:
    python calculate_at_content.py <path_to_numeric_data> <type_conversion> 

Argumentos:
    <path_to_numeric_data> : Ruta al archivo de texto que contiene los datos numericos.
    <type_conversion> : Tipo de conversion de unidad que se le va a aplicar a dichos datos.
"""

# ===========================================================================
# =                            imports
# ===========================================================================

import argparse
import numpy as np

from Conversions.operations.celsius_fahrenheit import C_to_F, F_to_C
from Conversions.operations.kg_lb import kg_to_lb, lb_to_kg
from Conversions.operations.km_mile import km_to_mile, mile_to_km
from Conversions.utils.file_io import l_file_to_array, nl_file_to_array, arrays_to_file
from Conversions.utils.validations import not_empty, type_file

# ===========================================================================
# =                            Main
# ===========================================================================

def main():
    parser = argparse.ArgumentParser(description="Conversion de valores numeros de una unidad a otra (peso, distancia, temperatura).")

    # Archivo de entrada
    parser.add_argument("input_file", type=str, help="Archivo con los valores numericos.")
    # Conversion
    parser.add_argument("type_conversion", type=str, choices=["C-F", "F-C", "kg-lb", "lb-kg", "km-mile", "mile-km"],
                        help="Tipo de conversion a realizar °C a °F = C-F o F-C kg a lb = kg-lb o lb-kg km a milla = km-mile o mile-km")

    args = parser.parse_args()

    # Almacena argumentos en variables
    file_path = args.input_file
    conversion = args.type_conversion

    # Valida que el archivo (contenido y formato)
    if not_empty(file_path):
        if type_file(file_path):
            type = "linear"
        else:
            type = "non_linear"

    # Almacena los datos del archvio en un array
    if type == "linear":
        array = l_file_to_array(file_path)
    if type == "non_linear":
        array = nl_file_to_array(file_path)
    
    # Dependiendo del tipo de conversion hace la transformacion y genera el archivo de salida
    if conversion == "C-F":
        new_array = C_to_F(array)
        arrays_to_file("Celsius_Fahrenheit", array, np.round(new_array, decimals=3))
    if conversion == "F-C":
        new_array = F_to_C(array)
        arrays_to_file("Fahrenheit_Celsius", array, np.round(new_array, decimals=3))
    if conversion == "kg-lb":
        new_array = kg_to_lb(array)
        arrays_to_file("kg_to_lb", array, np.round(new_array, decimals=3))
    if conversion == "lb-kg":
        new_array = lb_to_kg(array)
        arrays_to_file("lb_to_kg", array, np.round(new_array, decimals=3))
    if conversion == "km-mile":
        new_array = km_to_mile(array)
        arrays_to_file("km_to_mile", array, np.round(new_array, decimals=3))
    if conversion == "mile-km":
        new_array = mile_to_km(array)
        arrays_to_file("mile_to_km", array, np.round(new_array, decimals=3))
    

if __name__ == "__main__":
    main()