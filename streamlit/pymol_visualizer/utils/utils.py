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
    def __init__(self, pdb):
        self.pdb = pdb

        self.chains = []
        self.sequence = ''

        for line in pdb:
            if line.startswith('ATOM'):
                if line[21] not in self.chains:
                    self.chains.append(line[21])
                if line[13:15] == 'N ':
                    self.sequence += aa_codes[line[17:20]]
    
    # def get_chains(self):
    #     return self.chains
    
    # def get_sequence(self):
    #     return self.sequence



def parse_pdb(pdb):
    '''function to get all pdb info manually. get_pdb_file returns a string, hence all the splitting.'''
    Pdb = PDBInfo(pdb)
    return Pdb.chains, Pdb.sequence

def download_fasta(pdb, seq):
    with open(f'{pdb}.fasta', 'w') as outfile:
        outfile.write(f'>{pdb}\n')
        outfile.write(seq)