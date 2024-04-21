"""
NAME: contador_ATGC


VERSION: 1.0


AUTHOR: JORDI GARCIA GARCES


DESCRIPTION: Programa para contar el número de cada base nitrgoenada en archivo .txt
    Archivo de entrada   
        CRuta a larchivo con la secuencia a introducir.
        
    -- base
        Nucleótido a contar.
    --todo 
        Si se desea que se impriman todas las bases


Ejemplos
    
        python contador_ATGC.py --input archivo.txt
        python contador_ATGC.py --secuencia ATGCGTGA
        python contador_ATGC.py --base A


USAGE

    python contador_ATGC.py [-parameters] [value]
"""
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
