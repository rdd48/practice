def depth_pos(filename):
    horizontal, depth = 0, 0
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            l_split = l.split()
            if l_split[0] == 'forward':
                horizontal += int(l_split[1].strip())
            elif l_split[0] == 'down':
                depth += int(l_split[1].strip())
            elif l_split[0] == 'up':
                depth -= int(l_split[1].strip())
    
    return horizontal * depth

def depth_pos_aim(filename):
    horizontal, depth, aim = 0, 0, 0
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            l_split = l.split()
            if l_split[0] == 'forward':
                horizontal += int(l_split[1].strip())
                depth += int(l_split[1].strip()) * aim
            elif l_split[0] == 'down':
                # depth += int(l_split[1].strip())
                aim += int(l_split[1].strip())
            elif l_split[0] == 'up':
                # depth -= int(l_split[1].strip())
                aim -= int(l_split[1].strip())
    
    print(horizontal, depth, horizontal*depth)
    return horizontal * depth

# print(depth_pos_aim('input/test.txt'))
print(depth_pos_aim('input/2_directions.txt'))