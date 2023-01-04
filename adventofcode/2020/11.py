def adj_seats(t, rows, cols):
    adj_seats = set()
    r, c = t

    # seats to left
    if c > 0:
        adj_seats.add((r, c-1))
        if r > 0:
            adj_seats.add((r-1, c-1))
        if r < rows-1:
            adj_seats.add((r+1, c-1))
    
    # seats to right
    if c < cols -1:
        adj_seats.add((r, c+1))
        if r > 0:
            adj_seats.add((r-1, c+1))
        if r < rows-1:
            adj_seats.add((r+1, c+1))

    # above and below
    if r > 0:
        adj_seats.add((r-1, c))
    if r < rows-1:
        adj_seats.add((r+1, c))

    return adj_seats

def occupy_seat(adj, occ): 
    if not len(adj.intersection(occ)):
        return True
    return False

def empty_seat(adj, occ, val):
    if len(adj.intersection(occ)) >= val:
        return True
    return False

with open('input/11.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    # store floor, empty, and occupied as sets of (row, col) tuples
    floor, empty, occ = set(), set(), set()

    for ridx, row in enumerate(lines):
        for cidx, val in enumerate(row):
            if val == '.':
                floor.add((ridx, cidx))
            elif val == 'L':
                empty.add((ridx, cidx))
    
    rows, cols = len(lines), len(lines[0])

# part one
moved = True
round = 0

while moved:
    moved = False
    round += 1
    new_occ, new_empty = set(), set()

    for seat in empty:
        adj = adj_seats(seat, rows, cols)
        if occupy_seat(adj, occ):
            new_occ.add(seat)
            moved = True
        else:
            new_empty.add(seat)
    
    for seat in occ:
        adj = adj_seats(seat, rows, cols)
        if empty_seat(adj, occ, 4):
            new_empty.add(seat)
            moved = True
        else:
            new_occ.add(seat)
    
    occ, empty = new_occ, new_empty

print('part one: ', len(occ))

# part two
def get_seat_recur(t, dr, dc, rows, cols, occ, empty):
    r, c = t
    if r < 0 or r > rows-1 or c < 0 or c > cols-1:
        return False
    elif (r,c) in occ or (r,c) in empty:
        return (r,c)
    return get_seat_recur((r+dr, c+dc), dr, dc, rows, cols, occ, empty)

def adj_seats2(t, rows, cols, occ, empty):
    adj_seats = set()
    r, c = t

    # seats to left
    if (new := get_seat_recur((r,c-1), 0, -1, rows, cols, occ, empty)):
        adj_seats.add(new)
    if (new := get_seat_recur((r-1,c-1), -1, -1, rows, cols, occ, empty)):
        adj_seats.add(new)
    if (new := get_seat_recur((r+1,c-1), 1, -1, rows, cols, occ, empty)):
        adj_seats.add(new)
    
    # seats to right
    if (new := get_seat_recur((r,c+1), 0, 1, rows, cols, occ, empty)):
        adj_seats.add(new)
    if (new := get_seat_recur((r-1,c+1), -1, 1, rows, cols, occ, empty)):
        adj_seats.add(new)
    if (new := get_seat_recur((r+1,c+1), 1, 1, rows, cols, occ, empty)):
        adj_seats.add(new)

    if (new := get_seat_recur((r-1,c), -1, 0, rows, cols, occ, empty)):
        adj_seats.add(new)
    if (new := get_seat_recur((r+1,c), 1, 0, rows, cols, occ, empty)):
        adj_seats.add(new)

    return adj_seats

with open('input/11.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    # store floor, empty, and occupied as sets of (row, col) tuples
    floor, empty, occ = set(), set(), set()

    for ridx, row in enumerate(lines):
        for cidx, val in enumerate(row):
            if val == '.':
                floor.add((ridx, cidx))
            elif val == 'L':
                empty.add((ridx, cidx))
    
    rows, cols = len(lines), len(lines[0])
    
moved = True
round = 0

# # display grid if wanted for debugging
# import numpy as np
# def display_grid(occ, empty, floor, rows, cols):
#     a = np.chararray((rows, cols))
#     for r,c in occ:
#         a[r,c] = '#'
#     for r,c in empty:
#         a[r,c] = 'L'
#     for r,c in floor:
#         a[r,c] = '.'
#     for r in a:
#         print(''.join([str(i).replace('b','').replace("'","") for i in r.tolist()]))
#     print('')

while moved:
    moved = False
    round += 1
    new_occ, new_empty = set(), set()

    # print(round)
    # display_grid(occ, empty, floor, rows, cols)

    for seat in empty:
        adj = adj_seats2(seat, rows, cols, occ, empty)
        if occupy_seat(adj, occ):
            new_occ.add(seat)
            moved = True
        else:
            new_empty.add(seat)
    
    for seat in occ:
        adj = adj_seats2(seat, rows, cols, occ, empty)
        if empty_seat(adj, occ, 5):
            new_empty.add(seat)
            moved = True
        else:
            new_occ.add(seat)
    
    occ, empty = new_occ, new_empty
    

print('part two: ', len(occ))