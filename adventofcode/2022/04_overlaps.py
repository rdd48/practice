def count_overlaps(filename):

    with open(filename) as f:
        lines = f.readlines()

        score = 0
        for l in lines:
            first, last = l.strip().split(',')
            f1, f2 = int(first.split('-')[0]), int(first.split('-')[1])
            l1, l2 = int(last.split('-')[0]), int(last.split('-')[1])

            if f1 <= l1 and f2 >= l2:
                score += 1
            elif l1 <= f1 and l2 >= f2:
                score += 1
    
    return score

# print(count_overlaps('input/test.txt'))
print(count_overlaps('input/04.txt'))

def count_overlaps2(filename):

    with open(filename) as f:
        lines = f.readlines()

        score = 0
        for l in lines:
            first, last = l.strip().split(',')
            f1, f2 = int(first.split('-')[0]), int(first.split('-')[1])
            l1, l2 = int(last.split('-')[0]), int(last.split('-')[1])

            if f1 <= l1 and f2 >= l1:
                score += 1
            elif f1 >= l1 and l2 >= f1:
                score += 1
    
    return score

# print(count_overlaps2('input/test.txt'))
print(count_overlaps2('input/04.txt'))