from longest_motif import process_fasta

reverse_dict = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
}

def generate_reverse(frag):
    rev = ''
    for nt in frag:
        rev += reverse_dict[nt]
    return(rev[::-1])

def check_reverse(frag):
    rev = generate_reverse(frag)
    if rev == frag:
        return True
    return False

def main(fasta_file):
    names, fasta_dict = process_fasta(fasta_file)
    palindromes = []
    for n in names:
        seq = fasta_dict[n]
        for i in range(4, 13):
            for j in range(len(seq) - i + 1):
                frag = seq[j:j+i]
                if i == 18 and j == 4:
                    print(seq)
                if check_reverse(frag):
                    palindromes.append(f'{j + 1} {i}\n')
    return(''.join(palindromes))

print(main('input/rosalind_revp.txt'))