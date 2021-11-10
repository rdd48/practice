from longest_motif import process_fasta

def main(fasta_file):
    names, fasta_dict = process_fasta(fasta_file)
    overlaps = []
    for i in range(len(names)):
        # overlap len == 3
        base_seq = fasta_dict[names[i]]
        tail = base_seq[-3:]
        for j in range(len(names)):
            if i != j:
                head = fasta_dict[names[j]][:3]
                if head == tail:
                    overlaps.append(f'{names[i].strip()} {names[j]}')
    
    return(''.join(overlaps))

print(main('input/rosalind_grph.txt'))