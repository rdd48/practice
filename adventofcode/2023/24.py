import numpy as np

def check_path(xcross, ycross, x, y, dx, dy):
    if dx > 0 and xcross < x:
        return False
    elif dx < 0 and xcross > x:
        return False
    if dy > 0 and ycross < y:
        return False
    elif dy < 0 and ycross > y:
        return False
    return True

def main(fname, left, right):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    
    xyzs, dirs = [],[]
    for l in lines:
        sl = l.split('@')
        xyzs.append([int(i) for i in sl[0].split(',')])
        dirs.append([int(i) for i in sl[1].split(',')])
    
    xymbs = []
    for xyz,d in zip(xyzs, dirs):
        x,y,_ = xyz
        dx,dy,_ = d

        if not dx:
            m = np.inf
            b = None
        else:
            m = dy/dx
            b = y-(m*x)
        xymbs.append((x,y,m,b,dx,dy))
    
    ans = 0
    for idx1, xymb1 in enumerate(xymbs):
        for xymb2 in xymbs[idx1+1:]:
            x1,y1,m1,b1,dx1,dy1 = xymb1
            x2,y2,m2,b2,dx2,dy2 = xymb2
        
            if m1 == m2:
                continue
            elif not b1:
                xcross = x1
                ycross = (m2 * xcross) + b2
            elif not b2:
                xcross = x2
                ycross = (m1 * xcross) + b1
            else:
                xcross = (b2-b1) / (m1-m2)
                ycross = (xcross * m1) + b1
            
            if left <= xcross <= right and left <= ycross <= right:
                p1 = check_path(xcross, ycross, x1, y1, dx1, dy1)
                p2 = check_path(xcross, ycross, x2, y2, dx2, dy2)
                if p1 and p2:
                    ans += 1

    return ans

print(main('input/test.txt',7,27))
print(main('input/24.txt',200000000000000,400000000000000))
