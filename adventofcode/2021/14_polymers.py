import re


def process_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        start = lines[0].strip()

        inserts = {}
        for l in lines[2:]:
            l = l.strip().split(' -> ')
            inserts[l[0]] = l[1]

    return start, inserts


def main(filename, num_steps):
    start, d = process_input(filename)

    for _ in range(num_steps):
        new_str = start[0]
        for i in range(len(start)-1):
            if start[i:i+2] in d:
                new_str += d[start[i:i+2]] + start[i+1]

        start = new_str

    d_count = {}
    for i in start:
        if i in d_count:
            d_count[i] += 1
        else:
            d_count[i] = 1

    return max(d_count.values()) - min(d_count.values())


def main_fast(filename, num_steps=10):
    start, inserts = process_input(filename)

    # first step to initiate totals dict
    # totals dict has keys that are len 2 substrings that will have the char inserted between them
    # values are the number of times this len 2 substr shows up
    totals = {k: 0 for k in inserts.keys()}
    for i in range(len(start)-1):
        first_two = start[i] + inserts[start[i:i+2]]
        second_two = inserts[start[i:i+2]] + start[i+1]

        totals[first_two] += 1
        totals[second_two] += 1

    # remaining steps we find the two new substrings that will be added based on our rules
    # e.g., if we have two 'ch' in our polymer ({... 'ch': 2}, ...), and the rule is that you insert b between ch
    # then our new dict should look like {...'cb': 2, 'bh': 2, 'ch': 0...}
    for _ in range(num_steps-1):
        new_totals = {k: 0 for k in inserts.keys()}
        for k, v in totals.items():
            new_char = inserts[k]
            new_totals[k[0] + new_char] += v
            new_totals[new_char + k[1]] += v

        totals = new_totals

    # counting characters: keys in totals are two characters
    # but to avoid double-counting, only count the number of times the first character shows up
    # then add one to the very last character to count that, since the starting last char will also
    # be the ending last char (as all new inserts are in between two chars)
    char_counts = {start[-1]: 1}
    for k, v in totals.items():
        first = k[0]
        if first not in char_counts:
            char_counts[first] = v
        else:
            char_counts[first] += v

    return max(char_counts.values()) - min(char_counts.values())


# part one, which i did the slow way first (doesn't work for 40 rounds)
print(main('input/14_polymer.txt', 10))
print(main_fast('input/14_polymer.txt', 10))
# part two
print(main_fast('input/14_polymer.txt', 40))
