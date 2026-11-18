from Bio import SeqIO
input_file = "raw_data/tp53_exon8_clean.fasta"
target_motif = "GGGAGCCT"
print("Sample_ID\tLength\tMotif_Found\tprotein_seq")
for record in SeqIO.parse(input_file, "fasta"):
     seq_len = len(record.seq)
     has_motif = "Yes" if target_motif in record.seq else "No (Mutated!)"
     protein = record.seq.translate()
     print(f"{record.id}\t{seq_len}\t{has_motif}\t{protein}")
