# so uh the trick here is just arbitrarily keeping the top-5000 scoring options after step 5ish or so
# thanks to https://github.com/llimllib/personal_code/blob/master/misc/advent/2022/16/a.py for the idea this time

def process_input(fname):
    valve_flow, valve_tunnels = {}, {}
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        for l in lines:
            split_l = l.split()
            name = split_l[1]
            flow = int(split_l[4].replace('rate=', '').replace(';', ''))
            tunnels = [i.replace(',','') for i in split_l[9:]]

            valve_flow[name] = flow
            valve_tunnels[name] = tunnels

            # valves.append(Valve(name, flow, tunnels))
    return valve_flow, valve_tunnels

def open_valves(fname):
    valve_flow, valve_tunnels = process_input(fname)

    time = 30

    # paths is a main list containing:
    # list of visited nodes
    # list of opened nodes
    # current flow
    zero_flow = set([k for k, v in valve_flow.items() if v == 0])
    paths = [
        [['AA'], [], 0]
    ]
    new_paths = []

    for minute in range(1, time+1):
        min_left = time - minute
        for path, opened, curr_flow in paths:
            curr = path[-1]

            # open valve if possible
            # and add valve to opened
            if curr not in opened and curr not in zero_flow:
                new_total = curr_flow + (min_left * valve_flow[curr])
                new_paths.append([path, opened + [curr], new_total])

            # move to all possible nodes not already in path
            for tunnel in valve_tunnels[curr]:
                new_paths.append([path + [tunnel], opened.copy(), curr_flow])

        paths = new_paths
        new_paths = []

        if minute > 5:
            # sort by score and keep only top 5000 (arbitrarily)
            paths.sort(key=lambda x:x[2], reverse=True)
            paths = paths[:5000]


    
    return paths[0][-1]

# print(open_valves('input/test.txt'))
print(open_valves('input/16.txt'))


def open_valves2(fname):
    valve_flow, valve_tunnels = process_input(fname)

    time = 26

    # paths is a main list containing:
    # list of my visited nodes
    # list of my opened nodes
    # list of elephant visited nodes
    # current flow
    zero_flow = set([k for k, v in valve_flow.items() if v == 0])
    paths = [
        [['AA'], [], ['AA'], 0]
    ]
    new_paths = []

    for minute in range(1, time+1):
        min_left = time - minute
        for path, opened, ele_path, curr_flow in paths:
            curr = path[-1]
            ele_curr = ele_path[-1]

            # open valve if possible
            # and add valve to opened
            if curr not in opened and curr not in zero_flow:
                new_total = curr_flow + (min_left * valve_flow[curr])
                
                # have elephant open valve if possible
                if ele_curr != curr and ele_curr not in opened and ele_curr not in zero_flow:
                    # new_total += (min_left * valve_flow[ele_curr])
                    new_paths.append([path, opened + [curr, ele_curr], ele_path, new_total + (min_left * valve_flow[ele_curr])])

                # have elephant move to possible nodes
                for ele_tunnel in valve_tunnels[ele_curr]:
                    new_paths.append([path, opened + [curr], ele_path + [ele_tunnel], new_total])

            # move to all possible nodes not already in path
            for tunnel in valve_tunnels[curr]:

                # have ele open valve
                if ele_curr not in opened and ele_curr not in zero_flow:
                    new_total = curr_flow + (min_left * valve_flow[ele_curr])
                    new_paths.append([path + [tunnel], opened + [ele_curr], ele_path, new_total])

                # have elephant move to possible nodes
                for ele_tunnel in valve_tunnels[ele_curr]:
                    new_paths.append([path + [tunnel], opened.copy(), ele_path + [ele_tunnel], curr_flow])

        paths = new_paths
        new_paths = []

        if minute >= 5:
            # sort by score and keep only top 5000 (arbitrarily)
            paths.sort(key=lambda x:x[3], reverse=True)
            paths = paths[:5000]

    return paths[0][-1]

# print(open_valves2('input/test.txt'))
print(open_valves2('input/16.txt'))
