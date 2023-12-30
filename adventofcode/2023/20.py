from math import lcm

class Flipflop:
    def __init__(self, name, children):
        self.name = name
        self.state = False
        self.children = [i.replace(' ','') for i in children.split(',')]
        self.module = 'flipflop'
    
    def pulse(self, origin, stype):
        if stype == 'low':
            new_stype = 'high' if not self.state else 'low'
            self.state = not self.state
            return [(self.name, i, new_stype) for i in self.children]
        elif stype == 'high':
            return []

class Conjunction:
    def __init__(self, name, children):
        self.name = name
        self.children = [i.replace(' ','') for i in children.split(',')]
        self.all_states = {}
        self.module = 'conjunction'
    
    def add_states(self, parent):
        self.all_states[parent] = 'low'

    def pulse(self, origin, stype):
        self.all_states[origin] = stype
        if len(self.all_states.values()) == list(self.all_states.values()).count('high'):
            return [(self.name, i, 'low') for i in self.children]
        else:
            return [(self.name, i, 'high') for i in self.children]

def push_button(modules, signals):
    new_signals = []
    low, high = 1,0
    while True:
        for origin, sname, stype in signals:
            # print(origin, stype, sname)
            if stype == 'low':
                low += 1
            elif stype == 'high':
                high += 1
            if sname not in modules:
                continue
                # return low * high
            new_module = modules[sname]
            output = new_module.pulse(origin, stype)
            if output:
                for i in output:
                    new_signals.append(i)
        
        if not new_signals:
            return low, high, modules
        
        signals = new_signals.copy()
        new_signals = []

def main(fname, rounds):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    
    modules = {}
    for l in lines:
        name, children = l.split(' -> ')
        name = name.replace(' ','')[1:]
        if l.startswith('%'):
            modules[name] = Flipflop(name, children)
        elif l.startswith('&'):
            modules[name] = Conjunction(name, children)
        elif l.startswith('broadcaster'):
            signals = [('bcast', i.replace(' ',''), 'low') for i in children.split(',')]
    
    all_mods = modules.values()
    for m in all_mods:
        if m.module == 'conjunction':
            for m2 in all_mods:
                if m2.module == 'flipflop':
                    if m.name in m2.children:
                        m.add_states(m2.name)
    
    low, high = 0,0

    for _ in range(rounds):
        nl, nh, modules = push_button(modules, signals)
        low += nl
        high += nh
    
    return low * high

def push_button2(modules, signals):
    new_signals = []

    controller_signals = []
    while True:
        for origin, sname, stype in signals:
            # print(origin, stype, sname)
            if sname not in modules:
                continue
                # return low * high
            new_module = modules[sname]
            output = new_module.pulse(origin, stype)
            if output:
                for i in output:
                    new_signals.append(i)
                    origin, sname, stype = i
                    if origin in ('st', 'tn', 'hh', 'dt') and stype == 'high':
                        controller_signals.append(origin)
        
        if not new_signals:
            return modules, controller_signals
        
        signals = new_signals.copy()
        new_signals = []

def check_signals(d):
    for v in d.values():
        if not v:
            return False
    return True

def main2(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    
    modules = {}
    for l in lines:
        name, children = l.split(' -> ')
        name = name.replace(' ','')[1:]
        if l.startswith('%'):
            modules[name] = Flipflop(name, children)
        elif l.startswith('&'):
            modules[name] = Conjunction(name, children)
        elif l.startswith('broadcaster'):
            signals = [('bcast', i.replace(' ',''), 'low') for i in children.split(',')]
    
    all_mods = modules.values()
    for m in all_mods:
        if m.module == 'conjunction':
            for m2 in all_mods:
                if m2.module == 'flipflop':
                    if m.name in m2.children:
                        m.add_states(m2.name)
    
    controllers = {'st': False, 'tn': False, 'hh': False, 'dt': False}
    rd = 0
    while True:
        rd += 1
        # needed the subreddit's help on this, but basically:
        # rx needs to receive a low pulse from lv in my input
        # lv is controlled by &st, &tn, &hh, and &dt
        # so it becomes an lcm problem when these 4 all send a high pulse
        modules, controller_signals = push_button2(modules, signals)
        for cs in controller_signals:
            controllers[cs] = rd
        
        if check_signals(controllers):
            all_signals = list(controllers.values())
            return lcm(*all_signals)

# print(main('input/test.txt', 1000))
print(main('input/20.txt', 1000))
print(main2('input/20.txt'))