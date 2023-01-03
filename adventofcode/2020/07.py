with open('input/07.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    # build dict containing all relationships
    # round one: ignore quantities

    # d has holding bags: held bags
    d, held_d = {}, {}
    for l in lines:
        k = l.split(' bags contain ')[0]

        all_v = []
        for v in l.split(' bags contain')[1].split(','):
            clean_v = (v[3:].replace('.', ''))
            all_v.append(clean_v.replace(' bags','').replace(' bag',''))
        d[k] = all_v
    
    # held_d has held bags: holding bags
    for k,vlist in d.items():
        for v in vlist:
            if v in held_d:
                curr_bags = held_d[v].copy()
                held_d[v] = curr_bags + [k]
            else:
                held_d[v] = [k]
    
    # get everything that holds shiny gold bags
    holding_bags = set(held_d['shiny gold'])
    all_holding_bags = holding_bags.copy()

    while len(holding_bags):
        next_bags = set()
        for bag in holding_bags:
            if bag in held_d:
                for v in held_d[bag]:
                    next_bags.add(v)
                    all_holding_bags.add(v)
        holding_bags = next_bags
        next_bags = set()

    print(len(all_holding_bags))

    # part 2: respect quantities
    # d[bag]: [(quant1, bagtype1), (quant2, bagtype2)]
    d = {}
    for l in lines:
        k = l.split(' bags contain ')[0]

        all_v = []
        for v in l.split(' bags contain')[1].split(','):
            clean_v = (v[3:].replace('.', ''))
            clean_v = clean_v.replace(' bags','').replace(' bag','')
            num_bags = 0 if v[1:3] == 'no' else int(v[1])
            all_v.append((num_bags, clean_v))
        d[k] = all_v

    total = 0

    # curr_bags is now a list of lists
    # each sublist is [num_bag_type, [(num_bag1_contains, type_bag1), (num_bag2_contains, type_bag2), ...]]
    curr_bags = [[1, d['shiny gold']]]
    new_bags = []

    while curr_bags:
        for num_bags, bag in curr_bags:
            for num_held, bag_type in bag:
                total += (num_held * num_bags)
                if bag_type in d:
                    new_bags.append([num_bags * num_held, d[bag_type]])
        curr_bags = new_bags
        new_bags = []
    
    print(total)
