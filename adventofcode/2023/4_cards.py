def part1(fname):
    total = 0
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        for l in lines:
            subtotal = 0
            first, last = l.split('|')
            wl_ints = set([int(i) for i in first.split()[2:]])
            num_ints = set([int(i) for i in last.split()])

            for num in num_ints:
                if num in wl_ints:
                    subtotal += 1
            if subtotal:
                total += (2 ** (subtotal - 1))

    return total

def part2(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        card_nums = {i:1 for i in range(1, len(lines)+1)}
        for idx, l in enumerate(lines):
            subtotal = 0
            first, last = l.split('|')
            wl_ints = set([int(i) for i in first.split()[2:]])
            num_ints = set([int(i) for i in last.split()])
            
            for num in num_ints:
                if num in wl_ints:
                    subtotal += 1
            
            if subtotal:
                curr_cards = card_nums[idx+1]
                for new_card in range(idx+2, idx+subtotal+2):
                    card_nums[new_card] += curr_cards
    
    return sum(card_nums.values())

print(part1('input/test.txt'))
print(part1('input/4.txt'))
print(part2('input/test.txt'))
print(part2('input/4.txt'))