import requests
from bs4 import BeautifulSoup

def seq_from_uniprot(uniprot_id):
    r = requests.get(f'https://www.uniprot.org/uniprot/{uniprot_id}.fasta',
                 headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    soup_list = soup.text.split('\n')
    seq = ''.join(soup_list[1:])
    return(seq)

if __name__ == '__main__':
    with open('input/rosalind_mprt.txt') as f:
        lines = f.readlines()
        for l in lines:
            seq = seq_from_uniprot(l.strip())
            sites = []
            for i in range(len(seq)-3):
                if seq[i] == 'N':
                    if seq[i+1] != 'P':
                        if seq[i+2] in ['S', 'T']:
                            if seq[i+3] != 'P':
                                sites.append(str(i+1))
            if len(sites) > 0:
                print(l.strip())
                #print(sites)
                print(' '.join(sites))
