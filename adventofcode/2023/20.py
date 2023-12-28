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

print(main('input/test.txt', 1000))
print(main('input/20.txt', 1000))