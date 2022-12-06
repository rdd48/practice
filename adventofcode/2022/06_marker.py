def find_marker(fname, part2=False):
    with open(fname) as f:
        line = f.readline().strip()

        marker_len = 14 if part2 else 4

        for idx in range(1, len(line) - 3):

            # sets don't allow duplicates, so it's an easy way to check if dupes exist
            if len(set(line[idx:idx+marker_len])) == marker_len:
                return idx + marker_len


# print(find_marker('input/test.txt'))
print(find_marker('input/06.txt'))

# print(find_marker('input/test.txt', part2=True))
print(find_marker('input/06.txt', part2=True))
