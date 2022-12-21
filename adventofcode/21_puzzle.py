def funny_attempt(fname):
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.replace(':', '=').strip() for l in lines]

    unsolved = lines.copy()
    new = []
    while len(unsolved):
        for l in unsolved:
            try:
                exec(l)
            except NameError:
                new.append(l)
        
        unsolved = new
        new = []

    return locals()['root']

# this... works. lol.
# print(funny_attempt('input/test.txt'))
# print(funny_attempt('input/21.txt'))

def check_int(s):
    try:
        int(s)
        return True
    except:
        return False

# convert human to an expression first then solve for human (?)
def funny_attempt2(fname):
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.replace(':', ' =').strip() for l in lines]

        d = {}
        for l in lines:
            if l.startswith('root'):
                print(l)
                l = l.replace('+', '=')
                root_exp = l.split()[-3:]
            
            lsplit = l.split()
            
            if len(lsplit) <= 3:
                d[lsplit[0]] = lsplit[-1]
            else:
                d[lsplit[0]] = lsplit[-3:]
    
    looping = True
    while looping:
        looping = False
        new_exp = []
        for i in root_exp:
            if i in d and i != 'humn':
                if isinstance(d[i], list):
                    looping = True
                    new_exp.append('(')
                    for j in d[i]:
                        new_exp.append(j)
                    new_exp.append(')')
                else:
                    new_exp.append(d[i])
                
            else:
                new_exp.append(i)
        
        root_exp = new_exp
        new_exp = []
        
    eq = ''.join([str(r) for r in root_exp]).split('=')
    return eq[0], eq[1]

# print(funny_attempt2('input/test.txt'))
print(funny_attempt2('input/21.txt'))

# then solve the equation in mathpapa lol https://www.mathpapa.com/algebra-calculator.html
        
