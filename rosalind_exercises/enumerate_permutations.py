num = 6

def dupcheck(x):
    for elem in x:
        if x.count(elem) > 1:
            return True
    return False

total = 0

for i in range(1,num+1):
    for j in range(1,num+1):
        for k in range(1,num+1):
            for l in range(1,num+1):
                for m in range(1,num+1):
                    for n in range(1,num+1):
                        if not dupcheck([i, j, k, l, m, n]):
                            total += 1
                            print(i, j, k, l, m, n)

print(total)