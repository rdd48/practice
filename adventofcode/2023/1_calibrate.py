def isint(char):
    try:
        int(char)
        return True
    except:
        return False

def isstrint(char):
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx, w in enumerate(words):
        if char.startswith(w):
            return idx + 1
    return False

def isstrintrev(char):
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx, w in enumerate(words):
        if char.endswith(w):
            return idx + 1
    return False

def part1(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        total = 0
        for l in lines:
            str_num = ''
            for i in l:
                if isint(i):
                    str_num = i
                    break
            for i in l[::-1]:
                if isint(i):
                    str_num += i
                    break
            total += int(str_num)
    return total

def part2(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        total = 0
        for l in lines:
            str_num = ''
            for idx, i in enumerate(l):
                if isint(i):
                    str_num = i
                    break
                elif isstrint(l[idx:]):
                    str_num = str(isstrint(l[idx:]))
                    break
            for idx, i in enumerate(l[::-1]):
                if isint(i):
                    str_num += i
                    break
                elif isstrintrev(l[:len(l)-idx]):
                    str_num += str(isstrintrev(l[:len(l)-idx]))
                    print(l[:len(l)-idx], isstrintrev(l[:len(l)-idx]))
                    break
            total += int(str_num)
    return total

print(part1('input/1.txt'))
print(part2('input/1.txt'))