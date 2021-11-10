from longest_motif import process_fasta

codon_dict = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
    "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
    "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
    "TGT":"C", "TGC":"C", "TGA":"*", "TGG":"W",
    "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
    "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
    "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
    "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

rev_dict = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}

# goal: find all reading frames.
# 1. get translation and 3->5 translation
# 2. get all M, *
# 3. get all seqs from that ORF from M:*
# 4. repeat for all 5 other ORFs

def reverse_dna(dna):
    rev_dna = dna[::-1]
    compl_dna = ''
    for nt in rev_dna:
        compl_dna += rev_dict[nt]
    return compl_dna


def translate_dna(dna):
    trans = [codon_dict[dna[i:i+3]] for i in range(0,len(dna),3) if len(dna[i:i+3]) == 3]
    return ''.join(trans)

def get_all_aas(dna, aa):
    trans = translate_dna(dna)
    all_pos = []
    for i in range(len(trans)):
        if trans[i] == aa:
            all_pos.append(i)
    return all_pos

def get_next_stop(m_idx, stop_list):
    for s in stop_list:
        if s > m_idx:
            return s
    return False


def gen_orfs(dna):
    rev_dna = reverse_dna(dna)
    # rev_dna_2 = reverse_dna(dna[:-1])
    # rev_dna_3 = reverse_dna(dna[:-2])
    return [dna, dna[1:], dna[2:], rev_dna, rev_dna[1:], rev_dna[2:]]

names, fasta_dict = process_fasta('input/rosalind_orf.txt')

dna = fasta_dict[names[0]]

orfs = gen_orfs(dna)
# print(orfs)
proteins = []
for orf in orfs:
    m_list = get_all_aas(orf, 'M')
    stop_list = get_all_aas(orf, '*')
    protein = translate_dna(orf)
    for m in m_list:
        stop = get_next_stop(m, stop_list)
        if stop and protein[m:stop] not in proteins:
            proteins.append(protein[m:stop])
for i in proteins:
    print(i)