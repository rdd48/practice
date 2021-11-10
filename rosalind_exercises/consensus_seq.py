import numpy as np

# fasta_file = './test_fasta.txt'

def main(fasta_file):
    with open(fasta_file) as f:

        # 1. get len l of first fasta entry
        # 2. create l x 4 matrix
        # 3. for each entry in fasta, update matrix

        lines = f.readlines()

        nts = 'ACGT'

        num_seq = 0

        for i in range(len(lines)):
            if lines[i][0] == '>':
                seq = ''
                new_index = i + 1
                while lines[new_index][0] != '>':
                    seq += lines[new_index].strip()
                    new_index += 1
                    if new_index == len(lines):
                        break
                
                if num_seq == 0:
                    a = np.zeros((4, len(seq)), dtype='int')
                for nt_index in range(len(seq)):
                    nt_pos = nts.index(seq[nt_index])
                    a[nt_pos, nt_index] += 1
                
                num_seq += 1
    

    consensus = ''
    row, col = a.shape
    for c in range(col):
        max_idx = np.argmax(a[:,c])
        consensus += nts[max_idx]

    print(consensus)
    for r in range(row):
        lst = a[r,:].tolist()
        print(nts[r] + ': ' + ' '.join([str(l) for l in lst]))
    #return(consensus, a)

    

print(main('input/rosalind_cons.txt'))