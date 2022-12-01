def increasing_from_depths(filename):
    total_inc = 0

    with open(filename) as f:
        lines = f.readlines()
        for idx, l in enumerate(lines):
            if idx < len(lines) - 1:
                if int(l) < int(lines[idx+1]):
                    total_inc += 1
    
    return total_inc

def sliding_window_depths(filename):
    total_inc = 0
    with open(filename) as f:
        lines = f.readlines()
        for idx, l in enumerate(lines):
            if idx < len(lines) - 3:
                sum1 = int(l) + int(lines[idx+1]) + int(lines[idx+2])
                sum2 = int(lines[idx+1]) + int(lines[idx+2]) + int(lines[idx+3])
                if sum1 < sum2:
                    total_inc += 1
    
    return total_inc


# print(increasing_from_depths('input/1_depths.txt'))
print(sliding_window_depths('input/1_depths.txt'))