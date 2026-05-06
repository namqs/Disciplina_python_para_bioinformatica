import sys
from Bio import SeqIO

# Lendo um arquivo FASTA
for record in SeqIO.parse(sys.argv[1], "fasta"): #indica o arquivo e o tipo
 print(record.id) # ID da sequência
 print(str(record.seq)) # A sequência em si
 print(record.description) # Descrição completa