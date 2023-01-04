def man_dist(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2) + abs(y1-y2)

def rotate_right(degrees, wx, wy, x, y):
    for _ in range(degrees // 90):
        old_dwx = wx - x
        old_dwy = wy - y
        wx = x + old_dwy
        wy = y - old_dwx
    return wx, wy

def rotate_left(degrees, wx, wy, x, y):
    for _ in range(degrees // 90):
        old_dwx = wx - x
        old_dwy = wy - y
        wy = y + old_dwx
        wx = x - old_dwy
    return wx, wy

with open('input/12.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    directs = 'ESWN'

    # part one
    curr_direct = 0 # E
    pos = (0,0)
    for i in lines:
        new_direct, dist = i[0], int(i[1:])
        x,y = pos

        if new_direct == 'F':
            new_direct = directs[curr_direct]
        
        if new_direct == 'E':
            pos = (x+dist, y)
        elif new_direct == 'W':
            pos = (x-dist, y)
        elif new_direct == 'N':
            pos = (x, y+dist)
        elif new_direct == 'S':
            pos = (x, y-dist)
        elif new_direct == 'R':
            curr_direct = (curr_direct + (dist // 90)) % 4
        elif new_direct == 'L':
            curr_direct = (curr_direct - (dist // 90)) % 4
    print('part one: ', man_dist(pos, (0,0)))
    
    # part two
    curr_direct = 0 # E
    pos = (0,0)
    waypoint = (10,1)
    for i in lines:
        new_direct, dist = i[0], int(i[1:])
        x,y = pos
        wx, wy = waypoint
        if new_direct == 'F':
            dx = 1 if wx > x else -1
            dy = 1 if wy > y else -1

            pos = (x+(dx*(abs(wx-x)*dist)), y+(dy*(abs(wy-y)*dist)))
            waypoint = (pos[0]+(wx-x), pos[1]+(wy-y))

        elif new_direct == 'E':
            waypoint = (wx+dist, wy)
        elif new_direct == 'W':
            waypoint = (wx-dist, wy)
        elif new_direct == 'N':
            waypoint = (wx, wy+dist)
        elif new_direct == 'S':
            waypoint = (wx, wy-dist)
        
        elif new_direct == 'R':
            waypoint = rotate_right(dist, wx, wy, x, y)
        elif new_direct == 'L':
            waypoint = rotate_left(dist, wx, wy, x, y)
    
    print('part two: ', man_dist(pos, (0,0)))
        