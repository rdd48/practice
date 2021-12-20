''''
thank you thank you thank you to SwampThingTom. I stole a lot of his code for my solution.
https://github.com/SwampThingTom/AoC2021/blob/main/Python/19-BeaconScanner/BeaconScanner.py

I reaaaaaally struggled with this one. Still don't totally understand it. Also, runs like molasses.
'''


def process_input(filename):
    scanners = {}
    i = -1
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            if l[:3] == '---':
                i += 1
                new_list = []
            elif l.strip():
                x, y, z = l.strip().split(',')
                new_list.append((int(x), int(y), int(z)))
            else:
                scanners[i] = set(new_list)
                new_list = []
    if new_list:
        scanners[i] = set(new_list)
    return scanners


def move(points, delta):
    return set(add(point, delta) for point in points)


def difference(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])


def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2])


def orient(point, orientation):
    if orientation == 0:
        # (0, 1, 0)
        return point
    x, y, z = point
    if orientation == 1:
        # (0, -1, 0)
        return (x, -y, -z)
    if orientation == 2:
        # (1, 0, 0)
        return (y, x, -z)
    if orientation == 3:
        # (-1, 0, 0)
        return (y, -x, z)
    if orientation == 4:
        # (0, 0, 1)
        return (y, z, x)
    if orientation == 5:
        # (0, 0, -1)
        return (y, -z, -x)
    return None


def rotate(point, rotation):
    if rotation == 0:
        return point
    x, y, z = point
    if rotation == 1:
        return (z, y, -x)
    if rotation == 2:
        return (-x, y, -z)
    if rotation == 3:
        return (-z, y, x)
    return None


def transform(point, orientation, rotation):
    point = orient(point, orientation)
    return rotate(point, rotation)


def oriented_beacons(scanner, orientation):
    rot = orientation // 6
    ori = orientation % 6
    return set(transform(s, ori, rot) for s in scanner)


def find_match_between_scanners(found_scanner, ori_beacons, new_idx):
    for beacon1 in found_scanner:
        for beacon2 in ori_beacons:
            dist_diff = difference(beacon1, beacon2)
            moved = move(ori_beacons, dist_diff)

            if len(moved & found_scanner) >= 12:
                # found[new_idx] = moved
                return new_idx, moved, dist_diff
    return False


def find_match(found_scanner, all_found, scanners):
    output_list = []
    for new_idx, new_scanner in scanners.items():
        if new_idx not in all_found:
            for ori in range(24):
                ori_beacons = oriented_beacons(new_scanner, ori)
                match = find_match_between_scanners(
                    found_scanner, ori_beacons, new_idx)
                if match:
                    output_list.append(match)
                    break
    if output_list:
        return output_list
    return False


def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])


def main(filename):
    scanners = process_input(filename)
    found = {0: scanners[0]}
    found_dists = {0: (0, 0, 0)}
    found_tested = []

    # for s1 in range(1, len(scanners)):
    while len(found) < len(scanners):
        for found_idx, found_scanner in found.items():
            if found_idx not in found_tested:
                matches = find_match(found_scanner, found.keys(), scanners)
                if not matches:
                    continue
                else:
                    break

        found_tested.append(found_idx)
        for match in matches:
            found[match[0]] = match[1]
            found_dists[match[0]] = match[2]
            print(f'{match[0]}: {match[2]}')

    matched = []
    for k in found.keys():
        for v in found[k]:
            if v not in matched:
                matched.append(v)

    # print(len(matched))

    max_dist = 0
    for k1, v1 in found_dists.items():
        for k2, v2 in found_dists.items():
            if k1 != k2:
                dist = man_dist(v1, v2)
                if dist > max_dist:
                    max_dist = dist

    return len(matched), max_dist


# print(main('input/test.txt'))
print(main('input/19_scanners.txt'))
