import numpy as np

def build_grid(fname):
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        all_instruct = []
        min_x, max_x, max_y = 1000000, 0, 0
        
        for l in lines:
            instruct = []
            lsplit = l.split(' -> ')
            for ls in lsplit:
                x, y = ls.split(',')
                x, y = int(x), int(y)
                instruct.append((x, y))
                
                min_x = x if x < min_x else min_x
                max_x = x if x > max_x else max_x
                max_y = y if y > max_y else max_y
            
            all_instruct.append(instruct)
    
    a = np.zeros((max_y+1, max_x-min_x+1), dtype='int')

    for i in all_instruct:
        for idx, i1 in enumerate(i[:-1]):
            
            i2 = i[idx+1]
            x, y = i1
            x2, y2 = i2

            x -= min_x
            x2 -= min_x

            # draw horizontal
            if x != x2:
                direct = 1 if x < x2 else -1
                while x != x2:
                    a[y,x] = 1 # backwards-seeming because np is row, col
                    x += direct

            # draw vertical
            elif y != y2:
                direct = 1 if y < y2 else -1
                while y != y2:
                    a[y,x] = 1
                    y += direct
        
        # draw last part
        a[y,x] = 1

    # drop sand
    sx, sy = 500-min_x, 0
    units = 0

    while True:
        
        # will fall outside map
        if sy == max_y:

            # return a
            return units

        # nothing is below
        if not a[sy+1, sx]:
            sy += 1
        
        # something is below
        # move diag to the left
        
        elif not a[sy+1, sx-1]:
            sy += 1
            sx -= 1
        
        # move diag to the right
        elif not a[sy+1, sx+1]:
            sy += 1
            sx += 1
        
        else:
            a[sy,sx] = 1
            sx, sy = 500-min_x, 0
            units += 1
        

print(build_grid('input/test.txt'))
print(build_grid('input/14.txt'))

def build_grid2(fname):
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        all_instruct = []
        min_x, max_x, max_y = 1000000, 0, 0
        
        for l in lines:
            instruct = []
            lsplit = l.split(' -> ')
            for ls in lsplit:
                x, y = ls.split(',')
                x, y = int(x), int(y)
                instruct.append((x, y))
                
                min_x = x if x < min_x else min_x
                max_x = x if x > max_x else max_x
                max_y = y if y > max_y else max_y
            
            all_instruct.append(instruct)
    
    a = np.zeros((max_y+3, max_x-min_x+1), dtype='int')
    for x in range(max_x-min_x+1):
        a[max_y+2, x] = 1

    
    

    for i in all_instruct:
        for idx, i1 in enumerate(i[:-1]):
            
            i2 = i[idx+1]
            x, y = i1
            x2, y2 = i2

            x -= min_x
            x2 -= min_x

            # draw horizontal
            if x != x2:
                direct = 1 if x < x2 else -1
                while x != x2:
                    a[y,x] = 1 # backwards-seeming because np is row, col
                    x += direct

            # draw vertical
            elif y != y2:
                direct = 1 if y < y2 else -1
                while y != y2:
                    a[y,x] = 1
                    y += direct
        
        # draw last part
        a[y,x] = 1
    
    row, col = a.shape

    for r in range(row):
        lista = [str(i) for i in a[r].tolist()]
        print(''.join(lista))
    exit()

    # drop sand
    sx, sy = 500-min_x, 0
    units = 0

    while True:
        
        # will fall outside map
        if sy == max_y:

            # return a
            return units

        # nothing is below
        if not a[sy+1, sx]:
            sy += 1
        
        # something is below
        # move diag to the left
        
        elif not a[sy+1, sx-1]:
            sy += 1
            sx -= 1
        
        # move diag to the right
        elif not a[sy+1, sx+1]:
            sy += 1
            sx += 1
        
        else:
            a[sy,sx] = 1
            sx, sy = 500-min_x, 0
            units += 1
        

print(build_grid2('input/test.txt'))
print(build_grid2('input/14.txt'))