def process_bash(fname, part2=False):
    with open(fname) as f:
        lines = f.readlines()

        d = {}
        curr = ['/']
        total = 0

        for l in lines[1:]:
            # skip all "dir" and "ls" lines: not necessary if we get file path from cd
            if l.startswith('$ cd'):
                if l.strip() == '$ cd ..':
                    curr.pop()
                    
                else:
                    new = l.strip().split()[-1]
                    curr.append(new)

            elif l[0] not in ['d', '$']:
                file_size = int(l.split()[0])
                total += file_size
                
                temp_path = '/'
                for path in curr:
                    if temp_path + path not in d:
                        d[temp_path + path] = 0
                    d[temp_path + path] += file_size
                    temp_path += path + '/'
        

        if not part2:
            score = 0
            for v in d.values():
                if v < 100000:
                    score += v
            
            # print(d)
            return score
        
        else:
            required = total - 40000000
            best = float('inf')
            for v in d.values():
                if v > required and v < best:
                    best = v
            return best

# print(process_bash('input/test.txt'))
print(process_bash('input/07.txt'))

# print(process_bash('input/test.txt', part2=True))
print(process_bash('input/07.txt', part2=True))