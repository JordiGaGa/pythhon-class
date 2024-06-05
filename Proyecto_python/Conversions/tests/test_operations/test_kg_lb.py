import unittest
import numpy as np
from Conversions.operations.kg_lb import kg_to_lb, lb_to_kg

class TestConversionFunctions(unittest.TestCase):
    """
    Clase de pruebas unitarias para las funciones `kg_to_lb` y `lb_to_kg` del módulo `operations.kg_lb`.
    Esta clase contiene métodos para probar la correcta conversión de kilogramos a libras y viceversa,
    incluyendo el manejo correcto de entradas de arrays de numpy.
    
    Métodos:
        test_kg_to_lb: Prueba la conversión de kilogramos a libras para asegurar el correcto comportamiento
                       de la función `kg_to_lb`.
        test_lb_to_kg: Prueba la conversión de libras a kilogramos para asegurar el correcto comportamiento
                       de la función `lb_to_kg`.
    """
    def test_kg_to_lb(self):
        kg_array = np.array([1, 2, 3, 4, 5])
        lb_array_expected = np.array([2.205, 4.41, 6.615, 8.82, 11.025])
        np.testing.assert_array_almost_equal(kg_to_lb(kg_array), lb_array_expected, decimal=3)
    
    def test_lb_to_kg(self):
        lb_array = np.array([2.205, 4.41, 6.615, 8.82, 11.025])
        kg_array_expected = np.array([1, 2, 3, 4, 5])
        np.testing.assert_array_almost_equal(lb_to_kg(lb_array), kg_array_expected, decimal=3)

if __name__ == '__main__':
    unittest.main()
