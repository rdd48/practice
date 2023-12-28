import numpy as np
from sympy import Symbol
from sympy import solve_poly_system

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


def main2(fname):
    # needed a ton of help from reddit
    # https://topaz.github.io/paste/#XQAAAQBPCwAAAAAAAAA0m0pnuFI8c+qagMoNTEcTIfyUWj6FDwjYeb/2OTEpuch7ZM6w3JfTBcVQW1ku35Ks7ybi/CKFq8Xc27K4xWWdXGVKv9G8fAjoZn8OKbxv8VAsRhqHZfu9uyUOsO1MtDBf7H3AJiFefjccWDnGZlXlRvbhbpPHPKA6pndA9r39qvV8KWEoMoctrCOr0YrCiLMvGziz4EiRAvzRtr9ca8CYZbSb3kv1mVTQGRl92aaYjJI0MT6obpSuWTUtHfVTwVD6/LQGlvsmbUHqxrq5JYeLVbs8ZODdAA2i3AD6r2cLCpmtHB5nQgJ1EfEXMX30DAD6D5u8C4T3DYeaUE3A4UoideacYMpucZXeSnBTyWNmm2PF2N9ouCSdskSY3xCJHGZ5BY6S75EdIstnaGwYFZpCcvj4jijkzs5ovtmpcHEFZpewDUieQGpegwf0nPq0sQE7Z7noIgSOJXipEMS4xjxWeCt0pr8OrGPiL77pXuv24qHacVCu3cuE6AIUmRchbK0p1XQdgAC2YmXCayNI8Z8usZKiQD9W5mzzLZs7AZ49ui1UdXoOlV8RKWrwwPIM14axuOtabLmW5ftXI79w3FVb+WpMoP3WXP+xrwsmMgD8PvNh18pide+AVtUGgqVb/SD93XG6iWQ7b6qsAfmRx4m9jglU9KfNHjLkuXNik2cpDXT3RxUuoZ2RE5KhxSsnqRGp3iNvUEfOzYuba+1VW/hA+ob3TI+yD7zZ8S0Nu0zNSZx1tmaTGQOinGDwQNKuokM1cEVARF0xWGZxba9ao8ntBvWO+jOBrRSWWZJe61lx8o8bqeVVzl5xEJcR1765aVT0uhdWHq7NJXrG+ltBTMgJL2e6NQ94hPoy3EFFDHOs1sMN83SODkKdOMBW1K275fwLsLLdQkRYvHQC2D/yj6mVkfOGY3WyNCN8m9T0J4DYP5RnTgNNygZ1FflOehznnUctwOcIMnAwZoJahFSOcmLJ8HuTBdMHXbLOwkxahl4cy49iCblno9eApPdtjvMvDB4xtfeuzbyRaghc2D7sTNgTkGmSeJqsBYb1bYUJqDfXp+NKIi0XkxPdG44jm2sPiFLWDelbFyPbNV+6OL+XjRnyT/RO/YVZ0yxsze/tyBo+nIMOoz9UTZE08Lv7wJ/EgaUbs+moCG5KRhHDcmgwCjJ1glL5N8jLCtusYum5wCulFnsi8vImA2t3Ry154p/HFflEkTpQiGNyJch/lhsKUs16EbdBW9F7fahl0Pxltep1g031LDjDfSTUsGe+OtWG2nN1m/IF0oW9j0z4eTPONWvN8BxMCZ/cMTYwd1pcxRJpoSRIJvYsgb2GQtpTdpLZ6DnEClI0clrhWvcv43ifZI6mqdkwj/4H5dpU6lbN5QrK9YEu7Na+NqdbfA8G4OUm6QtB5oNbYSd/7b6WbpN3OMO/dFZJt/AgWgd+5gjHIm9l5YS43aYa+VgZDyeoLEU32vAgzssTSeG0l3ybjUVy4GQ3n6DZXHFRb9W1CT4kVvecNdNxUfgj7IhqQKGYkY7t6rDiZC0S3x4R715/wRP589FNC+EJhVPXrGMNACKJfghehjfdo26MyJGuqqXK7ndsLvsHRG2UseoDvWwAqPrpWQFip29pikdkMJFl/XddwDYdnBw90BAibjkkR2AINQeUz8LgzU9mI63aF6zk476P0m33BFuEfhZAecMYnFwuF4fahSdn79nvgGdTx0CmldhPg5ICq23gu+wjDBx+HUjQwzcpXd4CpzJJeTz0cMN2OVqwFGSVK9ChArzD/hUNlnDN6/LgFccICE68/HFSSLo6WFOl5Va2dLcrKnvT/7I8WnI=
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

    shards = []
    for line in lines:
        pos, vel = line.strip().split(" @ ")
        px,py,pz = pos.split(", ")
        vx,vy,vz = vel.split(", ")
        shards.append((int(px),int(py),int(pz),int(vx),int(vy),int(vz)))

    count = 0

    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    vx = Symbol('vx')
    vy = Symbol('vy')
    vz = Symbol('vz')

    equations = []
    t_syms = []

    for idx,shard in enumerate(shards[:5]):
        #vx is the velocity of our throw, xv is the velocity of the shard we're trying to hit. Yes, this is a confusing naming convention.
        x0,y0,z0,xv,yv,zv = shard
        t = Symbol('t'+str(idx)) #remember that each intersection will have a different time, so it needs its own variable

        #(x + vx*t) is the x-coordinate of our throw, (x0 + xv*t) is the x-coordinate of the shard we're trying to hit.
        #set these equal, and subtract to get x + vx*t - x0 - xv*t = 0
        #similarly for y and z
        eqx = x + vx*t - x0 - xv*t
        eqy = y + vy*t - y0 - yv*t
        eqz = z + vz*t - z0 - zv*t

        equations.append(eqx)
        equations.append(eqy)
        equations.append(eqz)
        t_syms.append(t)

    result = solve_poly_system(equations,*([x,y,z,vx,vy,vz]+t_syms))

    return result[0][0]+result[0][1]+result[0][2] #part 2 answer

print(main2('input/24.txt'))