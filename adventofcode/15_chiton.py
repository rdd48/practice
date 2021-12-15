import numpy as np


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


def get_lowest_cost_nbr(x, y, a, processed):
    nbrs = get_right_bottom_neighbors(x, y, a)
    costs = {n: a[n[0]][n[1]] for n in nbrs}
    lowest_cost = float('inf')
    lowest_cost_nbr = None
    for nbr, cost in costs.items():
        if cost < lowest_cost and cost not in processed:
            lowest_cost = cost
            lowest_cost_nbr = nbr

    return lowest_cost_nbr


def main(filename):
    a = process_input(filename)

    costs = {}
    for x in range(len(a)):
        for y in range(len(a[0])):
            costs[(x, y)] = float('inf')
    costs[(0, 0)] = 0
    next_nodes = []
    nodes = [(0, 0)]
    # paths = [[(0, 0), n] for n in first_nbrs]
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

        # print(next_nodes)
        # if len(next_nodes) >= 4:
        #     exit()
        nodes = next_nodes
        next_nodes = []

    # for k, v in costs.items():
    #     print(k, v)

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

    # print(costs)


# print(main('input/test.txt'))
print(main('input/15_chiton.txt'))

# print(main_2('input/test.txt'))
print(main_2('input/15_chiton.txt'))

# ok honestly this code is embarrassing, but... it runs and gets the right answer.
# it takes 5 minutes, but it runs.
