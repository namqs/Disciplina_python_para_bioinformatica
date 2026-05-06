from Bio import SeqIO
# Converte FASTQ ³ FASTA em uma linha
SeqIO.convert("reads.fastq", "fastq",
 "reads.fasta", "fasta")