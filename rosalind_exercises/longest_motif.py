
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

def get_shared_motifs(str1, str2):
    shared_motifs = []
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i:i+2] == str2[j:j+2]:
                if str1[i:i+2] not in shared_motifs and len(str1[i:i+2]) >= 2:
                    shared_motifs.append(str1[i:i+2])
                increase = 3
                while True:
                    if (i+increase >= len(str1)) or (j+increase >= len(str2)):
                        break
                    if str1[i:i+increase] == str2[j:j+increase]:
                        if str1[i:i+increase] not in shared_motifs and len(str1[i:i+increase]) >= 2:
                            shared_motifs.append(str1[i:i+increase])
                        increase += 1
                    else:
                        break
    return(shared_motifs)

def get_common_list_items(lst1, lst2):
    return [i for i in lst1 if i in lst2]

def get_max_str(lst):
    return max(lst, key=len)

def main(fasta_file):
    names, fasta_dict = process_fasta(fasta_file)
    all_shared = []
    for i in range(len(names)):
        if i < len(names) - 1:
            # compare this str with next str
            shared_motifs = get_shared_motifs(fasta_dict[names[i]], fasta_dict[names[i+1]])
            if i == 0:
                all_shared = shared_motifs
            else:
                curr_shared = []
                for sm in shared_motifs:
                    if sm in all_shared:
                        curr_shared.append(sm)
                all_shared = curr_shared
            if i == len(names) - 2:
                return(get_max_str(all_shared))

# so my slow method is below
# this method here uses binary search to find the maximum length of a substring in all strings
# jesus christ this is smart

def substr_in_all(arr, part):

  # returns True only if the part is found in all dna sequences in the array

  for dna in arr:
    # if dna.find(part)==-1:
    if part not in dna:
      return False
  return True

def common_substr(arr, l):
  first = arr[0]

  # i added this to prevent float errors
  l = int(l)

  # loop from 0 to (end - midpoint)
  for i in range(len(first)-l+1):

    part = first[i:i+l]

    if substr_in_all(arr, part):
      return part
  return ""

def longest_common_substr(arr):
  # initializes starting left = 0, right = array length
  l = 0; r = len(arr[0])

  while l+1<r:
    # initialize midpoint in middle of dna
    mid = (l+r) / 2

    if common_substr(arr, mid)!="":
      # i.e., if we find a substring, next look from mid value to end
      # then lengthen the search window
      
      print(f'l {l} => {mid}, {common_substr(arr, mid)}')
      l=mid

    else:
      # i.e., if we don't find a substring, next look from beginning to mid value
      # think of this as: shorten by half each time
      print(f'r {r} => {mid}')
      r=mid

  return common_substr(arr, l)

def wrapper(fasta_file):
    names, fasta_dict =  process_fasta(fasta_file)
    arr = [fasta_dict[n] for n in names]
    return longest_common_substr(arr)

# print(wrapper('test.fasta'))
# print(wrapper('input/rosalind_lcsm.txt'))
# print(main('input/rosalind_lcsm.txt'))

# print(get_shared_motifs('ACTGACAT', 'GACTGCACAT'))