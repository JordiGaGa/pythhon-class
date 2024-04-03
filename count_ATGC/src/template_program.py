'''
NAME: Contador de A,T,G,C
       

VERSION: 1.0
        

AUTHOR: JORDI GARCIA GARCES
        

DESCRIPTION: Programa para contar el numero de cada base nitrgoenada en archivo .txt
        

CATEGORY
        

USAGE

    % python programName [-parameters] [value]
    

ARGUMENTS 


METHOD


SEE ALSO

# ===========================================================================

from google.colab import files

upload = files.upload()

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

# ===========================================================================
