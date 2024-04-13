"""
NAME: contador_ATGC


VERSION: 1.0


AUTHOR: JORDI GARCIA GARCES


DESCRIPTION: Programa para contar el número de cada base nitrgoenada en archivo .txt


CATEGORY


USAGE

    python contador_ATGC [-parameters] [value]


ARGUMENTS


METHOD


SEE ALSO
"""

import argparse
# Programa
parser = argparse.ArgumentParser(description="contador ATGC")
# Archivo como parametro obligatorio
parser.add_argument("input_file", type=str, help="..")
# Parametro opcional de la base
parser.add_argument(
    "--base", choices=["A", "T", "G", "C"], help="Escoge una base nitrogenada")
# Parametro opcional para imprimir todos
parser.add_argument("--todo", type=str, help="..")

args = parser.parse_args()

# Aqui subimos el archivo y lo llamamos "string"
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
