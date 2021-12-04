def gamma_epsilon_rates(filename):
        
    with open(filename) as f:
        lines = f.readlines()
        binary_len = len(lines[0].strip())
        d = {}

        # create a dict of keys that are ints from (0, len binary item) with values of 0
        # assumes all binary items are the same len which was true for today's exercise
        # keys are sort of backward, in that key 0 is the leftmost (highest num) in binary, but works for today
        for idx in range(binary_len):
            d[idx] = 0

        # increase values in dict for each position in the binary number
        for l in lines:
            for idx, val in enumerate(l.strip()):
                d[idx] += int(val) # either 1 or 0
    
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(binary_len):
        # check if 1 is more common or 0
        if float(d[i]) > float(len(lines)) / 2.:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    return int(gamma_rate,2) * int(epsilon_rate,2)
    

def ogr_csr(filename):
    # ogr = oxygen generator rating
    # csr = co2 scrubber rating

    with open(filename) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]
        max_len = len(lines[0].strip())
        
        remaining_ogr = lines.copy()
        remaining_csr = lines.copy()

    pos = 0
    count = 0
    
    while True:
        for i in remaining_ogr:
            count += int(i[pos])
        
        if float(count) >= float(len(remaining_ogr)) / 2.:
            keep_val_ogr = '1'
        else:
            keep_val_ogr = '0'

        remaining_ogr = [i for i in remaining_ogr if i[pos] == keep_val_ogr]
        
        if len(remaining_ogr) == 1:
            ogr = remaining_ogr[0]
            # print(ogr)
            break
        elif pos+1 > max_len:
            return 'error: did not find a solution'
        else:
            pos += 1
            count = 0
    
    pos = 0
    count = 0

    while True:
        for i in remaining_csr:
            count += int(i[pos])
        
        if float(count) >= float(len(remaining_csr)) / 2.:
            keep_val_csr = '0'
        else:
            keep_val_csr = '1'

        remaining_csr = [i for i in remaining_csr if i[pos] == keep_val_csr]
        
        if len(remaining_csr) == 1:
            csr = remaining_csr[0]
            # print(csr)
            break
        elif pos+1 > max_len:
            return 'error: did not find a solution'
        else:
            pos += 1
            count = 0
    
    return int(ogr,2) * int(csr,2)

print(gamma_epsilon_rates('input/3_binary.txt'))
print(ogr_csr('input/3_binary.txt'))