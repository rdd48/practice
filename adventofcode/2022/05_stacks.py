def parse_input(fname, test):
    with open(fname) as f:
        lines = f.readlines()

        # test input is 3 lines, puzzle input is 9
        stack_len = 3 if test else 9

        # test input is 3 lines, puzzle input is 8
        num_lines = 3 if test else 8

        # generate "container" for each "stack" (list of lists)
        container = [[] for _ in range(stack_len)]
        line_len = len(lines[0].replace('\n', ''))
        
        for l in reversed(lines[:num_lines]):
            # "crate" is every 4th character starting with 2nd char
            for char in range(1, line_len, 4):
                if l[char] != ' ':
                    new_row = int((char - 1) / 4)
                    row_copy = container[new_row].copy()
                    row_copy.append(l[char])
                    container[new_row] = row_copy

    return container

def move_crates1(fname, test):
    container = parse_input(fname, test)

    with open(fname) as f:
        lines = f.readlines()

        instr_start = 5 if test else 10
        for l in lines[instr_start:]:
            instr = l.strip().split()
            move_num, start_pos, end_pos = int(instr[1]), int(instr[3]), int(instr[5])

            start_row = container[start_pos-1].copy()
            end_row = container[end_pos-1].copy()
            for _ in range(move_num):
                moved = start_row.pop()
                end_row.append(moved)
            
            container[start_pos-1] = start_row
            container[end_pos-1] = end_row

    return ''.join(row[-1] for row in container)
    

# print(move_crates1('input/test.txt', test=True))
print(move_crates1('input/05.txt', test=False))
        
def move_crates2(fname, test):
    container = parse_input(fname, test)

    with open(fname) as f:
        lines = f.readlines()

        instr_start = 5 if test else 10
        for l in lines[instr_start:]:
            instr = l.strip().split()
            move_num, start_pos, end_pos = int(instr[1]), int(instr[3]), int(instr[5])

            start_row = container[start_pos-1].copy()
            end_row = container[end_pos-1].copy()

            moving = []
            for _ in range(move_num):
                moved = start_row.pop()
                moving.append(moved)
            
            end_row = end_row.copy() + list(reversed(moving))
            
            container[start_pos-1] = start_row
            container[end_pos-1] = end_row
    print(container)

    return ''.join(row[-1] for row in container)

# print(move_crates2('input/test.txt', test=True))
print(move_crates2('input/05.txt', test=False))