def process_input(filename):
    a = []
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            a.append([int(i) for i in l.strip()])

    return a


def is_edge(x, y, a):
    num_rows = len(a)
    num_cols = len(a[0])
    top, right, bottom, left = False, False, False, False
    if x == 0:
        top = True
    elif x == num_rows - 1:
        bottom = True

    if y == 0:
        left = True
    elif y == num_cols - 1:
        right = True

    return top, right, bottom, left


def get_right_bottom_neighbors(x, y, a):
    top, right, bottom, left = is_edge(x, y, a)
    vals = []
    if not bottom:
        vals.append((x+1, y))
    if not right:
        vals.append((x, y+1))
    return vals


def get_top_left_neighbors(x, y, a):
    top, right, bottom, left = is_edge(x, y, a)
    vals = []
    if not top:
        vals.append((x-1, y))
    if not left:
        vals.append((x, y-1))
    return vals


def get_all_neighbors(x, y, a):
    top, right, bottom, left = is_edge(x, y, a)
    vals = []
    if not top:
        vals.append((x-1, y))
    if not left:
        vals.append((x, y-1))
    if not bottom:
        vals.append((x+1, y))
    if not right:
        vals.append((x, y+1))
    return vals


def main(filename):
    a = process_input(filename)

    costs = {}
    for x in range(len(a)):
        for y in range(len(a[0])):
            costs[(x, y)] = float('inf')
    costs[(0, 0)] = 0
    next_nodes = []
    nodes = [(0, 0)]

    while len(nodes) > 0:
        for curr_node in nodes:
            nbrs = get_right_bottom_neighbors(curr_node[0], curr_node[1], a)
            for n in nbrs:
                new_cost = costs[curr_node] + a[n[0]][n[1]]
                curr_cost = costs[n]
                if new_cost < curr_cost:
                    costs[n] = new_cost

                if n not in next_nodes:
                    next_nodes.append(n)

        nodes = next_nodes
        next_nodes = []

    return costs[(len(a)-1, len(a[0])-1)]


def expand_input_horizontal(a):
    new_a = a.copy()
    for i in range(1, 5):
        for x in range(len(a)):
            new_digits = [y+i if y+i < 10 else (y+i+1) % 10 for y in a[x]]
            new_row = new_a[x].copy() + new_digits
            new_a[x] = new_row

    return new_a


def expand_input_vertical(a):
    new_a = a.copy()
    for i in range(1, 5):
        for x in range(len(a)):
            new_digits = [y+i if y+i < 10 else (y+i+1) % 10 for y in a[x]]
            new_a.append(new_digits)

    return new_a


def main_2(filename):
    a = process_input(filename)
    a = expand_input_horizontal(a)
    a = expand_input_vertical(a)

    costs = {}
    for x in range(len(a)):
        for y in range(len(a[0])):
            costs[(x, y)] = float('inf')

    costs[(0, 0)] = 0
    next_nodes = []
    nodes = [(0, 0)]

    counter = 0
    while len(nodes) > 0:
        counter += 1
        for curr_node in nodes:
            nbrs = get_all_neighbors(curr_node[0], curr_node[1], a)
            for n in nbrs:
                new_cost = costs[curr_node] + a[n[0]][n[1]]
                curr_cost = costs[n]
                if new_cost < curr_cost:
                    costs[n] = new_cost

                    if n not in next_nodes:
                        next_nodes.append(n)

        nodes = next_nodes
        next_nodes = []

        if counter % 10 == 0:
            print(counter, len(nodes))

    return costs[(len(a)-1, len(a[0])-1)]

    # # found this basic solution below on github, seems basically the same but is a bit faster? not sure why
    # queue = [(0, 0)]
    # counter = 0
    # while queue:
    #     counter += 1
    #     current = queue.pop(0)
    #     neighbors = get_all_neighbors(current[0], current[1], a)
    #     for neighbor in neighbors:
    #         # if the current best cost to reach the neighbor is greater than the
    #         # cost to reach the current node plus the weight (risk) of the neighbor,
    #         # update the cost to reach the neighbor to the new minimum cost
    #         # and add the neighbor to the queue
    #         neighbor_cost = costs[(neighbor[0], neighbor[1])]
    #         cost_to_neighbor = costs[current[0],
    #                                  current[1]] + a[neighbor[0]][neighbor[1]]
    #         if neighbor_cost > cost_to_neighbor:
    #             costs[(neighbor[0], neighbor[1])] = cost_to_neighbor
    #             queue.append(neighbor)
    #     if counter % 10 == 0:
    #         print(counter, len(queue))
    # return costs[(len(a)-1, len(a[0])-1)]


# print(main('input/test.txt'))
# print(main('input/15_chiton.txt'))

# print(main_2('input/test.txt'))
print(main_2('input/15_chiton.txt'))

# ok honestly this code is embarrassing, but... it runs and gets the right answer.
# it takes 5 minutes, but it runs.
