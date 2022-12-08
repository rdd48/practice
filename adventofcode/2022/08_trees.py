import numpy as np

def visible_trees(fname):
    with open(fname) as f:
        lines = f.readlines()
        rows = len(lines)
        cols = len(lines[0].strip())
        a = np.zeros((rows, cols))

        # create array
        for row, l in enumerate(lines):
            for col, value in enumerate(l.strip()):
                a[row][col] = int(value)
    
    # count edges of grid first
    visible = (2 * rows) + (2 * cols) - 4

    # count inner trees
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            val = a[r][c]
            
            # check right
            # i.e., no value to the right is larger
            if np.sum(a[r][c+1:] >= val) == 0:
                visible += 1

            # check left
            elif np.sum(a[r][:c] >= val) == 0:
                visible += 1
            
            # check top
            elif np.sum(a[:r, c] >= val) == 0:
                visible += 1
            
            # check bottom
            elif np.sum(a[r+1:, c] >= val) == 0:
                visible += 1

    return visible

def visible_trees2(fname):
    with open(fname) as f:
        lines = f.readlines()
        rows = len(lines)
        cols = len(lines[0].strip())
        a = np.zeros((rows, cols))

        # create array
        for row, l in enumerate(lines):
            for col, value in enumerate(l.strip()):
                a[row][col] = int(value)

    best_view = 0

    # still don't need to check edges pretty sure
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            val = a[r][c]
            
            # check up
            up, new_r = 0, r - 1
            while new_r >= 0:
                up += 1
                if a[new_r][c] >= val:
                    break
                new_r -= 1
            
            # check down
            down, new_r = 0, r + 1
            while new_r <= rows - 1:
                down += 1
                if a[new_r][c] >= val:
                    break
                new_r += 1
            
            # check left
            left, new_c = 0, c - 1
            while new_c >= 0:
                left += 1
                if a[r][new_c] >= val:
                    break
                new_c -= 1
            
            # check right
            right, new_c = 0, c + 1
            while new_c <= cols - 1:
                right += 1
                if a[r][new_c] >= val:
                    break
                new_c += 1

            curr = up * down * left * right
            if curr > best_view:
                best_view = curr
    
    return best_view


# print(visible_trees('input/test.txt'))
print(visible_trees('input/08.txt'))

# print(visible_trees2('input/test.txt'))
print(visible_trees2('input/08.txt'))