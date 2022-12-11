import math

class Monkey:
    def __init__(self, items, op, div_num, true, false):

        # items is a list
        self.items = items

        # op is the part of the operation line after "="
        if op.split()[1] == '+':
            self.op = lambda x: x + int(op.split()[-1])
        elif op.split()[1] == '*':
            if op.split()[-1] == 'old':
                self.op = lambda x: x ** 2
            else:
                self.op = lambda x: x * int(op.split()[-1])
        
        self.div_num = int(div_num)
        self.true = int(true)
        self.false = int(false)

        self.inspect = 0
    
    def check_op(self, lcm=False):
        self.inspect += 1
        curr = self.items[0]

        if not lcm:
            new = self.op(curr) // 3
        else:
            new = self.op(curr) % lcm

        del self.items[0]

        if new % self.div_num == 0:
            return self.true, new
        else:
            return self.false, new
    
    def add_item(self, item):
        self.items.append(item)
    
    def get_items(self):
        return self.items

def monkey_throw(fname, part2=False):
    monkeys = []
    with open(fname) as f:
        lines = f.readlines()

        # process each monkey
        for idx in range(0, len(lines), 7):
            # determine items
            items = lines[idx+1].split(':')[-1].strip()
            items = [int(i) for i in items.split(',')]
            
            # get all other info
            op = lines[idx+2].split('=')[-1].strip()
            div_num = lines[idx+3].split('by')[-1].strip()
            true = lines[idx+4].split('monkey')[-1].strip()
            false = lines[idx+5].split('monkey')[-1].strip()

            monkeys.append(Monkey(items, op, div_num, true, false))
        
        if part2:
            # this part i couldn't conecptualize: didn't know the math operations to speed this up
            # big thanks to: https://aoc.just2good.co.uk/2022/11
            lcm = math.lcm(*[m.div_num for m in monkeys])
        else:
            lcm = False
        
        num_rounds = 20 if not part2 else 10000
        for _ in range(num_rounds):
            for m in monkeys:
                for _ in range(len(m.items)):
                    next_m_idx, value = m.check_op(lcm)
                    monkeys[next_m_idx].add_item(value)

                    
        max_insp = sorted([m.inspect for m in monkeys], reverse=True)
        return max_insp[0] * max_insp[1]
            
# print(monkey_throw('input/test.txt'))
print(monkey_throw('input/11.txt'))

# print(monkey_throw2('input/test.txt'))
print(monkey_throw('input/11.txt', part2=True))