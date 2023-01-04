with open('input/13.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    depart = int(lines[0])
    busses = []
    for bus in lines[1].split(','):
        if bus != 'x':
            busses.append(int(bus))

    min_wait_time = float('inf')
    best_bus = 0
    for bus in busses:
        wait_time = bus - (depart % bus)
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            best_bus = bus

    print('part one: ', min_wait_time * best_bus)

# part two
# solve with pypi?
from sympy.solvers import solve
from sympy import Symbol
from sympy.ntheory.modular import crt

with open('input/13.txt') as f:
    lines = f.readlines()
    busses = []

    for idx, bus in enumerate(lines[1].strip().split(',')):
        if bus != 'x':
            busses.append((int(idx), int(bus)))

    # create statement
    statement = ''
    for idx, bus in busses:
        statement += f'(t+{idx}) mod {bus} = 0, '
    print(statement)

    # can put this into wolfram lol and take the constant

    # another way: loop but increase loop multiplier when we get a correct hit
    # this works since all inputs are prime
    # thanks to reddit superthread and The_Droide for inspiration
    i = 1
    while not all([(i + k) % b == 0 for k, b in busses]):
        correct_busses = [b for k, b in busses if (i + k) % b == 0]
        prod = 1
        for b in correct_busses:
            prod *= b
        i += prod
    print(i)
