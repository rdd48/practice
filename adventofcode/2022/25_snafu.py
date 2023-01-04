def convert_b5(num):
    running_num = ''
    while num != 0:
        num, m = num // 5, num % 5
        running_num = str(m) + running_num
        
    return running_num

def b5_to_snafu(num):
    # 1243 in base 5
    # e.g. 2=0= in snafu
    # convert by: if 3, 4, or 5, -5 and add 1 to next col?
    b5_str = convert_b5(num)
    snafu = ''
    correction = 0
    for i in b5_str[::-1]:
        i = str(int(i) + correction)
        if i in ('0', '1', '2'):
            snafu = i + snafu
            correction = 0
        else:
            correction = 1
            if i == '3':
                snafu = '=' + snafu
            elif i == '4':
                snafu = '-' + snafu
            elif i == '5':
                snafu = '0' + snafu
    
    if correction:
        snafu = '1' + snafu
    return snafu

def convert_to_snafu(fname):
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]
    
    snafu_sum = 0
    for l in lines:
        # convert snafu here
        snafu = 0
        for idx, i in enumerate(l[::-1]):
            base_val = 5 ** idx
            if i in ('1', '2'):
                snafu += base_val * int(i)
            elif i == '-':
                snafu -= base_val
            elif i == '=':
                snafu -= (base_val * 2)
        snafu_sum += snafu
    
    print(snafu_sum)
    return b5_to_snafu(snafu_sum)
    

print(convert_to_snafu('input/test.txt'))
print(convert_to_snafu('input/25.txt'))



