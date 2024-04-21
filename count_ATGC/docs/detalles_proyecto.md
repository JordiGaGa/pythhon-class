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
# Librería
import argparse
# Programa
parser = argparse.ArgumentParser(description="contador ATGC")
# Archivo como parametro opcional
parser.add_argument("--input", 
                    type=str, 
                    help="Archivo con secuencia de DNA", 
                    required = False)
# Parametro opcional de la secuencia 
parser.add_argument("--secuencia",
                    type=str,
                    help="Secuencia de DNA",
                    required= False)
# Parametro opcional de la base a conocer
parser.add_argument("--base", 
                    choices=["A", "T", "G", "C"], 
                    help="Escoge una base nitrogenada",
                    required = False)

args = parser.parse_args()

#Funcion para conformar si el archivo tiene otro tipo de elementos 
def contenido(secuencia):
    caractres_validos = set("ATGC")
    for base in secuencia:
        if base not in caractres_validos:
            print(f"Caracter {base} es invalido")
            return(False)
    return(True)
#En caso de no haber ingresado ninguna entrada
if args.input == None and args.secuencia == None:
    print("No introduciste nada")
    exit()

#En caso de haber ingresado un odcumento
if args.input:
    try:
# Aqui subimos el archivo y lo llamamos "string"
        with open(args.input, "r") as string:
            # Convertimos el archivo a una string llamada "sec"
            sec = string.read().upper()
#En caso de algun error con el archivo regresa este mensaje
    except FileNotFoundError as fnf_error:
            print(f"El archivo {fnf_error.filename} no existe. \n")
            exit()
# En caso de haber ingresado una cadena de caracteres
if args.secuencia:
     sec = args.secuencia.upper()
    
#Se va a la funcion a analizar la entrada
confirmacion = contenido(sec)

#Posterior a haber ebtrado a la funcion confirmacion
try:
    if confirmacion == False:
        raise Exception(f"El archivo no es una secuancia de DNA")
except Exception as  message:
    print(message)
    exit()

# En caso de haber agregado parametro "base"
if args.base:
    print(f"{args.base}: {sec.count(args.base)}")
        
# En caso de no haber agregado parametro base imprime todos
else: 
    print(f"A: {sec.count("A")}\nT: {sec.count("T")}\nG: {sec.count("G")}\nC: {sec.count("C")}")
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

                
