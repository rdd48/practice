def process_input(fname, part2=False):
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

            if part2 and int(lsplit[1][:-1]) == 3:
                return bps
        
    return bps

def make_robots(fname):
    bps = process_input(fname)

    # so let's do a form of bfs? will probably fail on round 2 tbh
    # we need to keep track of num robots & curr resources for each
    # for each, let's do a dict of 2 dicts (1 with resources, 1 with robots


    best_geo_all_bps = {}
    

    for bp_idx, costs in bps.items():
        ore_cost, clay_cost, obs_cost, geo_cost = costs
        obs_cost_ore, obs_cost_clay = obs_cost
        geo_cost_ore, geo_cost_obs = geo_cost

        max_geo_per_bp = 0
        best_geode, best_geode_robot, best_nongeo_robot = 0, 0, 0

        paths = [{
            'rocks': {'ore': 0, 'clay': 0, 'obs': 0,'geo': 0},
            'robots': {'ore': 1, 'clay': 0, 'obs': 0,'geo': 0}
        }]
        new_paths = []
        
        # keep track of what we've seen. 
        # maybe in a tuple like (*rocks, *robots)
        observed = set((0,0,0,0,1,0,0,0))

        for round in range(24):
            print(bp_idx, round)
            for p in paths:
                # if we look at all paths, this runs like molasses. set up an arbitrary culling step at round 12
                # maybe if no clay robots have been purchased by then?

                curr_geode = p['rocks']['geo']
                if curr_geode > best_geode:
                    best_geode = curr_geode
                elif curr_geode + 2 <= best_geode:
                    continue

                curr_geode_robot = p['robots']['geo']
                if curr_geode_robot > best_geode_robot:
                    best_geode_robot = curr_geode_robot
                elif curr_geode_robot + 2 <= best_geode_robot:
                    continue

                curr_nongeo_robots = sum([val for robot, val in p['robots'].items() if robot != 'geo'])
                if curr_nongeo_robots > best_nongeo_robot:
                    best_nongeo_robot = curr_nongeo_robots
                elif curr_nongeo_robots + 10 <= best_nongeo_robot:
                    continue

                # first add all new resources
                curr_robots, curr_rocks = p['robots'].copy(), p['rocks'].copy()
                new_rocks = curr_rocks.copy()

                for robot_type, robot_num in curr_robots.items():
                    new_rocks[robot_type] = robot_num + curr_rocks[robot_type]

                # buy robots if possible but don't if you're already at max capacity
                max_ore_needed = max(ore_cost, clay_cost, obs_cost_ore, geo_cost_ore)
                if ore_cost <= curr_rocks['ore'] and curr_robots['ore'] <= max_ore_needed:
                    new_robots = curr_robots.copy()
                    new_robots['ore'] += 1
                    rocks_to_add = new_rocks.copy()
                    rocks_to_add['ore'] -= ore_cost

                    observed_path = tuple([*rocks_to_add.values(), *new_robots.values()])
                    if observed_path not in observed:
                        new_paths.append({'rocks': rocks_to_add, 'robots': new_robots})
                        observed.add(observed_path)
                
                if clay_cost <= curr_rocks['ore'] and curr_robots['clay'] <= obs_cost_clay:
                    new_robots = curr_robots.copy()
                    new_robots['clay'] += 1
                    rocks_to_add = new_rocks.copy()
                    rocks_to_add['ore'] -= clay_cost
                    observed_path = tuple([*rocks_to_add.values(), *new_robots.values()])
                    if observed_path not in observed:
                        new_paths.append({'rocks': rocks_to_add, 'robots': new_robots})
                        observed.add(observed_path)
                
                if obs_cost_ore <= curr_rocks['ore'] and obs_cost_clay <= curr_rocks['clay'] and curr_robots['obs'] <= geo_cost_obs:
                    new_robots = curr_robots.copy()
                    new_robots['obs'] += 1
                    rocks_to_add = new_rocks.copy()
                    rocks_to_add['ore'] -= obs_cost_ore
                    rocks_to_add['clay'] -= obs_cost_clay
                    observed_path = tuple([*rocks_to_add.values(), *new_robots.values()])
                    if observed_path not in observed:
                        new_paths.append({'rocks': rocks_to_add, 'robots': new_robots})
                        observed.add(observed_path)
                
                if geo_cost_ore <= curr_rocks['ore'] and geo_cost_obs <= curr_rocks['obs']:
                    new_robots = curr_robots.copy()
                    new_robots['geo'] += 1
                    rocks_to_add = new_rocks.copy()
                    rocks_to_add['ore'] -= geo_cost_ore
                    rocks_to_add['obs'] -= geo_cost_obs
                    observed_path = tuple([*rocks_to_add.values(), *new_robots.values()])
                    if observed_path not in observed:
                        new_paths.append({'rocks': rocks_to_add, 'robots': new_robots})
                        observed.add(observed_path)

                # add path where we don't do anything
                observed_path = tuple([*new_rocks.values(), *curr_robots.values()])
                if observed_path not in observed:
                    new_paths.append({'rocks': new_rocks, 'robots': curr_robots})
                    observed.add(observed_path)
            
            paths = new_paths
            new_paths = []
        
        for p in paths:
            if p['rocks']['geo'] > max_geo_per_bp:
                max_geo_per_bp = p['rocks']['geo']
        best_geo_all_bps[bp_idx] = max_geo_per_bp

        ans = 0
        for idx, best_geo in best_geo_all_bps.items():
            ans += (idx * best_geo)

    print(best_geo_all_bps)
    return ans

