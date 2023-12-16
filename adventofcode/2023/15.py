def update_code(i, curr):
    curr += ord(i)
    curr *= 17
    curr %= 256
    return curr

def main(fname):
    with open(fname) as f:
        codes = [l.strip().split(',') for l in f.readlines()][0]

    total = 0
    for c in codes:
        curr = 0
        for i in c:
             curr = update_code(i, curr)
        total += curr   
    return total

def update_code2(i, curr):
    curr = 0
    for chr in i:
        curr += ord(chr)
        curr *= 17
        curr %= 256
    return curr

def check_box_for_id(boxchar, box, boxint):
    for idx, boxid in enumerate(box):
        if boxchar == boxid[0]:
            box[idx] = (boxchar, boxint)
            return box
    return False

def get_focusing_power(box, i):
    subtotal = 0
    for bidx, b in enumerate(box):
        subtotal += (i+1) * (bidx+1) * b[1]
    return subtotal
    
def main2(fname):
    with open(fname) as f:
        codes = [l.strip().split(',') for l in f.readlines()][0]

    # boxes is a dict of 0-255 keys: (char_id, num) values
    boxes = {k:[] for k in range(256)}
    for c in codes:
        if c[-1] == '-':
            boxchar = c[:-1]
            boxid = update_code2(boxchar, 0)
            box_copy = boxes[boxid].copy()
            boxes[boxid] = list(filter(lambda x:x[0] != boxchar, box_copy))
        elif '=' in c:
            boxchar, boxint = c.split('=')
            boxint = int(boxint)
            boxid = update_code2(boxchar, 0)
            box_copy = boxes[boxid].copy()
            if new_box := check_box_for_id(boxchar, box_copy, boxint):
                boxes[boxid] = new_box
            else:
                box_copy.append((boxchar, boxint))
                boxes[boxid] = box_copy
        else:
            exit('wtf?')
    
    total = 0
    for i in range(256):
        box = boxes[i]
        total += get_focusing_power(box, i)

    return total
    


print(main('input/15.txt'))
print(main2('input/15.txt'))
