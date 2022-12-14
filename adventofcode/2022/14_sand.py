import numpy as np


def process_input(fname, part2=False):
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        all_instruct = []
        max_x, max_y = 0, 0
        
        for l in lines:
            instruct = []
            lsplit = l.split(' -> ')
            for ls in lsplit:
                x, y = ls.split(',')
                x, y = int(x), int(y)
                instruct.append((x, y))
                
                max_x = x if x > max_x else max_x
                max_y = y if y > max_y else max_y
            
            all_instruct.append(instruct)
    
    a = np.zeros((max_y+3, max_x * 2), dtype='int')

    if part2:
        for x in range(max_x * 2):
            a[max_y+2, x] = 1

    for i in all_instruct:
        for idx, i1 in enumerate(i[:-1]):
            
            i2 = i[idx+1]
            x, y = i1
            x2, y2 = i2

            # draw horizontal
            if x != x2:
                direct = 1 if x < x2 else -1
                while x != x2:
                    a[y,x] = 1 # backwards-seeming because np is row, col
                    x += direct

            # draw vertical
            elif y != y2:
                direct = 1 if y < y2 else -1
                while y != y2:
                    a[y,x] = 1
                    y += direct
        
        # draw last part
        a[y,x] = 1
    
    return a

def drop_sand(fname, part2=False):
    
    a = process_input(fname, part2)

    sx, sy = 500, 0
    units = 0

    max_y = a.shape[0] - 2

    while True:
        
        if not part2:
            # will fall outside map
            if sy == max_y:
                return units

        # nothing is below
        if not a[sy+1, sx]:
            sy += 1
        
        # something is below
        # move diag to the left
        elif not a[sy+1, sx-1]:
            sy += 1
            sx -= 1
        
        # move diag to the right
        elif not a[sy+1, sx+1]:
            sy += 1
            sx += 1
        
        else:
            units += 1

            if part2:
                if sy == 0 and sx == 500:
                    return units

            a[sy,sx] = 1
            sx, sy = 500, 0

print(drop_sand('input/test.txt'))
print(drop_sand('input/14.txt'))

print(drop_sand('input/test.txt', part2=True))
print(drop_sand('input/14.txt', part2=True))


# recursive approach

def solve_recur(fname, part2=False):
    a = process_input(fname, part2)

    # sx, sy = 500, 0
    # units = 0

    max_y = a.shape[0] - 2

    return drop_sand_recur(fname, a, 500, 0, 0, max_y, part2)



def drop_sand_recur(fname, a, sx, sy, units, max_y, part2=False):

    if not part2:
        # will fall outside map
        if sy == max_y:
            return units

    # nothing is below
    if not a[sy+1, sx]:
        return drop_sand_recur(fname, a, sx, sy+1, units, max_y, part2)
    
    # something is below
    # move diag to the left
    elif not a[sy+1, sx-1]:
        return drop_sand_recur(fname, a, sx-1, sy+1, units, max_y, part2)

    # move diag to the right
    elif not a[sy+1, sx+1]:
        return drop_sand_recur(fname, a, sx+1, sy+1, units, max_y, part2)
    
    # sand stays here
    else:
        if part2:
            if sy == 0 and sx == 500:
                return units + 1
                
        a[sy,sx] = 1
        return drop_sand_recur(fname, a, 500, 0, units + 1, max_y, part2)


# recursive set up leads to stack overflow, but works on the test inputs, so I think it's correct
# print(solve_recur('input/test.txt'))
# print(solve_recur('input/14.txt'))

# print(solve_recur('input/test.txt', part2=True))
# print(solve_recur('input/14.txt', part2=True))