# this takes like 15 minutes but is correct lol
# print(make_robots('input/test.txt'))
# print(make_robots('input/19.txt'))

def make_robots2(fname):
    bps = process_input(fname, part2=True)

    best_geo_all_bps = {}
    

    for bp_idx, costs in bps.items():
        ore_cost, clay_cost, obs_cost, geo_cost = costs
        obs_cost_ore, obs_cost_clay = obs_cost
        geo_cost_ore, geo_cost_obs = geo_cost

        max_geo_per_bp = 0
        best_geode, best_geode_robot, best_nongeo_robot = 0, 0, 0

        paths = [{
            'rocks': {'ore': 0, 'clay': 0, 'obs': 0,'geo': 0},
            'robots': {'ore': 1, 'clay': 0, 'obs': 0,'geo': 0}
        }]
        new_paths = []
        
        # keep track of what we've seen. 
        # maybe in a tuple like (*rocks, *robots)
        observed = set((0,0,0,0,1,0,0,0))

        for round in range(32):
            print(bp_idx, round)
            for p in paths:
                # if we look at all paths, this runs like molasses. set up an arbitrary culling step at round 12
                # maybe if no clay robots have been purchased by then?

                curr_geode = p['rocks']['geo']
                if curr_geode > best_geode:
                    best_geode = curr_geode
                elif curr_geode + 3 <= best_geode:
                    continue

                curr_geode_robot = p['robots']['geo']
                if curr_geode_robot > best_geode_robot:
                    best_geode_robot = curr_geode_robot
                elif curr_geode_robot + 2 <= best_geode_robot:
                    continue

                curr_nongeo_robots = sum([val for robot, val in p['robots'].items() if robot != 'geo'])
                if curr_nongeo_robots > best_nongeo_robot:
                    best_nongeo_robot = curr_nongeo_robots
                elif curr_nongeo_robots + 10 <= best_nongeo_robot:
                    continue

                # first add all new resources
                curr_robots, curr_rocks = p['robots'].copy(), p['rocks'].copy()
                new_rocks = curr_rocks.copy()

                for robot_type, robot_num in curr_robots.items():
                    new_rocks[robot_type] = robot_num + curr_rocks[robot_type]

                # buy robots if possible but don't if you're already at max capacity
                max_ore_needed = max(ore_cost, clay_cost, obs_cost_ore, geo_cost_ore)
                if ore_cost <= curr_rocks['ore'] and curr_robots['ore'] <= max_ore_needed:
                    new_robots = curr_robots.copy()
                    new_robots['ore'] += 1
                    rocks_to_add = new_rocks.copy()
                    rocks_to_add['ore'] -= ore_cost

                    observed_path = tuple([*rocks_to_add.values(), *new_robots.values()])
                    if observed_path not in observed:
                        new_paths.append({'rocks': rocks_to_add, 'robots': new_robots})
                        observed.add(observed_path)
                
                if clay_cost <= curr_rocks['ore'] and curr_robots['clay'] <= obs_cost_clay:
                    new_robots = curr_robots.copy()
                    new_robots['clay'] += 1
                    rocks_to_add = new_rocks.copy()
                    rocks_to_add['ore'] -= clay_cost
                    observed_path = tuple([*rocks_to_add.values(), *new_robots.values()])
                    if observed_path not in observed:
                        new_paths.append({'rocks': rocks_to_add, 'robots': new_robots})
                        observed.add(observed_path)
                
                if obs_cost_ore <= curr_rocks['ore'] and obs_cost_clay <= curr_rocks['clay'] and curr_robots['obs'] <= geo_cost_obs:
                    new_robots = curr_robots.copy()
                    new_robots['obs'] += 1
                    rocks_to_add = new_rocks.copy()
                    rocks_to_add['ore'] -= obs_cost_ore
                    rocks_to_add['clay'] -= obs_cost_clay
                    observed_path = tuple([*rocks_to_add.values(), *new_robots.values()])
                    if observed_path not in observed:
                        new_paths.append({'rocks': rocks_to_add, 'robots': new_robots})
                        observed.add(observed_path)
                
                if geo_cost_ore <= curr_rocks['ore'] and geo_cost_obs <= curr_rocks['obs']:
                    new_robots = curr_robots.copy()
                    new_robots['geo'] += 1
                    rocks_to_add = new_rocks.copy()
                    rocks_to_add['ore'] -= geo_cost_ore
                    rocks_to_add['obs'] -= geo_cost_obs
                    observed_path = tuple([*rocks_to_add.values(), *new_robots.values()])
                    if observed_path not in observed:
                        new_paths.append({'rocks': rocks_to_add, 'robots': new_robots})
                        observed.add(observed_path)

                # add path where we don't do anything
                observed_path = tuple([*new_rocks.values(), *curr_robots.values()])
                if observed_path not in observed:
                    new_paths.append({'rocks': new_rocks, 'robots': curr_robots})
                    observed.add(observed_path)
            
            paths = new_paths
            new_paths = []
        
        for p in paths:
            if p['rocks']['geo'] > max_geo_per_bp:
                max_geo_per_bp = p['rocks']['geo']
        best_geo_all_bps[bp_idx] = max_geo_per_bp

    ans = 1
    for best_geo in best_geo_all_bps.values():
        ans *= best_geo

    print(best_geo_all_bps)
    return ans


# this is also stupid slow, but whatever. i got the correct answer after another 10 min lol

# print(make_robots2('input/test.txt'))
print(make_robots2('input/19.txt'))
