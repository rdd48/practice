def process_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        split_l = lines[0].split(',')

    return [int(i) for i in split_l]


def main(filename):
    starting_pos = process_input(filename)

    min_pos = min(starting_pos)
    max_pos = max(starting_pos)

    d = {i: 0 for i in range(min_pos, max_pos+1)}

    for i in starting_pos:
        for k in d.keys():
            d[k] += abs(i - k)

    return min(d.values())


def sum_recur(x):
    # this func works to sum all values from 1 to x, but hit max depth for some values in the input
    if x == 0 or x == 1:
        return x
    else:
        return x + sum_recur(x-1)


def sum_while(x):
    # this func is slow but gets the job done.
    if x == 0 or x == 1:
        return x
    else:
        total = 1
        i = 2
        while i <= x:
            total += i
            i += 1
        return total


def faster_sum_while(x, d):
    # this func is faster since it stores solutions found over time in a dictionary
    original_x = x
    if x == 0 or x == 1:
        return x, d
    else:
        total = 0
        while x > 0:
            if x in d:
                d[original_x] = total + d[x]
                return total + d[x], d
            else:
                total += x
                x -= 1

        d[original_x] = total
        return total, d


def main_2(filename):
    starting_pos = process_input(filename)

    min_pos = min(starting_pos)
    max_pos = max(starting_pos)

    d = {i: 0 for i in range(min_pos, max_pos+1)}
    sum_d = {
        0: 0,
        1: 1
    }

    for idx, i in enumerate(starting_pos):
        for k in d.keys():

            # maybe i can speed up by stopping when i've already calc'd a value?
            crab_length, sum_d = faster_sum_while(abs(i - k), sum_d)
            d[k] += crab_length

        # uncomment to make sure it's actually moving

        # len_total = len(starting_pos)
        # if (idx+1) % 10 == 0:
        #     print(f'{idx+1} out of {len_total}')

    return min(d.values())


# part 1
# print(main('input/test.txt'))
print(main('input/7_crabs.txt'))

# part 2
# print(main_2('input/test.txt'))
print(main_2('input/7_crabs.txt'))
