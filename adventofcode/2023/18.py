def main(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    
    dirs = []
    for l in lines:
        splitl = l.split()
        dirs.append((splitl[0], int(splitl[1])))
    
    # (x, y)
    pos = (0,0)
    trenches = {(0,0)}
    for d, dunit in dirs:
        if d == 'L':
            for _ in range(dunit):
                pos = (pos[0]-1, pos[1])
                trenches.add(pos)
        elif d == 'R':
            for _ in range(dunit):
                pos = (pos[0]+1, pos[1])
                trenches.add(pos)
        elif d == 'D':
            for _ in range(dunit):
                pos = (pos[0], pos[1]-1)
                trenches.add(pos)
        elif d == 'U':
            for _ in range(dunit):
                pos = (pos[0], pos[1]+1)
                trenches.add(pos)
    
    # return sorted(list(trenches))
    
    # how do i get a starting point? hard-coding it in for now
    trenches.add((1,-1))
    curr_pos = {(1,-1)}
    new_pos = set()

    while True:
        for x,y in curr_pos:
            new_squares = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
            for nx, ny in new_squares:
                if (nx, ny) not in trenches:
                    trenches.add((nx, ny))
                    new_pos.add((nx,ny))

        if not len(new_pos):
            return len(trenches)
        
        curr_pos = new_pos.copy()
        new_pos = set()

def shoelace(tiles):
    fwd = 0
    rev = 0
    for idx, val in enumerate(tiles):
        curr_x, curr_y = val
        next_x, next_y = tiles[(idx+1) % len(tiles)]
        fwd += (curr_x * next_y)
        rev += (curr_y * next_x)
    return 0.5 * abs(fwd - rev)

def main2(fname):
    with open(fname) as f:
        lines = f.readlines()
        # hexcodes = [l.strip().split()[-1] for l in f.readlines() if l.strip()]

    trenches = []
    pos = (0,0)
    dist_convert = {'0':'R', '1':'D', '2':'L', '3':'U'}
    outer_area = 0

    for l in lines:
        hc = l.strip().split()[-1]
        d = dist_convert[hc[-2]]
        dist = int(hc[2:7], 16)

        outer_area += dist

        if d == 'L':
            pos = (pos[0]-dist, pos[1])
            
        elif d == 'R':
            pos = (pos[0]+dist, pos[1])
            
        elif d == 'D':
            pos = (pos[0], pos[1]-dist)
            
        elif d == 'U':
            pos = (pos[0], pos[1]+dist)
            
        trenches.append(pos)
        
    shoe_area = shoelace(trenches)
    total = shoe_area - (0.5 * outer_area) + 1
    return int(total + outer_area)
    
print(main('input/18.txt'))
print(main2('input/18.txt'))