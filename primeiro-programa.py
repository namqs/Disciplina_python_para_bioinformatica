from Bio.Seq import Seq #Importando da biblioteca Biopython

my_seq = Seq('AGTCAACGTACGTAA')

if (len(my_seq) % 3 == 0): #Se o tamanho da sequência for divisível por 3...
    print("Show! Da pra montar os codons")
else:
    print("Poxa, não da pra montar os codons")

