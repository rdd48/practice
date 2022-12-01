"""this code doesn't solve day 24. I'm leaving it here
to track the progress and ideas I had. the real solutions
are in the 24/ directory.

Huge thanks to this below reddit post for helping me understand how to 
approach this day's challenge. Probably wouldn't have solved it otherwise.
Turns out, this was more easily solved by hand for me.

https://www.reddit.com/r/adventofcode/comments/rom5l5/2021_day_24pen_paper_monad_deparsed/"""


def process_input(filename):
    rules = []
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip()
            rules.append(l.split())
    return rules


def is_str_int(s):
    try:
        return int(s)
    except ValueError:
        return None


def process_rule(r, val1, w, x, y, z):
    if is_str_int(r[2]) is not None:
        val2 = int(r[2])
    else:
        if r[2] == 'w':
            val2 = w
        elif r[2] == 'x':
            val2 = x
        elif r[2] == 'y':
            val2 = y
        elif r[2] == 'z':
            val2 = z

    if r[0] == 'add':
        return val1 + val2
    elif r[0] == 'mul':
        return val1 * val2
    elif r[0] == 'div':
        return val1 // val2
    elif r[0] == 'mod':
        return val1 % val2
    elif r[0] == 'eql':
        if val1 == val2:
            return 1
        else:
            return 0


def main(filename):
    rules = process_input(filename)

    max_val = 0
    num_times = 0
    total = 0

    for w in range(1, 10):
        for x in range(1, 10):
            for y in range(1, 10):
                for z in range(1, 10):
                    num_times += 1
                    print(num_times)

                    w, x, y, z = 9

                    ogw, ogx, ogy, ogz = w, x, y, z
                    for r in rules:
                        if r[1] == 'w':
                            if r[0] == 'inp':
                                w = ogw
                            else:
                                w = process_rule(r, w, w, x, y, z)
                        elif r[1] == 'x':
                            x = process_rule(r, x, w, x, y, z)
                        elif r[1] == 'y':
                            y = process_rule(r, y, w, x, y, z)
                        elif r[1] == 'z':
                            z = process_rule(r, z, w, x, y, z)

                    if z == 0:
                        total += 1
                    val = int(f'{w}{x}{y}{z}')
                    max_val = max(val, max_val)
                    exit()

    return total
    # return w, x, y, z


def reddit_helper():

    for i in reversed(range(99999999999999)):

        stack = []
        i_str = str(i)
        w, x, y, z = 0, 0, 0, 0

        for step_number in range(14):
            w = int(i_str[step_number])
            if len(stack) > 0:
                x = stack[-1]
            else:
                x = 0

            if step_number == 0:
                x += 12
            elif step_number == 1:
                x += 11
            elif step_number == 2:
                x += 14
            elif step_number == 3:
                stack.pop()
                x += -6
            elif step_number == 4:
                x += 15
            elif step_number == 5:
                x += 12
            elif step_number == 6:
                stack.pop()
                x += -9
            elif step_number == 7:
                x += 14
            elif step_number == 8:
                x += 14
            elif step_number == 9:
                stack.pop()
                x += -5
            elif step_number == 10:
                stack.pop()
                x += -9
            elif step_number == 11:
                stack.pop()
                x += -5
            elif step_number == 12:
                stack.pop()
                x += -2
            elif step_number == 13:
                stack.pop()
                x += -7

            if x != w:
                y = w

                if step_number == 0:
                    y += 4
                elif step_number == 1:
                    y += 10
                elif step_number == 2:
                    y += 12
                elif step_number == 3:
                    y += 14
                elif step_number == 4:
                    y += 6
                elif step_number == 5:
                    y += 16
                elif step_number == 6:
                    y += 1
                elif step_number == 7:
                    y += 7
                elif step_number == 8:
                    y += 8
                elif step_number == 9:
                    y += 11
                elif step_number == 10:
                    y += 8
                elif step_number == 11:
                    y += 3
                elif step_number == 12:
                    y += 1
                elif step_number == 13:
                    y += 8

                stack.append(y)

        if i % 100 == 0:
            print(i, len(stack))
        if len(stack) == 0:
            return i


print(reddit_helper())

# print(main('input/test.txt'))
# print(main('input/24_alu.txt'))
# t0 = time.time()
# for i in reversed(range(99999999999999)):
#     if i % 100 == 0:
#         print(i)
# print(time.time()-t0)
