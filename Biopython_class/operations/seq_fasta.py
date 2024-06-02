# Librerias 
import argparse
from Bio import SeqIO
from Bio.Seq import Seq

def encontrar_codones(marco, secuencia):
    """
    Encuentra todos los codones en el marco de lectura especificado.
    parametro marco: Marco de lectura (0, 1 o 2 para las secuencias originales y 3, 4 o 5 para las secuencias reversas).
    parametro secuencia: Secuencia de ADN.
    return: Lista de codones.
    """
    secuencia = secuencia[marco:]
    codones = [secuencia[i:i+3] for i in range(0, len(secuencia) - 2, 3)]
    return codones

def reverso_complementario(secuencia):
    """
    Obtiene la secuencia complementaria inversa.
    parametro secuencia: Secuencia de ADN.
    return: Secuencia complementaria inversa.
    """
    seq_obj = Seq(secuencia)
    return seq_obj.reverse_complement()

def codones_a_archivo(codones, header, archivo):
    """
    Escribe los codones en un archivo con formato FASTA.
    parametro codones: Lista de codones.
    parametro header: Encabezado de la secuencia.
    parametro archivo: Nombre del archivo de salida.
    """
    with open(archivo, 'a') as ar:
        ar.write(f">{header}\n")
        ar.write(' '.join(codones) + '\n')

def procesar_marco(marco, sequencia, header, output_prefix):
    """
    Procesa un marco de lectura y escribe los codones en un archivo.
    parametro marco: Marco de lectura (0 a 5).
    parametro secuencia: Secuencia de ADN.
    parametro header: Encabezado de la secuencia.
    parametro output_prefix: Prefijo para los archivos de salida.
    """
    if marco < 3:
        codones = encontrar_codones(marco, sequencia)
    else:
        rev_sec = reverso_complementario(sequencia)
        codones = encontrar_codones(marco - 3, str(rev_sec))
    
    output_filename = f'{output_prefix}_Frame{marco+1}.fa'
    codones_a_archivo(codones, header, output_filename)

def main():
    parser = argparse.ArgumentParser(description="Encuentra todos los codones en los 6 marcos de lectura de un archivo que contenga una secuencia de ADN.")
    parser.add_argument('input_file', help='Archivo FASTA de entrada con las secuencias de ADN.')
    parser.add_argument('output_prefix', help='Prefijo para los archivos de salida.')
    args = parser.parse_args()

    # Leer la secuencia de ADN desde el archivo FASTA
    secuencias = SeqIO.parse(args.input_file, "fasta")

    # Procesar los 6 marcos de lectura para cada secuencia en el archivo
    for secuencias in secuencias:
        for marco in range(6):
            procesar_marco(marco, str(secuencias.seq), secuencias.id, args.output_prefix)

if __name__ == "__main__":
    main()
