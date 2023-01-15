def is_valid_ticket(l, valid_fields):
    for val in l.split(','):
        is_valid = False
        for fmin, fmax in valid_fields:
            if fmin <= int(val) <= fmax:
                is_valid = True
        if not is_valid:
            return False
    return True

with open('input/16.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    nearby_tix = []
    for l in lines[25:]:
        for i in l.split(','):
            nearby_tix.append(int(i))
    
    valid_fields = []
    for l in lines[:19]:
        f1, f2 = l.split()[-3], l.split()[-1]
        f1min, f1max = int(f1.split('-')[0]), int(f1.split('-')[1])
        valid_fields.append((f1min, f1max))
        f2min, f2max = int(f2.split('-')[0]), int(f2.split('-')[1])
        valid_fields.append((f2min, f2max))
    
    # ugh this is dumb but it always should work
    ans = 0
    for ticket in nearby_tix:
        add_to = True
        for fmin, fmax in valid_fields:
            if fmin <= ticket <= fmax:
                add_to = False
                break
        if add_to:
            ans += ticket
    print('part one', ans)

    # part two
    all_fields = set()
    fields_to_ranges = {}
    for lidx, l in enumerate(lines[:20]):
        all_fields.add(l.split(':')[0])
        f1, f2 = l.split()[-3], l.split()[-1]
        f1min, f1max = int(f1.split('-')[0]), int(f1.split('-')[1])
        f2min, f2max = int(f2.split('-')[0]), int(f2.split('-')[1])
        fields_to_ranges[l.split(':')[0]] = (f1min, f1max, f2min, f2max)

    possible_fields = {k: all_fields.copy() for k in range(20)}
    for l in lines[25:]:
        # first make sure ticket is valid
        if is_valid_ticket(l, valid_fields):
            for idx, i in enumerate(l.split(',')):
                curr_possibles = possible_fields[idx]
                for field in curr_possibles:
                    f1min, f1max, f2min, f2max = fields_to_ranges[field]

                    # i.e., ticket not between either possible field
                    if not (f1min <= int(i) <= f1max or f2min <= int(i) <= f2max):
                        curr_copy = curr_possibles.copy()
                        curr_copy.remove(field)
                        possible_fields[idx] = curr_copy

    translation_dict = {}
    used_fields = set()
    for i in range(20):
        for k,v in possible_fields.items():
            if i == len(v):
                translation_dict[k] = v - used_fields
                used_fields = used_fields | v

    my_ticket = [int(i) for i in lines[22].split(',')]
    ans = 1
    for k, v in translation_dict.items():
        field = list(v)[0]
        if field.startswith('departure'):
            ans *= my_ticket[k]
    
    print('part two: ', ans)
