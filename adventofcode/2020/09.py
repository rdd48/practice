def check_pream(pream, target):
    for val in pream:
        if abs(target - val) in pream:
            return True
    return False

with open('input/09.txt') as f:
    lines = f.readlines()
    lines = [int(l.strip()) for l in lines]

    preamble_val = 25
    for idx, target in enumerate(lines[preamble_val:]):
        pream = set(lines[idx:idx+preamble_val])
        if not check_pream(pream, target):
            print(target)
            break
    
    for idx, val in enumerate(lines):
        next_idx = idx
        curr_sum = val
        curr_min, curr_max = val, val
        while next_idx > 0 and curr_sum <= target:
            next_idx -= 1
            curr_sum += lines[next_idx]
            if lines[next_idx] < curr_min:
                curr_min = lines[next_idx]
            elif lines[next_idx] > curr_max:
                curr_max = lines[next_idx]
            if curr_sum == target:
                print(curr_min + curr_max)
                break
                
            
        
        