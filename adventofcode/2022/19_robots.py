def process_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        # keep blueprints in dict with idx key and value: 
        # [ore_cost, clay_cost, (obs_cost_ore, obs_cost_clay), (geo_cost_ore, geo_cost_obs)]
        bps = {}
        for l in lines:
            lsplit = l.split()
            ore_idx = [idx for idx, i in enumerate(lsplit) if i.replace('.', '') == 'ore']
            ore_robot = int(lsplit[ore_idx[1]-1])
            clay_robot = int(lsplit[ore_idx[2]-1])
            obs_robot = (int(lsplit[ore_idx[3]-1]), int(lsplit[ore_idx[3]+2]))
            geo_robot = (int(lsplit[ore_idx[4]-1]), int(lsplit[ore_idx[4]+2]))

            bps[int(lsplit[1][:-1])] = [ore_robot, clay_robot, obs_robot, geo_robot]
        
    return bps

def make_robots(fname):
    bps = process_input(fname)

    # so let's do a form of bfs? will probably fail on round 2 tbh
    # we need to keep track of num robots & curr resources for each
    # for each, let's do a dict of 2 dicts (1 with resources, 1 with robots

    paths = [{
        'rocks': {'ore': 0, 'clay': 0, 'obs': 0,'geo': 0},
        'robots': {'ore': 1, 'clay': 0, 'obs': 0,'geo': 0}
    }]
    new_paths = []
    best_geo_all_bps = {}
    

    for bp_idx, costs in bps.items():
        ore_cost, clay_cost, obs_cost, geo_cost = costs
        obs_cost_ore, obs_cost_clay = obs_cost
        geo_cost_ore, geo_cost_obs = geo_cost

        max_geo_per_bp = 0
        
        # keep track of what we've seen. 
        # maybe in a tuple like (*rocks, *robots)
        observed = set()

        for round in range(24):
            print(round, len(paths), len(observed))
            for p in paths:
                # if we look at all paths, this runs like molasses. set up an arbitrary culling step at round 12
                # maybe if no clay robots have been purchased by then?
                if round >= 8:
                    if not p['robots']['clay']:
                        continue
                
                if round >= 14:
                    if not p['robots']['obs'] or p['robots']['clay'] < 3:
                        continue
                
                if round >= 20:
                    if not p['robots']['geo'] or p['robots']['obs'] < 2:
                        continue

                # first add all new resources
                curr_robots, curr_rocks = p['robots'].copy(), p['rocks'].copy()
                new_rocks = curr_rocks.copy()

                for robot_type, robot_num in curr_robots.items():
                    new_rocks[robot_type] = robot_num + curr_rocks[robot_type]

                # buy robots if possible
                if ore_cost <= curr_rocks['ore']:
                    new_robots = curr_robots.copy()
                    new_robots['ore'] += 1
                    rocks_to_add = new_rocks.copy()
                    rocks_to_add['ore'] -= ore_cost

                    observed_path = tuple([*rocks_to_add, *new_robots])
                    if observed_path not in observed:
                        new_paths.append({'rocks': rocks_to_add, 'robots': new_robots})
                        observed.add(observed_path)
                
                if clay_cost <= curr_rocks['ore']:
                    new_robots = curr_robots.copy()
                    new_robots['clay'] += 1
                    rocks_to_add = new_rocks.copy()
                    rocks_to_add['ore'] -= clay_cost
                    observed_path = tuple([*rocks_to_add, *new_robots])
                    if observed_path not in observed:
                        new_paths.append({'rocks': rocks_to_add, 'robots': new_robots})
                        observed.add(observed_path)
                
                if obs_cost_ore <= curr_rocks['ore'] and obs_cost_clay <= curr_rocks['clay']:
                    new_robots = curr_robots.copy()
                    new_robots['obs'] += 1
                    rocks_to_add = new_rocks.copy()
                    rocks_to_add['ore'] -= obs_cost_ore
                    rocks_to_add['clay'] -= obs_cost_clay
                    observed_path = tuple([*rocks_to_add, *new_robots])
                    if observed_path not in observed:
                        new_paths.append({'rocks': rocks_to_add, 'robots': new_robots})
                        observed.add(observed_path)
                
                if geo_cost_ore <= curr_rocks['ore'] and geo_cost_obs <= curr_rocks['obs']:
                    new_robots = curr_robots.copy()
                    new_robots['geo'] += 1
                    rocks_to_add = new_rocks.copy()
                    rocks_to_add['ore'] -= geo_cost_ore
                    rocks_to_add['obs'] -= geo_cost_obs
                    observed_path = tuple([*rocks_to_add, *new_robots])
                    if observed_path not in observed:
                        new_paths.append({'rocks': rocks_to_add, 'robots': new_robots})
                        observed.add(observed_path)

                # add path where we don't do anything
                observed_path = tuple([*new_rocks, *curr_robots])
                if observed_path not in observed:
                    new_paths.append({'rocks': new_rocks, 'robots': curr_robots})
                    observed.add(observed_path)

                # if _ == 2:
                #     # for np in new_paths:
                #     #     print(np)
                #     exit()
            
            paths = new_paths
            new_paths = []
        
        for p in paths:
            if new_max := p['rocks']['geo'] > max_geo_per_bp:
                max_geo_per_bp = new_max
        best_geo_all_bps[bp_idx] = max_geo_per_bp

        return best_geo_all_bps

print(make_robots('input/test.txt'))

'''
Ignore any state lagging behind the best geode count by 2 or more (this is the big save and came very much from this thread)

Ignore any state lagging behind the best geode bot count by 2 or more (sort of a duplicate of the above but at one point I was desperate for memory and performance)

Ignore any state lagging behind the largest count of non-ore bots by 10 or more (this is probably not guaranteed to give an optimal solution but does work for my inputs and cuts the search space down a chunk).

Use a hash set for speed and to make sure states are unique (not sure if two paths can lead to the same state but my gut feeling is they can)

'''