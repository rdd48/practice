def update_round(curr, next_pos, proposals, not_moving, proposals_to_del):
    if next_pos not in proposals:
        proposals[next_pos] = curr
    else:
        not_moving.add(curr)
        not_moving.add(proposals[next_pos])
        proposals_to_del.add(next_pos)
    return proposals, not_moving, proposals_to_del

def elf_dance(fname, part2=False):
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        elves = set()
        for yidx, y in enumerate(lines[::-1]): # go backwards so that starting y pos is 0
            for xidx, x in enumerate(y):
                if x == '#':
                    elves.add((xidx, yidx))
        
    for r in range(10000000000):

        # proposals will be a dict of proposed pos keys and current pos values
        proposals = {}
        proposals_to_del = set()
        not_moving = set()

        for x,y in elves:
            # check all other pos
            nw = True if (x-1,y+1) not in elves else False
            n = True if (x,y+1) not in elves else False
            ne = True if (x+1,y+1) not in elves else False
            e = True if (x+1,y) not in elves else False
            se = True if (x+1,y-1) not in elves else False
            s = True if (x,y-1) not in elves else False
            sw = True if (x-1,y-1) not in elves else False
            w = True if (x-1,y) not in elves else False

            # don't do anything
            if nw and n and ne and e and se and s and sw and w:
                not_moving.add((x,y))

            elif r % 4 == 0:
                if nw and n and ne:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x,y+1), proposals, not_moving, proposals_to_del)
                elif se and s and sw:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x,y-1), proposals, not_moving, proposals_to_del)
                elif nw and w and sw:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x-1,y), proposals, not_moving, proposals_to_del)
                elif ne and e and se:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x+1,y), proposals, not_moving, proposals_to_del)
                else:
                    not_moving.add((x,y))
            elif r % 4 == 1:
                if se and s and sw:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x,y-1), proposals, not_moving, proposals_to_del)
                elif nw and w and sw:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x-1,y), proposals, not_moving, proposals_to_del)
                elif ne and e and se:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x+1,y), proposals, not_moving, proposals_to_del)
                elif nw and n and ne:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x,y+1), proposals, not_moving, proposals_to_del)
                else:
                    not_moving.add((x,y))
            elif r % 4 == 2:
                if nw and w and sw:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x-1,y), proposals, not_moving, proposals_to_del)
                elif ne and e and se:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x+1,y), proposals, not_moving, proposals_to_del)
                elif nw and n and ne:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x,y+1), proposals, not_moving, proposals_to_del)
                elif se and s and sw:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x,y-1), proposals, not_moving, proposals_to_del)
                else:
                    not_moving.add((x,y))
            elif r % 4 == 3:
                if ne and e and se:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x+1,y), proposals, not_moving, proposals_to_del)
                elif nw and n and ne:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x,y+1), proposals, not_moving, proposals_to_del)
                elif se and s and sw:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x,y-1), proposals, not_moving, proposals_to_del)
                elif nw and w and sw:
                    proposals, not_moving, proposals_to_del = update_round((x,y), (x-1,y), proposals, not_moving, proposals_to_del)
                else:
                    not_moving.add((x,y))
        
        if part2 and not_moving == elves:
            return r + 1
        
        elves_new = not_moving.copy()
        for p in proposals.keys():
            if p not in proposals_to_del:
                elves_new.add(p)
        
        elves = elves_new.copy()

        if not part2 and r == 9:
            xmin, xmax = min(elves, key=lambda x:x[0])[0], max(elves, key=lambda x:x[0])[0]
            ymin, ymax = min(elves, key=lambda x:x[1])[1], max(elves, key=lambda x:x[1])[1]

            ans = 0
            for y in range(ymin, ymax+1):
                for x in range(xmin, xmax+1):
                    if (x,y) not in elves:
                        ans += 1

            return ans

# print(elf_dance('input/test.txt'))
print(elf_dance('input/23.txt'))

# print(elf_dance('input/test.txt', part2=True))
print(elf_dance('input/23.txt', part2=True))
    