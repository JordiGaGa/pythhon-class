import unittest
import numpy as np
from Conversions.operations.celsius_fahrenheit import C_to_F, F_to_C

class TestConversionFunctions(unittest.TestCase):
    """
    Clase de pruebas unitarias para las funciones `C_to_F` y `F_to_C` del módulo `operations.celsius_fahrenheit`.
    Esta clase contiene métodos para probar la correcta conversión de °Celsius a °Fahrenheit y viceversa,
    incluyendo el manejo correcto de entradas de arrays de numpy.
    
    Métodos:
        test_C_to_F: Prueba la conversión de °Celsius a °Fahrenheit para asegurar el correcto comportamiento
                     de la función `C_to_F`.
        test_F_to_C: Prueba la conversión de °Fahrenheit a °Celsius para asegurar el correcto comportamiento
                     de la función `F_to_C`.
    """
    def test_C_to_F(self):
        C_array = np.array([0, 100, -40, 37])
        F_array_expected = np.array([32, 212, -40, 98.6])
        np.testing.assert_array_almost_equal(C_to_F(C_array), F_array_expected, decimal=1)
    
    def test_F_to_C(self):
        F_array = np.array([32, 212, -40, 98.6])
        C_array_expected = np.array([0, 100, -40, 37])
        np.testing.assert_array_almost_equal(F_to_C(F_array), C_array_expected, decimal=1)

if __name__ == '__main__':
    unittest.main()
