def codon_frecuency(sequence):
    # Validacion de existencia de secuencia
    if not sequence:
        raise ValueError("La secuencia proporcionada esta vacia.")
    #Validacion de caracteres
    sequence = sequence.upper()
    if any(c not in 'ACGTN' for c in sequence):
        raise ValueError("La secuencia contiene caracteres no validos.")
    
    #Diccionario de codones
    dic_codones = {}
    #Se va analizando de 3 en tres la secuencia
    for i in range(0,len(sequence),3):
        codon = sequence[i:i + 3]        
        if codon in dic_codones:
            dic_codones[codon] += 1
        else:
            dic_codones[codon] = 1

    return dic_codones

sequence = "ATGTGCTAGCGTATG"
print(codon_frecuency(sequence))