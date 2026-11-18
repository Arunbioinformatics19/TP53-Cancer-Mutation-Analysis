import matplotlib.pyplot as plt
from Bio import SeqIO
sample_ids =[]
lengths = []
colors = []
for rec in SeqIO.parse("raw_data/tp53_exon8_clean.fasta", "fasta"):
     sample_ids.append(rec.id)
     lengths.append(len(rec.seq))
     if rec.id == "MH366474.1":
         colors.append("red")
     else:
          colors.append("steelblue")

plt.figure(figsize=(10, 5))
plt.bar(sample_ids, lengths, color=colors)
plt.xticks(rotation=45)
plt.xlabel("Cancer Isolate ID")
plt.ylabel("Sequence Length (bp)")
plt.title("TP53 exon 8 Length Comparison (Red = Mutated Isolate)")
plt.tight_layout()
plt.savefig("results/tp53_mutation_chart.png", dpi=300)
print("Chart saved successfully!")
