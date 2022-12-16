# huge thanks to https://github.com/tipa16384/adventofcode/blob/main/2022/puzzle15.py
# otherwise i wasn't getting very close

def calc_man_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2-x1) + abs(y2-y1)

def inp_str_to_ints(s):
    s = s.replace('x=','').replace('y=','').replace(' ','').strip()
    return eval(f'({s})')

def possible_beacons1(fname):
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        sensors, beacons = [], []

        for l in lines:
            l = l.replace('Sensor at ','').replace(' closest beacon is at ','')
            p1, p2 = l.split(':')
            sensors.append(inp_str_to_ints(p1))
            beacons.append(inp_str_to_ints(p2))
    
    # get man distance for each sensor / beacon pair
    man_dists = []
    for s, b in zip(sensors, beacons):
        man_dists.append(calc_man_dist(s, b))

    # also need min/max x for part1 which is dependent on distance from sensor
    xmin, xmax = float('inf'), 0
    for s, md in zip(sensors, man_dists):
        x = s[0]
        if x - md < xmin:
            xmin = x - md
        if x + md > xmax:
            xmax = x + md
    
    possible_beacons = 0
    # part1: see if beacon can be present in given row for all x values
    y = 10 if 'test' in fname else 2000000

    # don't count it if a beacon is already there
    beacons_at_row = [b for b in beacons if b[1] == y]
    
    for x in range(xmin, xmax):
        # this code is slow, so adding a tracker
        if not x % 10000:
            print(x)

        for s, md in zip(sensors, man_dists):
            curr_dist = calc_man_dist(s, (x, y))
            if curr_dist <= md:
                if (x, y) not in beacons_at_row:
                    possible_beacons += 1
                    break
        
    # print(xmin, xmax)
    return possible_beacons


# print(possible_beacons1('input/test.txt'))
print(possible_beacons1('input/15.txt'))


def add_point_to_set(s, x, y):
    if x >= 0 and x <= 4000000 and y >= 0 and y <= 4000000:
        s.add((x, y))
    return s

def is_inside(sensors, man_dists, x, y):
    for s, md in zip(sensors, man_dists):
        sx, sy = s
        if calc_man_dist((sx, sy), (x, y)) <= md:
            return True
    return False

def possible_beacons2(fname):
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        sensors, beacons = [], []

        for l in lines:
            l = l.replace('Sensor at ','').replace(' closest beacon is at ','')
            p1, p2 = l.split(':')
            sensors.append(inp_str_to_ints(p1))
            beacons.append(inp_str_to_ints(p2))
    
    # get man distance for each sensor / beacon pair
    man_dists = []
    all_possibles = {}
    
    for s, b in zip(sensors, beacons):
        man_dists.append(calc_man_dist(s, b))
    
        
    idx = 0 
    for s, md in zip(sensors, man_dists):
        # get possible points for all sensor
        print(idx)
        possibles = set()
        sx, sy = s
        idx += 1

        for d in range(md+2):
            possibles = add_point_to_set(possibles, sx - md - 1 + d, sy + d)
            possibles = add_point_to_set(possibles, sx + md + 1 - d, sy + d)
            possibles = add_point_to_set(possibles, sx - md - 1 + d, sy - d)
            possibles = add_point_to_set(possibles, sx + md + 1 - d, sy - d)
    
        all_possibles[(sx, sy)] = possibles

    ans = {}
    for v in all_possibles.values():
        for p in v:
            x, y = p
            if (x,y) not in ans:
                ans[(x,y)] = 0
            ans[(x,y)] += 1
            
            # this is the clever part: the only free part is one where the added buffer 
            # from each diamond is found in (at least) 4 different sensors
            if ans[(x,y)] >= 4:

                # make sure the diamond is not inside other sensors diamonds
                if not is_inside(sensors, man_dists, x, y):
                    return x * 4000000 + y

print(possible_beacons2('input/test.txt'))
print(possible_beacons2('input/15.txt'))