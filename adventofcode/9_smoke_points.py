def process_input(filename):
    a = []
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            a.append([int(i) for i in l.strip()])

    return a


def check_neighbors(val, x, y, a, top, right, bottom, left):
    # return True if all neighbors are lower
    if not top:
        top_val = a[x-1][y]
        if val >= top_val:
            return None
    if not bottom:
        bottom_val = a[x+1][y]
        if val >= bottom_val:
            return None
    if not left:
        left_val = a[x][y-1]
        if val >= left_val:
            return None
    if not right:
        right_val = a[x][y+1]
        if val >= right_val:
            return None

    return val


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


def grow_recur(lp, basin_points=None):
    x, y, a, top, right, bottom, left = lp[0], lp[1], lp[2], lp[3], lp[4], lp[5], lp[6]

    if not basin_points:
        basin_points = [(x, y)]

    top, right, bottom, left = is_edge(x, y, a)
    val = a[x][y]

    if not top:
        top_val = a[x-1][y]
        if val <= top_val and top_val != 9:
            if (x-1, y) not in basin_points:
                basin_points.append((x-1, y))
                grow_recur([x-1, y, a, top, right, bottom, left], basin_points)

    if not bottom:
        bottom_val = a[x+1][y]
        if val <= bottom_val and bottom_val != 9:
            if (x+1, y) not in basin_points:
                basin_points.append((x+1, y))
                grow_recur([x+1, y, a, top, right, bottom, left], basin_points)
    if not left:
        left_val = a[x][y-1]
        if val <= left_val and left_val != 9:
            if (x, y-1) not in basin_points:
                basin_points.append((x, y-1))
                grow_recur([x, y-1, a, top, right, bottom, left], basin_points)
    if not right:
        right_val = a[x][y+1]
        if val <= right_val and right_val != 9:
            if (x, y+1) not in basin_points:
                basin_points.append((x, y+1))
                grow_recur([x, y+1, a, top, right, bottom, left], basin_points)

    return len(basin_points)


def main(filename):
    a = process_input(filename)

    num_rows = len(a)
    num_cols = len(a[0])

    total = 0

    # loop through rows
    for xidx, x in enumerate(a):
        for yidx, val in enumerate(x):
            top, right, bottom, left = False, False, False, False
            if xidx == 0:
                top = True
            elif xidx == num_rows - 1:
                bottom = True

            if yidx == 0:
                left = True
            elif yidx == num_cols - 1:
                right = True

            val = check_neighbors(val, xidx, yidx, a, top, right, bottom, left)

            if val is not None:
                total += val + 1

    return total


def main_2(filename):
    a = process_input(filename)

    num_rows = len(a)
    num_cols = len(a[0])

    low_points = []

    # loop through rows
    for xidx, x in enumerate(a):
        for yidx, val in enumerate(x):
            top, right, bottom, left = False, False, False, False
            if xidx == 0:
                top = True
            elif xidx == num_rows - 1:
                bottom = True

            if yidx == 0:
                left = True
            elif yidx == num_cols - 1:
                right = True

            val = check_neighbors(val, xidx, yidx, a, top, right, bottom, left)

            if val is not None:
                low_points.append([xidx, yidx, a, top, right, bottom, left])

    all_basins = []
    for lp in low_points:
        basin_size = grow_recur(lp)
        all_basins.append(basin_size)

    all_basins.sort(reverse=True)
    top_basins = all_basins[:3]
    total = 1
    for tb in top_basins:
        total *= tb
    return total


print(main_2('input/test.txt'))
print(main_2('input/9_low_points.txt'))
