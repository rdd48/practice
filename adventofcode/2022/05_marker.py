def find_marker(fname):
    with open(fname) as f:
        line = f.readline().strip()

        for idx in range(1, len(line) - 3):
            if line[idx] not in line[idx+1:idx+4]:
                return idx + 4

print(find_marker('input/test.txt'))
print(find_marker('input/05.txt'))
