def process_instr(idx, instr, acc):
    if instr[:3] == 'nop':
        return idx+1, acc
    
    val = int(instr.split()[1])
    if instr[:3] == 'jmp':
        return idx + val, acc
    else:
        return idx + 1, acc + val

def change_lines(change_idx, lines):
    l = lines[change_idx]
    if l[:3] == 'nop':
        new_lines = lines.copy()
        new_lines[change_idx] = new_lines[change_idx].replace('nop', 'jmp')
        return new_lines
    elif l[:3] == 'jmp':
        new_lines = lines.copy()
        new_lines[change_idx] = new_lines[change_idx].replace('jmp', 'nop')
        return new_lines

def test_changed(new_lines):
    acc, idx = 0, 0
    change_visited = {0}

    while idx < len(new_lines):
        idx, acc = process_instr(idx, new_lines[idx], acc)
        if idx in change_visited:
            return False
        change_visited.add(idx)

    return acc

with open('input/08.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    acc, idx = 0, 0
    visited = [0]

    # part one
    while True:
        idx, acc = process_instr(idx, lines[idx], acc)
        if idx in visited:
            # print('part one: ', acc)
            break
        visited.append(idx)
    
    # part two
    end = len(lines)
    change_idx = visited.pop(0)

    while True:
        while lines[change_idx][:3] == 'acc':
            change_idx = visited.pop(0)
        new_lines = change_lines(change_idx, lines)

        acc, idx = 0, 0
        change_visited = {0}
        
        if (ans := test_changed(new_lines)):
            print(ans)
            break
        else:
            change_idx = visited.pop(0)


        # while idx < end:
        #     idx, acc = process_instr(idx, new_lines[idx], acc)
        #     if idx in change_visited:
        #         change_idx = visited.pop(0)
        #         break
        #     change_visited.add(idx)
