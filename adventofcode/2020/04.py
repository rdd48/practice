def all_fields(curr, fields):
    for f in fields:
        if f not in curr:
            return False
    return True

# part one
with open('input/04.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = 0
    curr = ''
    for l in lines:
        if l:
            curr += l
        else:
            if all_fields(curr, fields):
                valid += 1
            curr = ''

    # check last passport
    if all_fields(curr, fields):
        valid += 1

    print(valid)

# part two
def check_field(i):
    k,v = i.split(':')
    if k == 'cid':
        return True
    if (k == 'byr') and (1920 <= int(v) <= 2002):
        return True
    elif (k == 'iyr') and (2010 <= int(v) <= 2020):
        return True
    elif (k == 'eyr') and (2020 <= int(v) <= 2030):
        return True
    elif (k == 'hgt'):
        if (v[-2:] == 'cm') and (150 <= int(v[:-2]) <= 193):
            return True
        if (v[-2:] == 'in') and (59 <= int(v[:-2]) <= 76):
            return True
    elif (k == 'hcl') and (v[0] == '#'):
        legal = '0123456789abcdef'
        for char in v[1:]:
            if char not in legal:
                return False
        return True
    elif (k == 'ecl'):
        if v in {'amb','blu','brn','gry','grn','hzl','oth'}:
            return True
    elif (k == 'pid') and (len(v) == 9):
        legal = '0123456789'
        for char in v:
            if char not in legal:
                return False
        return True
    return False

def check_part2_fields(lst):
    if not all_fields(''.join(lst), fields):
        return False
    for i in lst:
        if not check_field(i):
            return False
    return True

with open('input/04.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    valid2 = 0
    curr = []
    for l in lines:
        if l:
            for i in l.split():
                curr.append(i)
        else:
            if check_part2_fields(curr):
                valid2 += 1
            curr = []
    if check_part2_fields(curr):
        valid2 += 1
    print(valid2)


