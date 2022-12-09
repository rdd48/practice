def calc_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (((y2 - y1)**2) + ((x2 - x1)**2))**0.5

def tail_states(fname):
    with open(fname) as f:
        lines = f.readlines()

        # head and tail positions
        h,t = [0,0], [0,0]

        # keep track of visited t positions in a set
        t_pos = set()
        
        for _, l in enumerate(lines):
            l = l.strip().split()
            direct, dist = l[0], int(l[1])

            start = t.copy()

            # move head & move tail laterally
            if direct == 'L':
                h[0] = h[0] - dist
                total_dist = calc_dist(h, t)

                # check that head moved further than tail & move tail
                if total_dist > 1.5:
                    t[0] = h[0] + 1
                    t[1] = h[1]

            elif direct == 'R':
                h[0] = h[0] + dist
                total_dist = calc_dist(h, t)
                
                if total_dist > 1.5:
                    t[0] = h[0] - 1
                    t[1] = h[1]

            elif direct == 'D':
                h[1] = h[1] - dist
                total_dist = calc_dist(h, t)

                if total_dist > 1.5:
                    t[1] = h[1] + 1
                    t[0] = h[0]

            elif direct == 'U':
                h[1] = h[1] + dist
                total_dist = calc_dist(h, t)

                if total_dist > 1.5:
                    t[1] = h[1] - 1
                    t[0] = h[0]

            # diagonally adjustment
            if start[0] != t[0] and start[1] != t[1]:
                # get x/y dirs it moved
                dx = 1 if start[0] < t[0] else -1
                dy = 1 if start[1] < t[1] else -1
                start[0] = start[0] + dx
                start[1] = start[1] + dy

                t_pos.add(tuple(start))
            
            # moved laterally on y
            if start[0] == t[0]:
                step = -1 if start[1] > t[1] else 1

                for i in range(start[1], t[1] + step, step):
                    start[1] = i
                    t_pos.add(tuple(start))
            
            # moved laterally on x
            elif start[1] == t[1]:
                step = -1 if start[0] > t[0] else 1

                for i in range(start[0], t[0] + step, step):
                    start[0] = i
                    t_pos.add(tuple(start))
            
    return len(t_pos)
            
# print(tail_states('input/test.txt'))
# print(tail_states('input/09.txt'))

def move_head(direct, dist, h, t):
    # move head & move tail laterally
    if direct == 'L':
        h[0] = h[0] - dist
        total_dist = calc_dist(h, t)

        # check that head moved further than tail & move tail
        if total_dist > 1.5:
            t[0] = h[0] + 1
            t[1] = h[1]

    elif direct == 'R':
        h[0] = h[0] + dist
        total_dist = calc_dist(h, t)
        
        if total_dist > 1.5:
            t[0] = h[0] - 1
            t[1] = h[1]

    elif direct == 'D':
        h[1] = h[1] - dist
        total_dist = calc_dist(h, t)

        if total_dist > 1.5:
            t[1] = h[1] + 1
            t[0] = h[0]

    elif direct == 'U':
        h[1] = h[1] + dist
        total_dist = calc_dist(h, t)

        if total_dist > 1.5:
            t[1] = h[1] - 1
            t[0] = h[0]
    
    return h, t

def move_rope(t1, t2):
    pass

def tail_states2(fname):
    with open(fname) as f:
        lines = f.readlines()

        # head and tail positions
        h,t1 = [0,0], [0,0]
        t2,t3,t4,t5,t6,t7,t8,t9 = [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]

        # keep track of visited t positions in a set
        t9_pos = set()
        
        for _, l in enumerate(lines):
            l = l.strip().split()
            direct, dist = l[0], int(l[1])

            h, t1 = move_head(direct, dist, h, t1)
            t1, t2 = move_rope(t1, t2)
            t2, t3 = move_rope(t2, t3)
            t3, t4 = move_rope(t3, t4)
            t4, t5 = move_rope(t4, t5)
            t5, t6 = move_rope(t5, t6)
            t6, t7 = move_rope(t6, t7)
            t7, t8 = move_rope(t7, t8)
            t8, t9 = move_rope(t8, t9)

            print(h,t1,t2,t3,t4,t5,t6,t7,t8,t9)

    # return len(t_pos)

print(tail_states2('input/test.txt'))
# print(tail_states('input/09.txt'))