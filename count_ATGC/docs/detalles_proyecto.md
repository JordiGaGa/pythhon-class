# "Count A,T,G,C"

Fecha: 21/03/2024

**Participantes**:

- Jordi Garcia Garces <email:jordigg@lcg.unam.mx>

## Descripcion del Problema
En este programa se cuentan las ocurrencias de los símbolos "A","T","G","C" de una cadena de DNA brindada a través de un archivo en formato .txt, además de que puede imprimir todos o únicamente el de interés del usuario. Esto nace a raíz de la necesidad de saber el número de bases nitrogenadas en una secuencia de DNA de interés 


## Especificacion de Requisitos
Requisitos funcionales:

- Leer las letras A,T,G,C de un archivo dado en formato de string. 
- Calcular la cantidad de bases que se repiten de cada tipo.

- Archivo .txt con secuencia de bases nitrogenadas representadas por los caracteres "A", "T", "G" o "C".

Requisitos no funcionales:
- Si quieres que te regrese una base en especifico poner: --base X (siendo X A,T,G o C).
- Si quieres saber cuantos nucleótidos había de todo tipo entonces poner: --todo X (Siendo x cualquier string)


## Análisis y Esquema

"Cómo se resolvió el problema y qué se usó"
A continuación, se muestra un pseudocódigo simple para ilustrar la logica básica del script:

```
with open("Secuencia.txt","r") as string: #Aqui subimos el archivo y lo llamamos "string"
  sec = str(string.readline()) #Convertimos el archivo a una string llamada "sec"
  A = 0
  T = 0
  G = 0
  C = 0
  for base in sec:
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

                
