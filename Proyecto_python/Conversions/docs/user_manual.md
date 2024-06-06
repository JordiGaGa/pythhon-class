# Convertidor de numeros en archivo 

Fecha: 05/06/2024

**Participantes**:

- Jocelyn Trujillo  <email:jocelynt@lcg.unam.mx> 
- Jordi Garcia <email:jordigg@lcg.unam.mx>

## Descripcion del Problema

Este es un proyecto que se encarga de: Convertir una serie de datos de un tipo de unidad de medicion a otro. La necesidad surge del requerimiento de poder hacer conversiones de unidades para aquellas personas que desean procesar los datos rn un tipo de unidad distinta al que tienen.

El problema enunciado implica leer los numeros de un archivo, convertirlos a la unidad deseada (en base a la conversion que se este realizando) y regresar un documento que contenga una matriz con las cifras iniciales y las mismas convertidas  


## Especificacion de Requisitos

Requisitos funcionales

- Leer numeros de un archivo dado, tanto en formato de numero entero como decimal.
- Establecer el tipo de conversion a realizar (fahrenheit a celcius, kilometros a millas o kilogramos a libras y viceversa).
- Regresar un documento que contenga una matriz con las unidades iniciales y las unidades convertidas al tipo solicitado.
- Producir un mensaje de error si el archivo esta vacio.

Requisitos no funcionales

- El script debera estar escrito en Python.
- El tiempo de respuesta debe ser rapido, incluso con archivos de gran tamaño.
- La entrada del archivo debe ser flexible (i.e. se acepta a traves de la linea de comandos).


## Analisis y Formato

Para resolver este problema, se utilizaran varias funciones incorporadas en Python, asi como el manejo de excepciones para la validacion de datos y archivo.

El formato de los datos de entrada sera simplemente un archivo, este puede contener en una sola linea numeros separados por espacios o tabuladores o un numero por linea. Los numeros pueden estar en formato entero o decimal. La salida sera un documento de texto que muestra una matriz con los numeros presentes en el documento inicial y los mismos convertidos. Los mensajes de error se imprimirán en la consola.

- **Actor**: Usuario
- **Descripcion**: El actor proporciona un archivo de entrada con numeros a convertir, asi como el tipo deconversion a realizar. El sistema valida el archivo y los datos de entrada, realiza las conversiones y regresa archivo con las mismas.
- **Flujo principal**:

	1. El actor inicia el sistema proporcionando el archivo de entrada con los numeros a convertir.
	2. El sistema valida el archivo y los datos de entrada.
	3. El sistema convierte los valores a la metrica solicitada por el usuario.
	4. El sistema devuelve un archivo con los datos convertidos. 
	
- **Flujos alternativos**:
	- Si el archivo proporcionado esta vacio
		1. El sistema muestra un mensaje de error.
	- Si el archivo proporcionado contiene caracteres no validos (que no sean numeros, enteres, espacios o tabuladores)
 		1. El sistema muestra un mensaje de error.
