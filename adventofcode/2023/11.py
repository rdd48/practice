def check_cols(cidx, rows):
    for r in rows:
        if r[cidx] == '#':
            return False
    return True

def man_dist(t1, t2):
    x1,y1 = t1
    x2,y2 = t2
    return abs((x2-x1))+abs((y2-y1))

def main(fname, add_num):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    
    row_adds = {}
    curr_adds = 0
    for ridx, r in enumerate(lines):
        if '#' not in r:
            curr_adds += (add_num-1)
        row_adds[ridx] = ridx + curr_adds
    
    col_adds = {}
    curr_adds = 0
    for cidx in range(len(lines[0])):
        if check_cols(cidx, lines):
            curr_adds += (add_num-1)
        col_adds[cidx] = cidx + curr_adds
    
    # get all universes as a list of (ridx, cidx) tuples
    unis = []
    for ridx, r in enumerate(lines):
        for cidx, c in enumerate(r):
            if c == '#':
                row_add = row_adds[ridx]
                col_add = col_adds[cidx]
                unis.append((row_add, col_add))
    
    ans = 0
    for uidx, u in enumerate(unis[:-1]):
        for u2 in unis[uidx+1:]:
            # if u == (6,1) and u2 == (11,5):
            #     print(man_dist(u,u2))
            ans += man_dist(u, u2)

    return ans

print(main('input/11.txt', 2))
print(main('input/11.txt', 1000000))
