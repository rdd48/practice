def is5pair(h):
    return True if h.count(max(h, key=h.count)) == 5 else False
def is4pair(h):
    return True if h.count(max(h, key=h.count)) == 4 else False
def isfullhouse(h):
    for i in h:
        if h.count(i) == 3 and h.count(h.replace(i, '')[0]) == 2:
            return True
    return False
def is3pair(h):
    return True if h.count(max(h, key=h.count)) == 3 else False
def is2pair(h):
    for i in h:
        if h.count(i) == 2:
            for j in h.replace(i, ''):
                if h.count(j) == 2:
                    return h 
    return False
def is1pair(h):
    return True if h.count(max(h, key=h.count)) == 2 else False

def part1(fname):
    r = 'AKQJT98765432'
    with open(fname) as f:
        lines = f.readlines()
        hands = [l.strip().split()[0] for l in lines if l.strip()]
        bids = [int(l.strip().split()[1]) for l in lines if l.strip()]
    
    pair5s, pair4s, fhs, pair3s, pair2s, pair1s, hicards = [], [], [], [], [], [], []
    for h, b in zip(hands, bids):
        if is5pair(h):
            pair5s.append((h, b))
        elif is4pair(h):
            pair4s.append((h, b))
        elif isfullhouse(h):
            fhs.append((h, b))
        elif is3pair(h):
            pair3s.append((h, b))
        elif is2pair(h):
            pair2s.append((h, b))
        elif is1pair(h):
            pair1s.append((h, b))
        else:
            hicards.append((h, b))

    rank = len(hands)
    total = 0
    all_hands = [pair5s, pair4s, fhs, pair3s, pair2s, pair1s, hicards]
    for ah in all_hands:
        ah.sort(key=lambda word: [r.index(c) for c in word[0]])
        for h in ah:
            total += rank * h[1]
            rank -= 1

    return total


def part2(fname):
    r2 = 'AKQT98765432J'

    with open(fname) as f:
        lines = f.readlines()
        hands = [l.strip().split()[0] for l in lines if l.strip()]
        bids = [int(l.strip().split()[1]) for l in lines if l.strip()]
    
    pair5s, pair4s, fhs, pair3s, pair2s, pair1s, hicards = [], [], [], [], [], [], []
    for h, b in zip(hands, bids):
        if 'J' not in h:
            if is5pair(h):
                pair5s.append((h, b))
            elif is4pair(h):
                pair4s.append((h, b))
            elif isfullhouse(h):
                fhs.append((h, b))
            elif is3pair(h):
                pair3s.append((h, b))
            elif is2pair(h):
                pair2s.append((h, b))
            elif is1pair(h):
                pair1s.append((h, b))
            else:
                hicards.append((h, b))
        else:
            if h.count('J') == 5:
                pair5s.append((h, b))
            elif h.count('J') + h.count(max(h.replace('J',''), key=h.count, default='')) == 5:
                pair5s.append((h, b))
            elif h.count('J') + h.count(max(h.replace('J',''), key=h.count, default='')) == 4:
                pair4s.append((h, b))
            elif h.count('J') == 1 and is2pair(h.replace('J','')): # full house case
                fhs.append((h, b))
            elif h.count('J') + h.count(max(h.replace('J',''), key=h.count, default='')) == 3:
                pair3s.append((h, b))
            elif h.count('J') == 1 and is1pair(h.replace('J','')):
                pair2s.append((h, b))
            elif h.count('J') + h.count(max(h.replace('J',''), key=h.count, default='')) == 2:
                pair1s.append((h, b))
            else:
                print(h)
                exit()

    
    rank = len(hands)
    total = 0
    all_hands = [pair5s, pair4s, fhs, pair3s, pair2s, pair1s, hicards]
    for ah in all_hands:
        ah.sort(key=lambda word: [r2.index(c) for c in word[0]])
        for h in ah:
            total += rank * h[1]
            rank -= 1

    return total

# print(part1('input/test.txt'))
print(part1('input/7.txt'))
# print(part2('input/test.txt'))
print(part2('input/7.txt'))
    