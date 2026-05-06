from Bio import SeqIO

def qualidade_ok(record, min_q=20): #função que determina o mínimo de qualidade PHRED == 20
 quals = record.letter_annotations["phred_quality"]
 return sum(quals) / len(quals) >= min_q

reads=SeqIO.parse("reads.fastq", "fastq") #Abre o arq FASTQ
filtrados = [] #cria lista

for read in reads:#filtra os registros de qualidade e add na lista de filtrados
    qualidade_da_sequencia = qualidade_ok(read)
    if qualidade_da_sequencia == True:
        filtrados.append(read)
    else:
        print(read.id, "descartado!")
 
SeqIO.write(filtrados, "filtrados.fasta", "fasta") #escreve os registros filtrados em um novo FASTA
print("Total de registros filtrados:", len(filtrados))