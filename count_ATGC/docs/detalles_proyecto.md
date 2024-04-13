# "Count A,T,G,C"

Fecha: 21/03/2024

**Participantes**:

- Jordi Garcia Garces <email:jordigg@lcg.unam.mx>

## Descripcion del Problema
En este programa se cuentan las ocurrencias de los símbolos "A","T","G","C" de una cadena de DNA brindada a través de un archivo en formato .txt, además de que puede imprimir todos o únicamente una que resulte de interés al usuario. Esto nace a raíz de la necesidad de saber el número de bases nitrogenadas en una secuencia de DNA de interés 


## Especificacion de Requisitos
Requisitos funcionales:
- Programa desarrollado en python.
- Leer las letras A,T,G,C de un archivo dado en formato de string. 
- Calcular la cantidad de bases que se repiten de cada tipo guardadas en variables independientes.
- Desplegar el resultado en forma de texto con las cifras y la respectiva base.

Requisitos no funcionales:
- Si quieres que te regrese una base en especifico poner: --base X (siendo X A,T,G o C).
- Programa adherido a los lineamientos de PEP8.
- Se hace uso de la librería argparse de python para la entrada de argumentos. 
- Si quieres saber cuantos nucleótidos había de todo tipo entonces poner: --todo X (Siendo x cualquier string)


## Análisis y Esquema

Para este problema se usaron ciertas funciones de python, así como el establecer los parámetros para poder validar el archivo y la salida. 
A continuación, se muestra un pseudocódigo simple para ilustrar la logica básica del script:

```
with open(args.input_file, "r") as string:
    # Convertimos el archivo a una string llamada "sec"
    sec = str(string.readline())

    A = 0
    T = 0
    G = 0
    C = 0
    # Usamos contadores para cada tipo de base
    for base in sec:
        if base == "A":
            A += 1
        if base == "T":
            T += 1
        if base == "G":
            G += 1
        if base == "C":
            C += 1
    # Si se agrego el parametro todo, imprime
    if args.todo:
        print(f"El numero de bases son:\nA:{A}\nT:{T}\nG:{G}\nC:{C}")
    # Si se agrego el parametro base, imprime el texto de acuerdo a la base pedida
    if args.base:
        if args.base == "A":
            print(f"La base {args.base} se repite {A} veces")
        if args.base == "T":
            print(f"La base {args.base} se repite {T} veces")
        if args.base == "G":
            print(f"La base {args.base} se repite {G} veces")
        if args.base == "C":
            print(f"La base {args.base} se repite {C} veces")
```

"Se introduce archivo.txt con la secuencia de bases nitrogenadas esctritas como "A", "T", "G" o "C" y se regresa la cantidad de cada una de las bases presentes en la secuencia. 


#### Caso de uso:

- **Actor**: Usuario
- **Descripción**: "El usuario proporciona el archivo con la secuencia de DNA con los caracteres A,T,G,C (únicamente ellos), posteriormente se ejecuta y el resultado arrojará ya sea la base nitrogenada de interés y la cantidad o cada una de las bases y la cantidad presente."
- **Flujo principal**:

	1. El actor inicia el sistema proporcionando el archivo de entrada.
	2. El sistema valida el archivo y los datos de entrada.
	3. El sistema lee la secuencia caracter por caracter. 
	4. El sistema muestra el resultado.
	
- **Flujos alternativos**: "Excepciones"
  - Si el archivo proporcionado no existe.
  		1. Se muestra mensaje de error por default.

                
