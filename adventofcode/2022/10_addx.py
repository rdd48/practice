def cycles(fname):
    with open(fname) as f:
        lines = f.readlines()
        cycle, x, strengths = 1, 1, 0
        cycles = (20, 60, 100, 140, 180, 220)

        for l in lines:
            l = l.strip()
            if l.startswith('noop'):
                cycle += 1
                if cycle in cycles:
                    strengths += (cycle * x)
                
            elif l.startswith('addx'):
                
                cycle += 1
                if cycle in cycles:
                    strengths += (cycle * x)
                cycle += 1
                x += int(l.split()[-1])
                if cycle in cycles:
                    strengths += (cycle * x)
                
    
    return strengths
                
# print(cycles('input/test.txt'))
print(cycles('input/10.txt'))

def pixels(fname):
    with open(fname) as f:
        lines = f.readlines()
        x, cycle = 1, 0
        sprites = ['*'] * 240

        for l in lines:
            l = l.strip()
            if l.startswith('noop'):
                sprite_pos = (x-1, x, x+1)
                if cycle % 40 in sprite_pos:
                    sprites[cycle] = '#'
                cycle += 1
                
            elif l.startswith('addx'):
                sprite_pos = (x-1, x, x+1)
                if cycle % 40 in sprite_pos:
                    sprites[cycle] = '#'
                cycle += 1
                
                if cycle % 40 in sprite_pos:
                    sprites[cycle] = '#'
                cycle += 1
            
                x += int(l.split()[-1])
    
    substr = ''
    for i in range(0, 240, 5):
        # helps visibility to add space after every 5 chars
        substr += ''.join(sprites[i:i+5]) + ' '
        if i % 40 == 35:
            print(substr)
            substr = ''


                
# print(pixels('input/test.txt'))
print(pixels('input/10.txt'))