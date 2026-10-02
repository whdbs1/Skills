import time


def aro(n,mx=3):
    res = []
    n = divmod(n,mx)
    x1, y1= [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(4):
        x2 = n[0] + x1[i]
        y2 = n[1] + y1[i]
        if 0 <= x2 < mx and 0 <= y2 < mx:
            res.append(x2*mx+y2)
    return res

def exc(m,s,e):
    m = list(m)
    m[s],m[e] = m[e],m[s]
    return [''.join(m),[s,e]]

def exp(m):
    return [ser for i, val in enumerate(m) if val == '0' for ser in aro(i) if m[ser] != '0']

def bfs()
    




st = time.time()

print(exp('123456000'))
et = time.time()
res = et - st


print("실행 시간: {:.5f}초".format(res))
