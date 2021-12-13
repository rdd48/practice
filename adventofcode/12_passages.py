def process_input(filename):
    d = {}
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            nodes = l.strip().split('-')
            n1, n2 = nodes[0], nodes[1]
            if n1 in d.keys():
                d[n1] += [n2]
            else:
                d[n1] = [n2]
            if n2 in d.keys():
                d[n2] += [n1]
            else:
                d[n2] = [n1]

    return d


def main_1(filename):
    d = process_input(filename)
    paths = [['start', i] for i in d['start']]
    total = 0
    next_paths = []

    while len(paths) > 0:
        for idx, p in enumerate(paths):
            to_visit = d[p[-1]]
            for v in to_visit:
                if v == 'end':
                    total += 1
                elif v.isupper() or v not in p:
                    next_paths.append(p + [v])

        paths = next_paths
        next_paths = []

    return total


def main_2(filename):
    d = process_input(filename)
    paths = [['start', i] for i in d['start']]
    total = []
    next_paths = []

    while len(paths) > 0:
        for idx, p in enumerate(paths):
            to_visit = d[p[-1]]
            for v in to_visit:
                if v == 'end':
                    # print(','.join(p + ['end']))
                    total.append(p)
                elif v == 'start':
                    continue
                elif v.isupper():
                    next_paths.append(p + [v])
                elif p.count(v) < 2 and v not in p:
                    next_paths.append(p + [v])
                elif p.count(v) < 2:
                    append_next = True
                    for i in p:
                        # so we can revisit small caves twice, once per round.
                        # hence this long if statement here, basically saying:
                        # check all other lowercase vals in our path to make sure there's only one visit.
                        if i != v and p.count(i) > 1 and i.islower():
                            append_next = False
                    if append_next:
                        next_paths.append(p + [v])

        paths = next_paths
        next_paths = []

    return len(total)


# print(main_1('input/12_paths.txt'))
print(main_2('input/12_paths.txt'))
