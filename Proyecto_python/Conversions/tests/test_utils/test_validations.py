import unittest
from unittest.mock import mock_open, patch
from Conversions.utils.validations import not_empty, type_file

class TestFileValidation(unittest.TestCase):
    """
    Clase de pruebas unitarias para las funciones del módulo `utils.validations`.
    Esta clase contiene métodos para probar la correcta lectura y escritura de datos numéricos
    desde y hacia archivos, incluyendo el manejo correcto de archivos simulados con `unittest.mock`.

    Métodos:
        test_not_empty_empty_file: Prueba la función `not_empty` para validar que lanza una excepción
                                    cuando se proporciona un archivo vacío.
        test_not_empty_non_empty_file: Prueba la función `not_empty` para validar que devuelve True
                                        cuando se proporciona un archivo no vacío.
        test_type_file_linear: Prueba la función `type_file` para validar que funciona correctamente
                                con un archivo que contiene datos numéricos organizados de manera lineal.
        test_type_file_non_linear: Prueba la función `type_file` para validar que funciona correctamente
                                    con un archivo que contiene datos numéricos organizados con saltos de línea.
        test_type_file_invalid_characters: Prueba la función `type_file` para validar que lanza una excepción
                                            cuando se proporciona un archivo que contiene caracteres no válidos.
    """

    def test_not_empty_empty_file(self):
        # Prueba para un archivo vacío
        with patch("os.path.getsize", return_value=0):
            with self.assertRaises(ValueError):
                not_empty("fake_file.txt")

    def test_not_empty_non_empty_file(self):
        # Prueba para un archivo no vacío
        with patch("os.path.getsize", return_value=10):  # Simula un archivo no vacío
            result = not_empty("fake_file.txt")
            self.assertTrue(result)

    def test_type_file_linear(self):
        # Prueba para un archivo con datos numéricos organizados de manera lineal
        mock_data = "1 2 3 4 5"
        with patch("builtins.open", mock_open(read_data=mock_data)):
            with patch("os.path.getsize", return_value=len(mock_data)):
                file_path = "fake_file.txt"
                result = type_file(file_path)
                self.assertTrue(result)

    def test_type_file_non_linear(self):
        # Prueba para un archivo con datos numéricos organizados con saltos de línea
        mock_data = "1\n2\n3\n4\n5\n"
        with patch("builtins.open", mock_open(read_data=mock_data)):
            with patch("os.path.getsize", return_value=len(mock_data)):
                file_path = "fake_file.txt"
                result = type_file(file_path)
                self.assertFalse(result)

    def test_type_file_invalid_characters(self):
        # Prueba para un archivo que contiene caracteres no válidos
        mock_data = "1 a 3 4 5"
        with patch("builtins.open", mock_open(read_data=mock_data)):
            with patch("os.path.getsize", return_value=len(mock_data)):
                file_path = "fake_file.txt"
                with self.assertRaises(ValueError):
                    type_file(file_path)

if __name__ == '__main__':
    unittest.main()
