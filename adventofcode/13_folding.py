def process_input(filename):
    dots = []
    folds = []
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            if l.startswith('fold'):
                fold_axis = l.strip().split(' ')
                fold_axis = fold_axis[-1]
                fold_direction = fold_axis.split('=')[0]
                fold_dist = int(fold_axis.split('=')[1])
                folds.append([fold_direction, fold_dist])
            elif l.strip():
                xy = l.strip().split(',')
                dots.append((int(xy[0]), int(xy[1])))

    return dots, folds


def main(filename, part_one=True):
    dots, folds = process_input(filename)
    new_dots = []
    for fold in folds:
        fold_dir, fold_dist = fold[0], fold[1]
        if fold_dir == 'y':
            for dot in dots:
                if dot[1] < fold_dist:
                    if dot not in new_dots:
                        new_dots.append(dot)
                elif dot[1] > fold_dist:
                    new_y = fold_dist - (dot[1] - fold_dist)
                    if (dot[0], new_y) not in new_dots:
                        new_dots.append((dot[0], new_y))
        elif fold_dir == 'x':
            for dot in dots:
                if dot[0] < fold_dist:
                    if dot not in new_dots:
                        new_dots.append(dot)
                elif dot[0] > fold_dist:
                    new_x = fold_dist - (dot[0] - fold_dist)
                    if (new_x, dot[1]) not in new_dots:
                        new_dots.append((new_x, dot[1]))

        dots = new_dots
        new_dots = []

        if part_one:
            return len(dots)

    max_x = max(dots, key=lambda x: x[0])[0]
    max_y = max(dots, key=lambda x: x[1])[1]

    a = []
    for x in range(max_x+1):
        a.append(['.' for _ in range(max_y+1)])

    for d in dots:
        x, y = d[0], d[1]
        x_copy = a[x].copy()
        x_copy[5-y] = '#'
        a[x] = x_copy

    for row in a:
        print(''.join(row))

    return ''


print(main('input/13_folds.txt'))
print(main('input/13_folds.txt', part_one=False))
