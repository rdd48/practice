def process_input(filename):
    """process input into a list of the input lines"""
    with open(filename) as f:
        lines = f.readlines()
        paren_list = [l.strip() for l in lines]
    return paren_list


def check_paren(s, part_one=True):
    """
    For part one: we want to get the offending closed parentheses that fails the line. If line is ok, return False.
    For part two: we want the remaining open parens that need to be closed for lines that work. If line fails, return False.
    """

    d = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }

    p_str = ''
    for ch in s:
        if ch in d.keys():  # d.keys() = closed brackets
            if len(p_str) == 0:
                return ch if part_one else False
            elif p_str[-1] == d[ch]:
                p_str = p_str[:-1]
            else:
                return ch if part_one else False
        elif ch in d.values():  # d.values() = open brackets
            p_str += ch

    return False if part_one else p_str


def main(filename):
    paren_list = process_input(filename)

    ans_str = ''

    for s in paren_list:
        paren = check_paren(s)
        if paren: 
            # i.e., if the string failed, paren is the character that failed
            ans_str += paren

    solution = (ans_str.count(')')) * 3
    solution += (ans_str.count(']')) * 57
    solution += (ans_str.count('}')) * 1197
    solution += (ans_str.count('>')) * 25137

    return solution


def main_2(filename):
    paren_list = process_input(filename)

    d = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }

    totals = []
    for s in paren_list:
        ans_str = 0
        paren = check_paren(s, part_one=False)
        if paren:

            # complete the unfinished parentheses (in the paren variable)
            # so reversing paren gives us the order of open parens to be closed.
            # for each paren to close, first multiply total by 5 then add the value corresponding to that paren,
            # e.g. closing ( gives you 1, [ gives you 2, etc.
            rev_paren = paren[::-1]
            for i in rev_paren:
                ans_str *= 5
                ans_str += d[i]
            totals.append(ans_str)

    # we need the midpoint, and the len is always odd. so get the midpoint via int division
    # and get the midpoint value of our sorted answers.
    totals.sort()
    mid = len(totals) // 2
    return totals[mid]


# part one
print(main('input/10_parens.txt'))

# part two
print(main_2('input/10_parens.txt'))
