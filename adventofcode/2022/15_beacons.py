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
                    # print(x)
                    possible_beacons += 1
                    break
        
    # print(xmin, xmax)
    return possible_beacons


print(possible_beacons1('input/test.txt'))
print(possible_beacons1('input/15.txt'))
