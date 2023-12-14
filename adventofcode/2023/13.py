def get_sym_rows(ridx, gridlen):
    sym_rows = []
    for r in range(ridx):
        sym_r = (2*ridx) - r - 1
        if sym_r >= 0 and sym_r < gridlen:
            sym_rows.append((r, sym_r))
    return sym_rows

def check_all_h(axis, grid):
    sym_rows = get_sym_rows(axis, len(grid))
    for start, end in sym_rows:
        if grid[start] != grid[end]:
            return False
    return True

def check_horiz(grid):
    for axis in range(1,len(grid)):
        if check_all_h(axis, grid):
            return axis
    return False

def check_all_v(axis, grid):
    sym_col = get_sym_rows(axis, len(grid[0]))
    for start, end in sym_col:
        start_col = ''.join([i[start] for i in grid])
        end_col = ''.join([i[end] for i in grid])
        if start_col != end_col:
            return False
    return True

def check_vert(grid):
    for axis in range(1,len(grid[0])):
        if check_all_v(axis, grid):
            return axis
    return False

def check_horiz2(grid, orig_haxis):
    # axis needs to be incremented by one
    # need to update this to check all positions
    for axis in range(1,len(grid)):
        if axis != orig_haxis:
            if check_all_h(axis, grid):
                return axis
    return False

def check_vert2(grid, orig_vaxis):
    for axis in range(1,len(grid[0])):
        if axis != orig_vaxis:
            if check_all_v(axis, grid):
                return axis
    return False

def main(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines()]
        lines.append('')
    
    all_grids = []
    curr_grid = []
    for l in lines:
        if l:
            curr_grid.append(l)
        if not l and curr_grid:
            all_grids.append(curr_grid)
            curr_grid = []
    
    total = 0
    for grid in all_grids:
        if haxis := check_horiz(grid):
            total += (100 * haxis)
        
        elif vaxis := check_vert(grid):
            total += vaxis
    
    return total

def smudge_grid(grid):
    grids = []
    for ridx, r in enumerate(grid):
        for cidx, c in enumerate(r):
            temp = grid.copy()
            new_char = '.' if c == '#' else '#'
            temp[ridx] = r[:cidx] + new_char + r[cidx+1:]
            grids.append(temp)
    return grids

def main2(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines()]
        lines.append('')
    
    all_grids = []
    curr_grid = []
    for l in lines:
        if l:
            curr_grid.append(l)
        if not l and curr_grid:
            all_grids.append(curr_grid)
            curr_grid = []
    
    total = 0
    for grid in all_grids:
        orig_haxis = check_horiz(grid)
        orig_vaxis = check_vert(grid)

        for sg in smudge_grid(grid):

            if haxis := check_horiz2(sg, orig_haxis):
                total += (100 * haxis)
                break
            
            elif vaxis := check_vert2(sg, orig_vaxis):
                total += vaxis
                break
        
    return total


print(main('input/13.txt'))
print(main2('input/13.txt'))