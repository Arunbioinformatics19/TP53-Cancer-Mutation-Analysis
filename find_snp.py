from Bio import SeqIO
records = list(SeqIO.parse("raw_data/tp53_exon8_clean.fasta", "fasta"))
ref_record = max(records, key=lambda r: len(r.seq))
print("Reference Sample:", ref_record.id, "Length:", len(ref_record.seq))
print("_" * 50)
for rec in records:
     if str(rec.seq) in str(ref_record.seq):
         print(f"{rec,id}\t-> 100% Exact Match (Only Shorter Length)")
     else:
         print(f"{rec.id}\t-> MUTATION DETECTED! (Sequence Mismatch)")
