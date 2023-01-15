def add_mask(mask, bin_val):
    # pad bin_val to 36 with leading 0s
    bin_val = ('0' * (36-len(bin_val))) + bin_val

    masked_val = ''
    for b, m in zip(bin_val, mask):
        if m in ('0', '1'):
            masked_val = masked_val + m
        else:
            masked_val = masked_val + b

    return masked_val

# part one
with open('input/14.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    d = {}
    for l in lines:
        if l.startswith('mask'):
            mask = l.split()[-1]
        elif l.startswith('mem'):
            address = int(l[l.index('[')+1:l.index(']')])
            dec_val = l.split()[-1]
            bin_val = bin(int(dec_val))[2:]

            if address not in d:
                d[address] = ''
            d[address] = add_mask(mask, bin_val)
    
    ans = 0
    for v in d.values():
        ans += int(v, 2)
    print('part one: ', ans)

def add_mask_to_address(mask, bin_val):
    # pad bin_val to 36 with leading 0s
    bin_val = ('0' * (36-len(bin_val))) + bin_val

    masked_val = ''
    for b, m in zip(bin_val, mask):
        if m == '1':
            masked_val = masked_val + m
        elif m == 'X':
            masked_val = masked_val + 'X'
        else:
            masked_val = masked_val + b
            
    return masked_val

def get_all_addresses(masked_address):
    addresses = ['']
    while len(masked_address):
        
        val = masked_address[-1]
        masked_address = masked_address[:-1]
        if val == 'X':
            new_a = []
            for a in addresses:
                a0 = '0' + a
                new_a.append(a0)
                a1 = '1' + a
                new_a.append(a1)
            addresses = new_a
    
        else:
            new_a = []
            for a in addresses:
                a = val + a
                new_a.append(a)
            addresses = new_a

    return addresses

# part two
with open('input/14.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    d = {}
    for l in lines:
        if l.startswith('mask'):
            mask = l.split()[-1]
        elif l.startswith('mem'):
            address = int(l[l.index('[')+1:l.index(']')])
            dec_val = l.split()[-1]

            addresses = get_all_addresses(add_mask_to_address(mask, bin(address)[2:]))
            for a in addresses:
                dec_a = int(a, 2)
                if dec_a not in d:
                    d[dec_a] = ''
                d[dec_a] = int(dec_val)
    
    ans = 0
    for v in d.values():
        ans += v
    print('part two: ', ans)