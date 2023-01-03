def get_row(s):
    l,r = 0, 127
    for char in s:
        if char == 'F':
            r = (l+r)//2
        elif char == 'B':
            l = (l+r)//2
            l += 1
    return l

def get_col(s):
    l,r = 0, 7
    for char in s:
        if char == 'L':
            r = (l+r)//2
        elif char == 'R':
            l = (l+r)//2
            l += 1
    return l

with open('input/05.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    max_id = 0
    all_ids = set()

    for line in lines:
        row = get_row(line[:7])
        col = get_col(line[-3:])

        # part one
        if (seat_id := (row * 8) + col) > max_id:
            max_id = seat_id
        
        # part two
        all_ids.add(seat_id)

print('part one: ', max_id)

for r in range(128):
    for c in range(8):
        curr_id = (r * 8) + c
        if curr_id not in all_ids:
            if curr_id - 1 in all_ids and curr_id + 1 in all_ids:
                print('part two: ', curr_id)
                exit()
