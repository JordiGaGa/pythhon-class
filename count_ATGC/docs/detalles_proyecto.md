# "Count A,T,G,C"

Fecha: 21/03/2024

**Participantes**:

- Jordi Garcia Garces <email:jordigg@lcg.unam.mx>

## Descripcion del Problema
Cuenta las ocurrencias de los símbolos "A","T","G","C" de una cadena de DNA que lea a través de un archivo. 


## Especificacion de Requisitos
Requisitos funcionales:

- Archivo .txt con secuencia de bases nitrogenadas representadas por los caracteres "A", "T", "G" o "C".

Requisitos no funcionales:

-

## Análisis y Esquema

"Cómo se resolvió el problema y qué se usó"
A continuación, se muestra un pseudocódigo simple para ilustrar la logica básica del script:

```
A = 0
T = 0
G = 0
C = 0
for base in string: #Siendo "string" el nombre con el que se lee el archivo.
  if base == "A":
    A += 1
  if base == "T":
    T += 1
  if base == "G":
    G += 1
  if base == "C":
    C += 1

print(f"El numero de bases son:\nA:{A}\nT:{T}\nG:{G}\nC:{C}")
```

"Se introduce archivo.txt con la secuencia de bases nitrogenadas esctritas como "A", "T", "G" o "C" y se regresa la cantidad de cada una de las bases presentes en la secuencia. 


#### Caso de uso:

```
Entra documento ---> Lee cada uno de los caracteres ---> Regresa cantidad de bases

```

- **Actor**: Usuario
- **Descripción**: "Se introduce el documento en el archivo, posteriormente se ejecuta y el resultado arrojará cada una de las bases nitrogenadas y la cantidad de ellas."
- **Flujo principal**:

	1. El actor inicia el sistema proporcionando el archivo de entrada.
	2. El sistema valida el archivo y los datos de entrada.
	3. El sistema lee la secuencia caracter por caracter. 
	4. El sistema muestra el resultado.
	
- **Flujos alternativos**: "Excepciones"

                
