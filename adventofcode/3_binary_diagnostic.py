def gamma_epsilon_rates(filename):
        
    with open(filename) as f:
        lines = f.readlines()
        d = {}
        for idx in range(len(lines[0].strip())):
            d[idx] = 0

        for l in lines:
            for idx, val in enumerate(l.strip()):
                d[idx] += int(val) # either 1 or 0
    
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(12):
        # check if 1 is more common or 0
        if float(d[i]) > float(len(lines)) / 2.:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    return float(int(gamma_rate,2)) * float(int(epsilon_rate,2))
    

def ogr_csr(filename):
    # org = oxygen generator rating
    # csr = co2 scrubber rating

    with open(filename) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]
        max_len = len(lines[0].strip())
        
        remaining_ocr = lines.copy()
        remaining_csr = lines.copy()

    pos = 0
    count = 0
    
    while True:
        for i in remaining_ocr:
            count += int(i[pos])
        
        if float(count) >= float(len(remaining_ocr)) / 2.:
            keep_val_ocr = '1'
        else:
            keep_val_ocr = '0'

        remaining_ocr = [i for i in remaining_ocr if i[pos] == keep_val_ocr]
        
        if len(remaining_ocr) == 1:
            ocr = remaining_ocr[0]
            # print(ocr)
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
    
    return float(int(ocr,2)) * float(int(csr,2))

print(ogr_csr('input/3_binary.txt'))
print(gamma_epsilon_rates('input/3_binary.txt'))
