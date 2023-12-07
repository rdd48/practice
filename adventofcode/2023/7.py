def is5pair(h):
    for i in h:
        if h.count(i) == 5:
            return i*5
    return False
def is4pair(h):
    for i in h:
        if h.count(i) == 4:
            return (i*4) + h.replace(i,'')
    return False
def isfullhouse(h):
    for i in h:
        if h.count(i) == 3 and h.count(h.replace(i, '')[0]) == 2:
            return (i*3) + h.replace(i, '')
    return False
def is3pair(h):
    for i in h:
        if h.count(i) == 3:
            remain = h.replace(i, '')
            rc = ''.join(sorted(remain, key=lambda x:r.index(x)))
            return (i*3) + rc
    return False
def is2pair(h):
    for i in h:
        if h.count(i) == 2:
            for j in h.replace(i, ''):
                if h.count(j) == 2:
                    if r.index(i) > r.index(j):
                        return (i * 2) + (j * 2) + h.replace(i,'').replace(j,'')
                    elif r.index(i) < r.index(j):
                        return (j * 2) + (i * 2) + h.replace(i,'').replace(j,'')
    return False
def is1pair(h):
    for i in h:
        if h.count(i) == 2:
            remain = h.replace(i, '')
            rc = ''.join(sorted(remain, key=lambda x:r.index(x)))
            return (i*2) + rc
    return False

def part1(fname):
    global r 
    r = 'AKQJT98765432'
    with open(fname) as f:
        lines = f.readlines()
        hands = [l.strip().split()[0] for l in lines if l.strip()]
        bids = [int(l.strip().split()[1]) for l in lines if l.strip()]
    
    pair5s, pair4s, fhs, pair3s, pair2s, pair1s, hicards = [], [], [], [], [], [], []
    for h, b in zip(hands, bids):
        if x := is5pair(h):
            pair5s.append((x, b))
        elif x := is4pair(h):
            pair4s.append((x, b))
        elif x := isfullhouse(h):
            fhs.append((x, b))
        elif x := is3pair(h):
            pair3s.append((x, b))
        elif x := is2pair(h):
            pair2s.append((x, b))
        elif x := is1pair(h):
            pair1s.append((x, b))
        else:
            hicards.append((''.join(sorted(h, key=lambda x:r.index(x))), b))
    
    pair5s.sort(key=lambda x:r.index(x[0][0]))
    pair4s.sort(key=lambda word: [r.index(c) for c in word[0]])
    fhs.sort(key=lambda word: [r.index(c) for c in word[0]])
    pair3s.sort(key=lambda word: [r.index(c) for c in word[0]])
    pair2s.sort(key=lambda word: [r.index(c) for c in word[0]])
    pair1s.sort(key=lambda word: [r.index(c) for c in word[0]])
    hicards.sort(key=lambda word: [r.index(c) for c in word[0]])

    rank = len(hands)
    total = 0
    all_hands = [pair5s, pair4s, fhs, pair3s, pair2s, pair1s, hicards]
    for ah in all_hands:
        for h in ah:
            # print(h)
            total += rank * h[1]
            rank -= 1

    return total
    
print(part1('input/test.txt'))
# print(part1('input/7.txt'))


    
# pair5s, pair4s, fhs = [], {k:'' for k in r}, {k:'' for k in r}
#     pair3s, pair2s, pair1s, hicards = {k:{i:'' for i in r} for k in r}, [], [], []
#     for h, b in zip(hands, bids):
#         if x := is5pair(h):
#             pair5s.append((x, b))
#         elif x := is4pair(h):
#             pair4s[x[0]] = (x[1], b)
#         elif x := isfullhouse(h):
#             fhs[x[0]] = (x[-1], b)
#         elif x := is3pair(h):
#             pair3s[x[0]] = {x[-2]: x[-1]}