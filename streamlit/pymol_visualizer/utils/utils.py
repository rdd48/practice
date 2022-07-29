from pypdb import get_info

aa_codes = {
    'ALA': 'A', 'CYS': 'C', 'ASP': 'D', 'GLU': 'E',
    'PHE': 'F', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I', 
    'LYS': 'K', 'LEU': 'L', 'MET': 'M', 'ASN': 'N',
    'PRO': 'P', 'GLN': 'Q', 'ARG': 'R', 'SER': 'S',
    'THR': 'T', 'VAL': 'V', 'TRP': 'W', 'TYR': 'Y',
    'UNK': '[unknown]'
} 

def get_name(pdb):
    pdb_data = get_info(pdb)
    return pdb_data['struct']['title'].title()

def get_rcsb_info(pdb):
    return get_info(pdb)
    
class PDBInfo:
    def __init__(self, pdb, pdb_lines):
        self.pdb = pdb
        self.pdb_lines = pdb_lines
        self.chains = {}
        self.backbone_atoms = []
        self.sidechain_atoms_by_aas = {aa: [] for aa in aa_codes.keys()}
        self.num_atoms = 0

        for line in pdb_lines:
            if line.startswith('ATOM'):
                self.num_atoms += 1
                if line[21] not in self.chains:
                    self.chains[line[21]] = ''
                if line[13:15] == 'N ':
                    aa = aa_codes[line[17:20]]
                    self.chains[line[21]] += aa
                    if line[17:20] not in self.sidechain_atoms_by_aas:
                        self.sidechain_atoms_by_aas[line[17:20]] = []
                atom_num = int(line[7:12])
                if line[13:15] not in ('N ', 'C ', 'CA', 'O '):
                    self.sidechain_atoms_by_aas[line[17:20]].append(atom_num)
                elif line[13:15] in ('N ', 'C ', 'CA'):
                    self.backbone_atoms.append(atom_num)
    
    def get_chains(self):
        return self.chains
    
    def get_sequence(self):
        sequence = ''
        for chain, chain_seq in self.chains.items():
            sequence += f'>{self.pdb}_{chain}\n'
            sequence += f'{chain_seq}\n'
        
        return sequence
    
    def get_one_line_sequence(self):
        one_line_seq = ''
        for i in self.chains.values():
            one_line_seq += i
        return one_line_seq
    
    def get_sidechain_atoms_by_aa(self, aa):
        return self.sidechain_atoms_by_aas[aa]


def parse_pdb(pdb, pdb_lines):
    '''function to get all pdb info manually. get_pdb_file returns a string, hence all the splitting.'''
    return PDBInfo(pdb, pdb_lines)

def download_fasta(pdb, seq):
    with open(f'{pdb}.fasta', 'w') as outfile:
        outfile.write(f'>{pdb}\n')
        outfile.write(seq)