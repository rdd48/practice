def map_seed(s, m):
    for dest, source, r in m:
        if s >= source and s < source + r:
            return dest + abs(s - source)
    return s

def part1(fname):

    # these are sets, i guess? of (source, dest, r)
    all_maps = [set(), set(), set(), set(), set(), set(), set()]
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        seeds = [int(i) for i in lines[0].split()[1:]]

        curr_idx = 0
        for l in lines[2:]:
            if l[0] not in '0123456789':
                curr_idx += 1
            else:
                list_copy = all_maps[curr_idx].copy()
                dest, source, r = [int(i) for i in l.split()]
                list_copy.add((dest, source, r))
                all_maps[curr_idx] = list_copy
    
    min_seed = max(seeds)
    out_debug = []
    for s in seeds:
        for m in all_maps:
            s = map_seed(s, m)
            
        out_debug.append(s)
        if s <= min_seed:
            min_seed = s
    
    return min_seed

def check_s_in_ranges(s, seed_pairs):
    for p0, p1 in seed_pairs:
        if s >= p0 and s < (p0 + p1):
            return True
    return False

def part2(fname):
    # kinda brute force, can't believe this works

    # the idea: get within 100000 first. then search all -/+ 100000 values, assuming they're possible.

    all_maps = [set(), set(), set(), set(), set(), set(), set()]
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        seeds = [int(i) for i in lines[0].split()[1:]]
        seed_pairs = []
        for idx in range(len(seeds)):
            if idx % 2 == 1:
                p0, p1 = seeds[idx-1], seeds[idx]
                seed_pairs.append((p0, p1))

        curr_idx = 0
        for l in lines[2:]:
            if l[0] not in '0123456789':
                curr_idx += 1
            else:
                list_copy = all_maps[curr_idx].copy()
                dest, source, r = [int(i) for i in l.split()]
                list_copy.add((dest, source, r))
                all_maps[curr_idx] = list_copy
    
    min_seed = max(seeds)

    # so here we just get close. gets w/i 100000
    for p0, p1 in seed_pairs:

        # for s in range(p0, p0+p1):
        for s in range(p0, p0+p1, 100000):
            start_s = s
            for m in all_maps:
                s = map_seed(s, m)
            
            if s <= min_seed:
                min_seed = s
                best_start_s = start_s
    
    # here we refine between -/+ 100000
    for s in range(best_start_s-100000, best_start_s+100000, 1):
        if check_s_in_ranges(s, seed_pairs):
            for m in all_maps:
                s = map_seed(s, m)
            
            if s <= min_seed:
                min_seed = s
                best_start_s = start_s

    return min_seed
            

print(part1('input/5.txt'))
print(part2('input/5.txt'))