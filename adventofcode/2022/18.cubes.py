def inside_space(xyz, mins, maxs):
    x,y,z = xyz
    xmin, ymin, zmin = mins
    xmax, ymax, zmax = maxs

    if xmin <= x <= xmax and ymin <= y <= ymax and zmin <= z <= zmax:
        return True
    return False

def cube_sa(fname, part2=False):
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]
    
    # first get all cubes as a set
    cubes = set()
    for l in lines:
        x,y,z = eval(l)
        cubes.add((x,y,z))
    
    # part1
    if not part2:
        all_nbrs = 0
        for l in lines:
            x,y,z = eval(l)
            nbrs = [(x-1, y, z), (x+1, y, z), (x,y-1,z), (x,y+1,z), (x,y,z-1), (x,y,z+1)]
            for n in nbrs:
                if n not in cubes:
                    all_nbrs += 1
        
        return all_nbrs

    # part 2

    # need to get all cubes inside area
    # first get the outside area by depth-first-search from a corner of the bounding cube
    # then we'll reverse the outside area to get essentially a solid (non-porous) object

    # also add a point of buffer for the cubes on the edges
    xmin, xmax = min(cubes, key=lambda x:x[0])[0]-1, max(cubes, key=lambda x:x[0])[0]+1
    ymin, ymax = min(cubes, key=lambda x:x[1])[1]-1, max(cubes, key=lambda x:x[1])[1]+1
    zmin, zmax = min(cubes, key=lambda x:x[2])[2]-1, max(cubes, key=lambda x:x[2])[2]+1

    mins = (xmin, ymin, zmin)
    maxs = (xmax, ymax, zmax)

    paths, new_paths = [(xmin, ymin, zmin)], []
    externals = set()

    while len(paths) > 0:
        for p in paths:
            x,y,z = p
            for poss_path in [(x-1, y, z), (x+1, y, z), (x,y-1,z), (x,y+1,z), (x,y,z-1), (x,y,z+1)]:
                if inside_space(poss_path, mins, maxs) and poss_path not in externals and poss_path not in cubes:
                    externals.add(poss_path)
                    new_paths.append(poss_path)
                    
        paths = new_paths
        new_paths = []
    
    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            for z in range(zmin, zmax+1):
                if (x,y,z) not in externals:
                    cubes.add((x,y,z))


    all_nbrs = 0
    for l in lines:
        x,y,z = eval(l)
        nbrs = [(x-1, y, z), (x+1, y, z), (x,y-1,z), (x,y+1,z), (x,y,z-1), (x,y,z+1)]
        for n in nbrs:
            if n not in cubes:
                all_nbrs += 1
    
    return all_nbrs

# print(cube_sa('input/test.txt', part2=True))
print(cube_sa('input/18.txt'))
# print(cube_sa('input/test.txt', part2=True))
print(cube_sa('input/18.txt', part2=True))
