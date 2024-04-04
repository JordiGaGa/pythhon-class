"""
NAME: contador_ATGC
       

VERSION: 1.0
        

AUTHOR: JORDI GARCIA GARCES
        

DESCRIPTION: Programa para contar el numero de cada base nitrgoenada en archivo .txt
        

CATEGORY
        

USAGE

    python contador_ATGC [-parameters] [value]
    

ARGUMENTS 


METHOD


SEE ALSO
"""

import argparse
parser = argparse.ArgumentParser(description="contador ATGC")
parser.add_argument("input_file", type=str, help="..")
args = parser.parse_args()

with open(args.input_file, "r") as string:  # Aqui subimos el archivo y lo llamamos "string"
    # Convertimos el archivo a una string llamada "sec"
    sec = str(string.readline())
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
