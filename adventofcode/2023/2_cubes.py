def check_game(sl):
    max_colors = {'red': 12, 'green': 13, 'blue': 14}
    colors = [c.replace(',', '').replace(';','') for c in sl[3::2]]
    for idx, i in enumerate(sl[2::2]):
        color = colors[idx]
        if int(i) > max_colors[color]:
            return False
    return True

def part1(fname):
    total = 0
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        for l in lines:
            sl = l.split()
            game_no = int(sl[1].replace(':', ''))
            if check_game(sl):
                total += game_no
    return total

def part2(fname):
    total = 0
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        for l in lines:
            sl = l.split()
            max_cubes = {'red': 0, 'green': 0, 'blue': 0}
            colors = [c.replace(',', '').replace(';','') for c in sl[3::2]]
            for idx, i in enumerate(sl[2::2]):
                color = colors[idx]
                if int(i) > max_cubes[color]:
                    max_cubes[color] = int(i)
            subtotal = 1
            for num in max_cubes.values():
                subtotal *= num
            total += subtotal
    return total


print(part1('input/2.txt'))
print(part2('input/2.txt'))