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


def get_line_points(coord, diagonal=False):
    # coord is a list of 2 lists
    # each inner list is in the form [x,y]
    # return a list of list line coordinates

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

    # line is horizontal
    elif starty == endy:
        if startx < endx:
            return [[i, starty] for i in range(startx, endx + 1)]
        else:
            return [[i, starty] for i in range(endx, startx + 1)]

    # line is diagonal
    if diagonal:
        if abs(startx - endx) == abs(starty - endy):
            new_coords = []
            if startx < endx and starty < endy:
                counter = 0
                for i in range(startx, endx + 1):
                    new_coords.append([i, starty + counter])
                    counter += 1
                return new_coords
            elif startx > endx and starty > endy:
                counter = 0
                for i in range(endx, startx + 1):
                    new_coords.append([i, endy + counter])
                    counter += 1
                return new_coords
            elif startx < endx and starty > endy:
                counter = 0
                for i in range(startx, endx + 1):
                    new_coords.append([i, starty - counter])
                    counter += 1
                return new_coords
            elif startx > endx and starty < endy:
                counter = 0
                for i in range(endx, startx + 1):
                    new_coords.append([i, endy - counter])
                    counter += 1
                return new_coords

    return []


def main(filename, diagonal=False):
    all_coords = process_input(filename)
    answer = 0
    overlaps = {}

    for c in all_coords:
        points = get_line_points(c, diagonal)
        if points:
            str_points = [f"{i[0]},{i[1]}" for i in points]
            for sp in str_points:
                if sp in overlaps:
                    overlaps[sp] += 1
                    if overlaps[sp] == 2:
                        answer += 1
                else:
                    overlaps[sp] = 1

    return answer


print(main("input/5_lines.txt"))
print(main("input/5_lines.txt", diagonal=True))

