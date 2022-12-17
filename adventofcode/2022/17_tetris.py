def get_coords(piece_num, y):
    coords = {
        0: [(2, y), (3, y), (4, y), (5, y)],
        1: [(2, y+1), (3, y), (3, y+1), (3, y+2), (4, y+1)],
        2: [(2, y), (3, y), (4, y), (4, y+1), (4, y+2)],
        3: [(2, y), (2, y+1), (2, y+2), (2, y+3)],
        4: [(2, y), (3, y), (2, y+1), (3, y+1)],
    }

    return coords[piece_num]

def tetris(fname, rounds):
    with open(fname) as f:
        dirs = f.readline().strip()
    
    width = 7
    fall_y = 4
    dir_idx = 0
    occupied = set([(x,0) for x in range(7)])

    # store the highest point for each x in our grid
    max_x = [0] * width

    for round in range(rounds):
        falling = True
        piece_idx = round % 5
        coords = get_coords(piece_idx, fall_y)
        
        # print(round, coords)
        while falling:
            # first move laterally
            dir = dirs[dir_idx % len(dirs)]

            # move left if leftmost x > 0
            if dir == '<' and coords[0][0] > 0:
                new_coords = [(x-1, y) for x,y in coords]
                if not set(new_coords).intersection(occupied):
                    coords = new_coords
            
            # move right if rightmost x < width
            elif dir == '>' and coords[-1][0] < width-1:
                new_coords = [(x+1, y) for x,y in coords]
                if not set(new_coords).intersection(occupied):
                    coords = new_coords
            
            dir_idx += 1

            # check if falls or at rest
            for c in coords:
                x,y = c
        
                # piece is one above so it stops falling
                if (x, y - 1) in occupied:
                    # update max_x
                    for x,y in coords:
                        if y > max_x[x]:
                            max_x[x] = y
                        occupied.add((x,y))
                    
                    # update global max y
                    fall_y = max(max_x) + 4

                    falling = False
                    break
            
            if falling:
                # piece didn't hit anything so we decrease y_coords by 1
                coords = [(x, y-1) for x,y in coords]
        
    return max(max_x)


# print(tetris('input/test.txt', 2022))
print(tetris('input/17.txt', 2022))

def tetris2(fname, rounds):

    with open(fname) as f:
        dirs = f.readline().strip()
    
    width = 7
    fall_y = 4
    dir_idx = 0
    occupied = set([(x,0) for x in range(7)])

    # store the highest point for each x in our grid
    max_x = [0] * width

    to_match = {}
    matched_rounds, matched_heights = [], []
    remainder_rounds = float('inf') # this gets updated later
    ans = 0

    for round in range(rounds):

        # arbitrarily try to match round 500
        if round == 500:
            max_height = max(max_x)
            to_match = {(x,y - max_height) for x,y in occupied if y > max_height - 20}

        if round > 500:
            max_height = max(max_x)
            attempt = {(x,y - max_height) for x,y in occupied if y > max_height - 20}

            if to_match == attempt:

                # matched rounds are the round numbers that match the block pattern in round 500
                # (e.g. for the test, matched rounds looks like [535, 570 ... 500 + 35n])
                matched_rounds.append(round)

                # matched heights are the max y values (grid heights) corresponding to each matched rounds
                matched_heights.append(max_height)

                if len(matched_heights) > 1:
                    # the pattern repeats every (matched_rounds[1] - matched_rounds[0]) rounds
                    # we reach 1000000000000 in round = 1000000000000 - curr_round % (matched_rounds[1] - matched_rounds[0])
                    # i.e., how many rounds remaining after out completed cycle (1 cycle = # rounds it takes to revisit the pattern)
                    # (slightly messy since round and matched_rounds[1] are the same thing, but whatever)
                    
                    rounds_in_pattern = matched_rounds[1] - matched_rounds[0]
                    remainder_rounds = (rounds - round) % rounds_in_pattern
                    cycles_left = (rounds - round) // rounds_in_pattern

                    # points after all cycles (without remainder_rounds) is the total points now
                    # plus (remaining cycles * points per cycle)
                    points_per_cycle = matched_heights[1] - matched_heights[0]
                    ans = points_per_cycle * cycles_left


        falling = True
        piece_idx = round % 5
        coords = get_coords(piece_idx, fall_y)

        while falling:
            # first move laterally
            dir = dirs[dir_idx % len(dirs)]

            # move left if leftmost x > 0
            if dir == '<' and coords[0][0] > 0:
                new_coords = [(x-1, y) for x,y in coords]
                if not set(new_coords).intersection(occupied):
                    coords = new_coords
            
            # move right if rightmost x < width
            elif dir == '>' and coords[-1][0] < width-1:
                new_coords = [(x+1, y) for x,y in coords]
                if not set(new_coords).intersection(occupied):
                    coords = new_coords
            
            dir_idx += 1

            # check if falls or at rest
            for c in coords:
                x,y = c
        
                # piece is one above so it stops falling
                if (x, y - 1) in occupied:
                    # update max_x
                    for x,y in coords:
                        if y > max_x[x]:
                            max_x[x] = y
                        occupied.add((x,y))
                    
                    # update global max y
                    fall_y = max(max_x) + 4

                    falling = False
                    break
            
            if falling:
                # piece didn't hit anything so we decrease y_coords by 1
                coords = [(x, y-1) for x,y in coords]
        
        remainder_rounds -= 1
        if remainder_rounds == 0:
            return ans + max(max_x)
        
    return max(max_x)

# print(tetris2('input/test.txt', 1000000000000))
print(tetris2('input/17.txt', 1000000000000))