def process_input(filename):
    a = []
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            a.append([int(i) for i in l.strip()])

    return a


def is_edge(x, y, a):
    num_rows = len(a)
    num_cols = len(a[0])
    top, right, bottom, left = False, False, False, False
    if x == 0:
        top = True
    elif x == num_rows - 1:
        bottom = True

    if y == 0:
        left = True
    elif y == num_cols - 1:
        right = True

    return top, right, bottom, left


def increase_one(a):
    for x in range(len(a)):
        for y in range(len(a[x])):
            a[x][y] += 1
    return a


def get_tens_and_up(a):
    tens = []
    for x in range(len(a)):
        for y in range(len(a[x])):
            if a[x][y] >= 10:
                tens.append([x, y])
    return tens


def flash_nbrs(x, y, a):
    top, right, bottom, left = is_edge(x, y, a)
    if not top:
        a[x-1][y] += 1
        if not left:
            a[x-1][y-1] += 1
        if not right:
            a[x-1][y+1] += 1
    if not bottom:
        a[x+1][y] += 1
        if not left:
            a[x+1][y-1] += 1
        if not right:
            a[x+1][y+1] += 1
    if not left:
        a[x][y-1] += 1
    if not right:
        a[x][y+1] += 1

    a[x][y] = 0
    return a


def main(filename):
    a = process_input(filename)
    a = increase_one(a)
    total = 0
    flash_points = []
    for _ in range(100):
        while True:
            tens = get_tens_and_up(a)

            for xy_list in tens:
                total += 1
                flash_points.append(xy_list)
                a = flash_nbrs(xy_list[0], xy_list[1], a)

            for xy_list in flash_points:
                a[xy_list[0]][xy_list[1]] = 0

            if len(get_tens_and_up(a)) == 0:
                a = increase_one(a)
                flash_points = []

                break

    return total


def main_2(filename):
    a = process_input(filename)
    a = increase_one(a)
    total = 0
    flash_points = []
    cycle = 0
    target = len(a) * len(a[0])
    while True:
        cycle += 1
        while True:
            tens = get_tens_and_up(a)

            for xy_list in tens:
                total += 1
                flash_points.append(xy_list)

                if len(flash_points) == target:
                    return cycle

                a = flash_nbrs(xy_list[0], xy_list[1], a)

            for xy_list in flash_points:
                a[xy_list[0]][xy_list[1]] = 0

            if len(get_tens_and_up(a)) == 0:
                a = increase_one(a)
                flash_points = []

                break


# print(main_2('input/test.txt'))
print(main_2('input/11_octopi.txt'))
