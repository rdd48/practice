def get_score(chr):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    chr_score = alphabet.index(chr.lower()) + 1

    if chr.isupper():
        chr_score += 26

    # print(chr, chr_score)
    return chr_score

def rucksack_score(filename):

    with open(filename) as f:
        lines = f.readlines()

        score = 0
        for l in lines:
            line_len = len(l.strip())
            first = l[:line_len//2]
            second = l.strip()[line_len//2:]

            # slow way
            for i in first:
                if i in second:
                    score += get_score(i)
                    break
    
    return score

def rucksack_score2(filename):
    with open(filename) as f:
        lines = f.readlines()

        score = 0
        for idx in range(0, len(lines), 3):
            l1, l2, l3 = lines[idx].strip(), lines[idx+1].strip(), lines[idx+2].strip()

            # probably also the slow way
            in_first_two = ''
            for i in l1:
                if i in l2:
                    in_first_two += i
            
            for i in in_first_two:
                if i in l3:
                    score += get_score(i)
                    break
    
    return score


# print(rucksack_score('input/test.txt'))
# print(rucksack_score('input/03.txt'))

print(rucksack_score2('input/test.txt'))
print(rucksack_score2('input/03.txt'))