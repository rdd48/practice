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
                h[0] = h.copy()[0] - dist

                # check that head moved further than tail & move tail
                if dist > 1:
                    t[0] = h.copy()[0] + 1
                    t[1] = h.copy()[1]

            elif direct == 'R':
                h[0] = h.copy()[0] + dist
                
                if dist > 1:
                    t[0] = h.copy()[0] - 1
                    t[1] = h.copy()[1]

            elif direct == 'D':
                # print(h[1])
                h[1] = h.copy()[1] - dist
                # print(h[1])

                if dist > 1:
                    t[1] = h.copy()[1] + 1
                    t[0] = h.copy()[0]

            elif direct == 'U':
                h[1] = h.copy()[1] + dist

                if dist > 1:
                    t[1] = h.copy()[1] - 1
                    t[0] = h.copy()[0]

            # compare start and end tail pos
            # but not when move dist was only 1
            # if dist < 2:
            #     continue

            # diagonally adjustment
            if start[0] != t[0] and start[1] != t[1]:
                # get x/y dirs it moved
                dx = 1 if start[0] < t[0] else -1
                dy = 1 if start[1] < t[1] else -1
                start[0] = start.copy()[0] + dx
                start[1] = start.copy()[1] + dy

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
            
            print(l, h, t)
            if _ > 15:
                exit()
    return len(t_pos)
            

#print(tail_states('input/test.txt'))
print(tail_states('input/09.txt'))