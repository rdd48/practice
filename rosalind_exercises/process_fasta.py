def process_fasta(fasta_file):
    with open(fasta_file) as f:

        fasta_dict = {}

        lines = f.readlines()
        num_seq = 0

        names = []

        for i in range(len(lines)):
            if lines[i][0] == '>':
                name = lines[i][1:]
                names.append(name)
                seq = ''
                new_index = i + 1
                while lines[new_index][0] != '>':
                    seq += lines[new_index].strip()
                    new_index += 1
                    if new_index == len(lines):
                        break
                
                fasta_dict[name] = seq
                num_seq += 1
    
    return(names, fasta_dict)
