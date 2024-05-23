import Bio.Seq
import re 

#String pasada a objeto seq
seq_obj = Bio.Seq.Seq('ATGCGTGATTGAATC')

#Se regresa a string para el len
seq_str = str(seq_obj)
print(f'{seq_str} tiene {len(seq_str)} nucleotidos')

#Se saca la reversa complementaria de la cadena 
tseq_obj = seq_obj.reverse_complement()
print(f'cadena reverso complementaria {tseq_obj}')

#Cadena de aminoacidos de la secuencia respetando si hay codon de paro
seq_amn = seq_obj.translate(to_stop = True)

print(f'La cadena de aminoacidos de la cadena original es {seq_amn}')

#Version de RNA de la cadena y retrotranscrita 
rna = seq_obj.transcribe()
retrna = rna.back_transcribe()
print(f'La cadena original como RNA es {rna}')
print(f'La cadena de RNA regresada a DNA es {retrna}')

#  Se imprime cada codon por separado 
for codon in re.findall(r"(.{3})", str(seq_obj)):
    print(codon)
