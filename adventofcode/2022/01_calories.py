def get_max_cals(filename):

    with open(filename) as f:
        lines = f.readlines()

        cals = 0
        max_cals = 0

        for l in lines:
            if l.strip():
                cals += int(l.strip())
            else:
                if cals > max_cals:
                    max_cals = cals
                cals = 0
    
    # get last cals value
    if cals > max_cals:
        max_cals = cals

    return max_cals

def get_top_three_cals(filename):

    with open(filename) as f:
        lines = f.readlines()

        cals = 0
        all_cals = []

        for l in lines:
            if l.strip():
                cals += int(l.strip())
            elif not l.strip():
                all_cals.append(cals)
                cals = 0
        
        # get last cals value
        all_cals.append(cals)
    
    all_cals.sort(reverse=True)

    return sum(all_cals[:3])



# print(get_max_cals('input/test.txt'))
print(get_max_cals('input/01.txt'))
print(get_top_three_cals('input/01.txt'))
