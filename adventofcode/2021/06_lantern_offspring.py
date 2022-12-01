def process_input(filename):
    # turn input into a list of ints. Each int represents a fish and its remaining years

    with open(filename) as f:
        lines = f.readlines()

    lines = lines[0].strip().split(',')
    return [int(i) for i in lines]


def fish_offspring(filename, days):
    # process input into a list of ints, and initialize a list of total fishes
    all_fishes = process_input(filename)
    total_fishes = len(all_fishes)

    # initialize a dictionary for counting total fish at each day-timer
    # keys = internal timer days, values = num fish
    d = {i: 0 for i in range(9)}
    for fish in all_fishes:
        d[fish] += 1

    # loop through num days
    for _ in range(days):
        for k, v in d.items():

            # for fish at day 0
            if k == 0:

                # increase num fishes total
                total_fishes += v

                # save new fishes to add to day 6 and reset day 8 after inner loop
                new_fishes = v

            else:
                # reduce day count by one of all fish in this day
                d[k-1] = v

        # reset all fish at 0 to 6 by adding to all 6s
        # (since 6 also includes fish that went 7 -> 6)
        d[6] += new_fishes

        # set new fish to have day 8 timer
        d[8] = new_fishes

    return total_fishes


# part one
# print(fish_offspring('input/test.txt', 18))
# print(fish_offspring('input/test.txt', 80))
print(fish_offspring('input/6_lanternfish.txt', 80))

# part two
# print(fish_offspring('input/test.txt', 256))
print(fish_offspring('input/6_lanternfish.txt', 256))
