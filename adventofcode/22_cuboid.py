"""Huge thanks to: https://pastebin.com/vKSar4KB for showing the way to the solution"""

import numpy as np


def process_input(filename):
    steps = []
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip()
            on_off, xyz = l.split(' ')
            x, y, z = xyz.split(',')
            x1, x2 = x[2:].split('..')
            x1, x2 = int(x1), int(x2)
            y1, y2 = y[2:].split('..')
            y1, y2 = int(y1), int(y2)
            z1, z2 = z[2:].split('..')
            z1, z2 = int(z1), int(z2)
            steps.append([on_off == 'on', (x1, x2), (y1, y2), (z1, z2)])

    return steps


def resize_input(axis):
    a1, a2 = axis[0], axis[1]
    if a1 < -50:
        a1 = -50
    elif a1 > 50:
        a1 = 50
    if a2 < -50:
        a2 = -50
    elif a2 > 50:
        a2 = 50

    if a1 == a2 == -50 or a1 == a2 == 50:
        return False

    # this resize thing was pretty clever, stole from https://pastebin.com/vKSar4KB
    return a1+50, a2+50


def main(filename):
    steps = process_input(filename)

    cuboid = np.zeros((101, 101, 101))

    for s in steps:
        on_off, x, y, z = s
        if on_off:
            val = 1
        else:
            val = 0

        if resize_input(x) and resize_input(y) and resize_input(z):
            x1, x2 = resize_input(x)
            y1, y2 = resize_input(y)
            z1, z2 = resize_input(z)
        else:
            continue

        cuboid[x1:x2+1, y1:y2+1, z1:z2+1] = val

    return int(np.sum(cuboid))


def main_2(filename):
    steps = process_input(filename)
    # again, great idea from the pastebin above to trim all cubes
    cubes = []

    for s in steps:
        on_off, x, y, z = s

        x1, x2 = x
        y1, y2 = y
        z1, z2 = z

        x2 += 1
        y2 += 1
        z2 += 1

        new_cubes = []
        for c in cubes:

            # check for overlap
            x_overlap = x2 > c[1] and x1 < c[2]
            y_overlap = y2 > c[3] and y1 < c[4]
            z_overlap = z2 > c[5] and z1 < c[6]

            if x_overlap and y_overlap and z_overlap:
                # i.e., existing cube starts first in x direction
                if x1 > c[1]:
                    new_cubes.append([c[0], c[1], x1, c[3], c[4], c[5], c[6]])
                    # trim the cube c we've been comparing our curr to
                    c[1] = x1

                # i.e., existing cube ends first in x direction
                if x2 < c[2]:
                    new_cubes.append([c[0], x2, c[2], c[3], c[4], c[5], c[6]])
                    c[2] = x2

                # now repeat for y and z
                if y1 > c[3]:
                    new_cubes.append([c[0], c[1], c[2], c[3], y1, c[5], c[6]])
                    c[3] = y1

                if y2 < c[4]:
                    new_cubes.append([c[0], c[1], c[2], y2, c[4], c[5], c[6]])
                    c[4] = y2

                if z1 > c[5]:
                    new_cubes.append([c[0], c[1], c[2], c[3], c[4], c[5], z1])
                    c[5] = z1

                if z2 < c[6]:
                    new_cubes.append([c[0], c[1], c[2], c[3], c[4], z2, c[6]])
                    c[6] = z2

            else:
                new_cubes.append(c)

        new_cubes.append([on_off, x1, x2, y1, y2, z1, z2])
        cubes = new_cubes

    total = 0
    for c in cubes:
        if c[0]:
            total += (c[2] - c[1]) * (c[4] - c[3]) * (c[6] - c[5])

    return total


# print(main('input/test.txt'))
print(main('input/22_cuboid.txt'))
# print(main_2('input/test.txt'))
print(main_2('input/22_cuboid.txt'))
