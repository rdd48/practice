def process_input(filename):
    with open(filename) as f:
        lines = f.readlines()

        # all_points will be a list of coordinate lists
        # so each list within all_points contains two lists of xy coords
        all_coords = []

        for l in lines:
            both_coords = l.strip().split(" -> ")
            first_coords = both_coords[0].split(",")
            first_coords = [int(i) for i in first_coords]

            second_coords = both_coords[1].split(",")
            second_coords = [int(i) for i in second_coords]

            all_coords.append([first_coords, second_coords])

    return all_coords


def get_line_points(coord, check_diagonal=False):
    # coord is a list of 2 lists
    # each inner list is in the form [x,y]
    # return a list of len-2 list line coordinates

    startx, starty = coord[0][0], coord[0][1]
    endx, endy = coord[1][0], coord[1][1]

    # case where coords are all equal? not sure if this will happen
    if startx == endx and starty == endy:
        exit("probably will not happen")

    # case where line is vertical
    if startx == endx:
        if starty < endy:
            return [[startx, i] for i in range(starty, endy + 1)]
        else:
            return [[startx, i] for i in range(endy, starty + 1)]

    # case where line is horizontal
    elif starty == endy:
        if startx < endx:
            return [[i, starty] for i in range(startx, endx + 1)]
        else:
            return [[i, starty] for i in range(endx, startx + 1)]

    if check_diagonal:

        # case where line is diagonal
        if abs(startx - endx) == abs(starty - endy):
            new_coords = []

            # pos slope from down/left to up/right
            if startx < endx and starty < endy:
                return [[val, starty+idx] for (idx, val) in enumerate(range(startx, endx + 1))]

            # pos slope from up/right to down/left
            elif startx > endx and starty > endy:
                return [[val, endy+idx] for (idx, val) in enumerate(range(endx, startx+1))]

            # neg slope from up/left to down/right
            elif startx < endx and starty > endy:
                return [[val, starty-idx] for (idx, val) in enumerate(range(startx, endx + 1))]

            # neg slope from down/right to up/left
            elif startx > endx and starty < endy:
                return [[val, endy - idx] for (idx, val) in enumerate(range(endx, startx + 1))]

    # if not straight or 45-degree diagonal, return an empty list
    return []


def main(filename, check_diagonal=False):
    all_coords = process_input(filename)
    answer = 0
    overlaps = {}

    for c in all_coords:
        points = get_line_points(c, check_diagonal)
        if points:
            # str_points = [f"{i[0]},{i[1]}" for i in points]
            tuple_points = [(i[0], i[1]) for i in points]
            for tp in tuple_points:
                if tp in overlaps:
                    overlaps[tp] += 1
                    if overlaps[tp] == 2:
                        answer += 1
                else:
                    overlaps[tp] = 1

    return answer


print(main("input/5_lines.txt"))
print(main("input/5_lines.txt", check_diagonal=True))
