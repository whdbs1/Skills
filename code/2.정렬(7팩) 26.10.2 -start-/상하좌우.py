mx = 3
m = [0,1,2,3,4,5,6,7,8]

def aro(n):
    res = []
    n = divmod(n,mx)
    x1, y1= [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(4):
        x2 = n[0] + x1[i]
        y2 = n[1] + y1[i]
        if 0 <= x2 < mx and 0 <= y2 < mx:
            res.append((x2, y2))
    return res

