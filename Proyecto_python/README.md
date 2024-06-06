# Conversions

Este es un paquete de Python el cual su funcion es convertir los numeros dentro de un documento dependiendo de su naturaleza,
ya sea de kilometros a millas, grados celcius a fahrenheit o kilogramos a libras (y vicenversa).

## Uso

El paquete acepta un script que contenga unicamente los numeros a tratar, ya sea separados por espacios, tabuladores o en una 
sola columna.

```
python conversions.py -inputfile [archivo] -type_conversion [conversions] str: contiene uno de los siguientes ejemplos: C-F, F-C, kg-lb, lb-kg, km-mile, mile-km.
```

donde `[archivo]` es el nombre del archivo que contiene los valores a manipular y `[conversions]` contiene el tipo de conversion a realizar conforme a los parametros puestos.

## Salida

El paquete regresara un archivo con una matriz que contenga los numeros introducidos previamente junto con los mismos convertidos a las unidades solicitadas.

## Control de errores

Si el archivo proporcionado esta vacio, se generara un mensaje de error.

## Pruebas

El paquete incluye un conjunto de pruebas unitarias. Puede ejecutar estas pruebas con:

```
python -m Conversions.test.operations.test_celcius_fahrenheit
python -m Conversions.test.operations.test_kg_lb
python -m Conversions.test.operations.test_km_mile
python -m Conversions.test.operations.test_kg_lb
python -m Conversions.test.utils.test_file_io
python -m Conversions.test.utils.test_validations
```

## Datos

El paquete esta diseñado para operar en archivos de texto plano, con un numeros ya sea en una linea separados por tabuladores o espacios o un numero por renglon. 

## Metadatos y documentacion

Este README ofrece informacion de uso basico. Para obtener informacion mas detallada sobre el paquete y la implementacion consulte [user_manual](https://github.com/JordiGaGa/pythhon-class/blob/main/Proyecto_python/Conversions/docs/user_manual).

## Codigo fuente

El codigo fuente esta disponible en este repositorio. Se acoge con satisfaccion cualquier contribucion o sugerencia a traves de solicitudes pull request.

## Terminos de uso

Este paquete esta disponible bajo la licencia [MIT License](https://github.com/JordiGaGa/pythhon-class/blob/main/Proyecto_python/LICENSE). Consulte el archivo LICENSE para obtener mas detalles.


## Contactenos

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en Git hub: [JordiGaGa](https://github.com/JordiGaGa) & [Jocelyn-TG](https://github.com/Jocelyn-TG).
