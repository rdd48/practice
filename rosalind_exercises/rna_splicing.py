from translate_rna import translate_rna
from longest_motif import process_fasta

names, fasta_dict = process_fasta('input/rosalind_splc.txt')

base_seq = fasta_dict[names[0]]

for name in names[1:]:
    seq = fasta_dict[name]
    if seq in base_seq:
        split_seq = base_seq.split(seq)
        base_seq = ''.join(split_seq)

base_seq = base_seq.replace('T', 'U')

print(translate_rna(base_seq))