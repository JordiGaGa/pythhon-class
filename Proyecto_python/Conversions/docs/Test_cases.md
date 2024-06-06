# Casos de prueba 

Este documento describe los casos de prueba para el script dentro del paquete de Python el cual su funcion es convertir los numeros dentro de un documento dependiendo de su naturaleza, ya sea de kilometros a millas, grados celcius a fahrenheit o kilogramos a libras (y vicenversa).

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

El script está diseñado para validar el archivo y calcular las conversiones de unidad dependiendo de lo indicado por el usuario. El script también está diseñado para manejar errores como si el archivo esta vacio o si los datos introducidos no son los adecuados.

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.
    
    
### Caso de prueba 1: Comprobacion de la conversion de °C a °F
 
- Descripcion: Verificar que el script puede transformar de manera adeucada varios valores numericos de celsius a fahrenheit.
- Datos de entrada:
  ```
	Archivo con los siguientes datos:
		"0 20 25 30 35 40"
    Conversion: C-F
  ```
- Resultado esperado archivo con la siguiente informacion:

```
0    32
20   68
25   77
30   86
35   95
40  104
```

Siendo que los datos estan divididos de la siguiente manera: "original  transformado"

### Caso de prueba 2: Comprobacion de la conversion de °F a °C

- Descripcion: Verificar que el script puede transformar de manera adeucada varios valores numericos de fahrenheit a celsius.
- Datos de entrada:
  ```
	Archivo con los siguientes datos:
	    "32. 68. 77. 86. 95. 104"
    Conversion: F-C
  ```
- Resultado esperado archivo con la siguiente informacion:

```
32    0
68   20
77   25
86   30
95   35
104  40
```

Siendo que los datos estan divididos de la siguiente manera: "original  transformado"

### Caso de prueba 3: Comprobacion de la conversion de kg a libra

- Descripcion: Verificar que el script puede transformar de manera adeucada varios valores numericos de kg a libra.
- Datos de entrada:
  ```
	Archivo con los siguientes datos:
	    "1 2 3 4 5"
    Conversion: kg-lb
  ```
- Resultado esperado archivo con la siguiente informacion:
```
1  2.205
2  4.41
3  6.615
4  8.82
5  11.025
```
Siendo que los datos estan divididos de la siguiente manera: "original  transformado"

### Caso de prueba 4: Comprobacion de la conversion de libra a kg

- Descripcion: Verificar que el script puede transformar de manera adeucada varios valores numericos de libra a kg.
- Datos de entrada:
  ```
	Archivo con los siguientes datos:
	    "2.205 4.41 6.615 8.82 11.025"
    Conversion: lb-kg
  ```
- Resultado esperado archivo con la siguiente informacion:
```
2.205  1
4.41   2
6.615  3
8.82   4
11.025 5
```
Siendo que los datos estan divididos de la siguiente manera: "original transformado"

### Caso de prueba 5: Comprobacion de la conversion de km a millas

- Descripcion: Verificar que el script puede transformar de manera adeucada varios valores numericos de km a millas.
- Datos de entrada:
  ```
	Archivo con los siguientes datos:
	    "1 2 3 4 5"
    Conversion: km-millas
  ```
- Resultado esperado archivo con la siguiente informacion:
```
1 0.621
2 1.243
3 1.864
4 2.486
5 3.107
```
Siendo que los datos estan divididos de la siguiente manera: "original  transformado"

### Caso de prueba 6: Comprobacion de la conversion de millas a km

- Descripcion: Verificar que el script puede transformar de manera adeucada varios valores numericos de millas a km.
- Datos de entrada:
  ```
	Archivo con los siguientes datos:
	    "0.621 1.243 1.864 2.486 3.107"
    Conversion: kg-lb
  ```
- Resultado esperado archivo con la siguiente informacion:
```
0.621 1
1.243 2
1.864 3
2.486 4
3.107 5
```
Siendo que los datos estan divididos de la siguiente manera: "original  transformado"

### Caso de prueba 7: Comprobacion de error para cuando el archivo introducido esta vacío

- Descripcion: Verificar que el script maneja correctamente los archivos vacíos.
- Datos de entrada:
	```
    Archivo sin contenido.
    Cualquier conversion ej. F-C
	```
- Resultado esperado: 
		1.- Regresa un error:
            ValueError: El archivo esta vacio.
		2.- Termina el programa.

### Caso de prueba 8: Comprobacion de error para caracteres no validos introducidos dentro del archivo

- Descripcion: Verificar que el script maneja correctamente archivos con caracteres no validos al ejecutar el programa.
- Datos de entrada:
	```
	Archivo con los siguientes datos:
		"0 15 20 30 40 a 60"
	Cualquier conversion ej. F-C
	 ```
- Resultado esperado: 
		1.- Regresa un error:
            ValueError: El archivo contiene caracteres no válidos (letras).
		2.- Termina el programa.
