def process_input(filename):
    with open(filename) as f:
        line = f.readlines()[0]
        x_pos, y_pos = line.split(' ')[-2], line.split(' ')[-1]

        x_pos = x_pos.replace('x=', '').replace(',', '')
        x_min, x_max = int(x_pos.split('..')[0]), int(x_pos.split('..')[1])

        y_pos = y_pos.replace('y=', '').replace(',', '')
        y_min, y_max = int(y_pos.split('..')[0]), int(y_pos.split('..')[1])

        return x_min, x_max, y_min, y_max

def launch(x_vel, y_vel, x_min, x_max, y_min, y_max):
    x, y = 0, 0
    max_height = 0
    while x < x_max and y > y_min:
        x += x_vel
        y += y_vel

        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1
        y_vel -= 1

        if y > max_height:
            max_height = y

        if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
            return max_height
        
    return None

def factorial(x):
    if x in [0, 1]:
        return x
    else:
        return x + factorial(x-1)

def inverse_factorial(x):
    i, num = 0, 1
    while i < x:
        num += 1
        i = factorial(num)
    return num


def main(filename, part_two=False):
    x_min, x_max, y_min, y_max = process_input(filename)

    max_height = 0
    total = []

    # brute force
    # but i did realize that there's no use testing x values < "inverse factoral" of target's x_min
    # since e.g. if the target x_min is 10, then:
    # x = 1: stops increasing x @ 1, x = 2 => 4, x = 3 => 6, until x = 4
    # the y range... not sure why this works but i was playing with values until something seemed reasonable
    for x in range(inverse_factorial(x_min), x_max+1):
        for y in range(-abs(y_min), abs(y_min)+1):
            ans = launch(x, y, x_min, x_max, y_min, y_max)
            if ans is not None:
                total.append((x,y))
                if ans > max_height:
                    max_height = ans
    
    if not part_two:
        return max_height
    else:
        return len(total)

# part one
# print(main('input/test.txt'))
print(main('input/17_launch.txt'))

# part two
# print(main('input/test.txt', part_two=True))
print(main('input/17_launch.txt', part_two=True))