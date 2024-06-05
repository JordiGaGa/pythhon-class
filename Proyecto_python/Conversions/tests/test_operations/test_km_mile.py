import unittest
import numpy as np
from Conversions.operations.km_mile import km_to_mile, mile_to_km

class TestConversionFunctions(unittest.TestCase):
    """
    Clase de pruebas unitarias para las funciones `km_to_mile` y `mile_to_km` del módulo `operations.km_mile`.
    Esta clase contiene métodos para probar la correcta conversión de Km a millas y viceversa,
    incluyendo el manejo correcto de entradas de arrays de numpy.
    
    Métodos:
        test_km_to_mile: Prueba la conversión de Km a millas para asegurar el correcto comportamiento
                         de la función `km_to_mile`.
        test_mile_to_km: Prueba la conversión de millas a Km para asegurar el correcto comportamiento
                         de la función `mile_to_km`.
    """
    def test_km_to_mile(self):
        km_array = np.array([15, 20, 30, 40])
        mile_array_expected = np.array([9.323, 12.43, 18.645, 24.86])
        np.testing.assert_array_almost_equal(km_to_mile(km_array), mile_array_expected, decimal=3)
    
    def test_mile_to_km(self):
        mile_array = np.array([9.323, 12.43, 18.645, 24.86])
        km_array_expected = np.array([15, 20, 30, 40])
        np.testing.assert_array_almost_equal(mile_to_km(mile_array), km_array_expected, decimal=3)

if __name__ == '__main__':
    unittest.main()
