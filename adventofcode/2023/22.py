# slowwwwww

def check_support(same_level, ub):
    ux,uy,_ = ub
    for sb in same_level:
        sx,sy,_ = sb
        for x in sx:
            for y in sy:
                if x in ux and y in uy:
                    return True
    return False
        
def check_disintegrate(same_level, upper_level):
    if not upper_level:
        return 1

    for ub in upper_level:
        # if any upper brick is unsupported, return 0
        if not check_support(same_level, ub):
            return 0
    return 1

def main(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    
    # how to store bricks?
    # maybe as lists of lists, each inner list is a brick
    # each inner brick has (x1,x2), (y1,y2), (z1,z2) tuples where 1<=2 always

    bricks = []
    for l in lines:
        start,end = l.split('~')
        x1, y1, z1 = [int(i) for i in start.split(',')]
        x2, y2, z2 = [int(i) for i in end.split(',')]
        bricks.append([
            tuple(range(min(x1, x2), max(x1,x2)+1)),
            tuple(range(min(y1, y2), max(y1,y2)+1)),
            tuple(range(min(z1, z2), max(z1,z2)+1)),
        ])
    
    # now sort by z1
    bricks.sort(key=lambda x:x[2][-1], reverse=False)

    # make all bricks fall and store in new list of lists
    fallen = []
    for b in bricks:
        # bx1,bx2,by1,by2,bz1,bz2 = unpack_brick(b)
        bx, by, bz = b
        add_brick = True
        
        if bz[0] == 1:
            fallen.append(b)
        else:
            for fb in fallen:
                # fx1,fx2,fy1,fy2,fz1,fz2 = unpack_brick(fb)
                fx, fy, fz = fb
                if fz[-1] < bz[0]:
                    # check if x or y overlaps
                    if len(set(fx).intersection(set(bx))) and len(set(fy).intersection(set(by))):
                        z_dist = bz[0] - fz[-1]
                        bz = tuple(map(lambda x:x-z_dist+1, bz))
                        fallen.append([bx, by, bz])
                        add_brick = False
                        break
            
            # here we never hit another brick, so set the z1 to 1
            if add_brick:
                z_dist = bz[0] - 1
                bz = tuple(map(lambda x:x-z_dist, bz))
                fallen.append([bx, by, bz])
        
        fallen.sort(key=lambda x:x[2][-1], reverse=True)
    
    total = 0
    for b in fallen:
        # need everything on the same top level, i.e. current z2
        # also need everything on next level up, i.e. their z1 = current z2 + 1
        bz2 = b[2][-1]
        same_level = list(filter(lambda x:x[2][-1]==bz2, fallen))
        same_level.remove(b)
        upper_level = list(filter(lambda x:x[2][0]==bz2+1, fallen))
        total += check_disintegrate(same_level, upper_level)
    
    return total

def get_upper_bricks_dis(b, fallen):
    bz2 = b[2][-1]
    same_level = list(filter(lambda x:x[2][-1]==bz2, fallen))
    same_level.remove(b)
    upper_level = list(filter(lambda x:x[2][0]==bz2+1, fallen))

    if not upper_level:
        return []
    
    dis_fallen = []
    
    for ub in upper_level:
        if not check_support(same_level, ub):
            dis_fallen.append(ub)
    return dis_fallen

def update_fallen(dis_fallen, fallen, b):
    if not dis_fallen:
        return fallen
    fallen.remove(b)
    for df in dis_fallen:
        fallen.remove(df)
        bx, by, bz = df
        add_brick = True
        
        if bz[0] == 1:
            fallen.append(b)
        else:
            for fb in fallen:
                # fx1,fx2,fy1,fy2,fz1,fz2 = unpack_brick(fb)
                fx, fy, fz = fb
                if fz[-1] < bz[0]:
                    # check if x or y overlaps
                    if len(set(fx).intersection(set(bx))) and len(set(fy).intersection(set(by))):
                        z_dist = bz[0] - fz[-1]
                        bz = tuple(map(lambda x:x-z_dist+1, bz))
                        fallen.append([bx, by, bz])
                        add_brick = False
                        break
            
            # here we never hit another brick, so set the z1 to 1
            if add_brick:
                z_dist = bz[0] - 1
                bz = tuple(map(lambda x:x-z_dist, bz))
                fallen.append([bx, by, bz])
        
        fallen.sort(key=lambda x:x[2][-1], reverse=True)
    
    return fallen

def fall_bricks(bricks):
    # now sort by z1
    bricks.sort(key=lambda x:x[2][-1], reverse=False)

    # make all bricks fall and store in new list of lists
    fallen = []
    moved_bricks = 0
    for b in bricks:
        # bx1,bx2,by1,by2,bz1,bz2 = unpack_brick(b)
        bx, by, bz = b
        add_brick = True
        
        if bz[0] == 1:
            fallen.append(b)
        else:
            for fb in fallen:
                # fx1,fx2,fy1,fy2,fz1,fz2 = unpack_brick(fb)
                fx, fy, fz = fb
                if fz[-1] < bz[0]:
                    # check if x or y overlaps
                    if len(set(fx).intersection(set(bx))) and len(set(fy).intersection(set(by))):
                        z_dist = bz[0] - fz[-1]
                        if z_dist > 1:
                            moved_bricks += 1
                        bz = tuple(map(lambda x:x-z_dist+1, bz))
                        fallen.append([bx, by, bz])
                        add_brick = False
                        break
            
            # here we never hit another brick, so set the z1 to 1
            if add_brick:
                z_dist = bz[0] - 1
                if z_dist > 0:
                    moved_bricks += 1
                bz = tuple(map(lambda x:x-z_dist, bz))
                fallen.append([bx, by, bz])
        
        fallen.sort(key=lambda x:x[2][-1], reverse=True)

    return fallen, moved_bricks

def main2(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    
    # how to store bricks?
    # maybe as lists of lists, each inner list is a brick
    # each inner brick has (x1,x2), (y1,y2), (z1,z2) tuples where 1<=2 always

    bricks = []
    for l in lines:
        start,end = l.split('~')
        x1, y1, z1 = [int(i) for i in start.split(',')]
        x2, y2, z2 = [int(i) for i in end.split(',')]
        bricks.append([
            tuple(range(min(x1, x2), max(x1,x2)+1)),
            tuple(range(min(y1, y2), max(y1,y2)+1)),
            tuple(range(min(z1, z2), max(z1,z2)+1)),
        ])
    
    fallen, _ = fall_bricks(bricks)

    fallen_bricks = 0
    for idx, b in enumerate(fallen):
        bricks_remove = fallen.copy()
        bricks_remove.remove(b)
        _, num_fallen = fall_bricks(bricks_remove)
        fallen_bricks += num_fallen
        

    return fallen_bricks


print(main2('input/test.txt'))
print(main2('input/22.txt'))

