def calc_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return int((((y2 - y1)**2) + ((x2 - x1)**2))**0.5)

def move_head(direct, h, t):
    # move head & move tail laterally
    if direct == 'L':
        h[0] = h[0] - 1
        total_dist = calc_dist(h, t)

        # check that head moved further than tail & move tail
        if total_dist > 1.5:
            t[0] = h[0] + 1
            t[1] = h[1]

    elif direct == 'R':
        h[0] = h[0] + 1
        total_dist = calc_dist(h, t)
        
        if total_dist > 1.5:
            t[0] = h[0] - 1
            t[1] = h[1]

    elif direct == 'D':
        h[1] = h[1] - 1
        total_dist = calc_dist(h, t)

        if total_dist > 1.5:
            t[1] = h[1] + 1
            t[0] = h[0]

    elif direct == 'U':
        h[1] = h[1] + 1
        total_dist = calc_dist(h, t)

        if total_dist > 1.5:
            t[1] = h[1] - 1
            t[0] = h[0]
    
    return h, t

def move_rope(h, t):
    # return starting pos if close
    total_dist = calc_dist(h, t)
    if total_dist < 1.5:
        return h, t
    
    # determine direct to move t
    # check for diag movement
    if h[0] != t[0] and h[1] != t[1] and total_dist > 1.5:
        dx = 1 if t[0] < h[0] else -1
        dy = 1 if t[1] < h[1] else -1
        t[0] = t[0] + dx
        t[1] = t[1] + dy
    
    if total_dist < 1.5:
        return h, t

    # check now for x movement
    if h[0] != t[0]:
        x_dist = abs(h[0] - t[0])
        direct = 1 if t[0] < h[0] else -1
        t[0] = t[0] + ((x_dist - 1) * direct)
    
    # check now for y movement
    if h[1] != t[1]:
        y_dist = abs(h[1] - t[1])
        direct = 1 if t[1] < h[1] else -1
        t[1] = t[1] + ((y_dist - 1) * direct)

    return h, t


def count_rope_pos(fname, part2=False):
    with open(fname) as f:
        lines = f.readlines()

        # head and tail positions
        h,t1 = [0,0], [0,0]

        if part2:
            t2,t3,t4,t5,t6,t7,t8,t9 = [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]

        # keep track of visited t positions in a set
        tracked_pos = set()
        
        for l in lines:
            l = l.strip().split()
            direct, dist = l[0], int(l[1])

            # do this one step at a time
            for _ in range(dist):
                h, t1 = move_head(direct, h, t1)
                if not part2:
                    tracked_pos.add(tuple(t1))
                else:
                    t1, t2 = move_rope(t1, t2)
                    t2, t3 = move_rope(t2, t3)
                    t3, t4 = move_rope(t3, t4)
                    t4, t5 = move_rope(t4, t5)
                    t5, t6 = move_rope(t5, t6)
                    t6, t7 = move_rope(t6, t7)
                    t7, t8 = move_rope(t7, t8)
                    t8, t9 = move_rope(t8, t9)
                    tracked_pos.add(tuple(t9))

    return len(tracked_pos)

# print(move_rope('input/test.txt'))
print(count_rope_pos('input/09.txt'))
print(count_rope_pos('input/09.txt', part2=True))