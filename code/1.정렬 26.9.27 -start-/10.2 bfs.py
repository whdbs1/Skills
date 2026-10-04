import time
from collections import deque

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

def ch(m):
    res = []
    for i in [i for i in range(len(m)) if m[i] =='0']:
        for ser in aro(i):
            if m[ser] != str(0):
                res.append(exc(m,ser,i))
    return res
        
def bt():                            
    path = []
    cur = em
    while cur != sm:
        p, m = par[cur]
        path.append([m,cur])
        cur = p
    path.append(sm)

def bfs(m):
    em ='030125064'
    q = deque([m])
    vst = {m:0}
    while q:
        cur = q.popleft()
        if cur == em:
            break
        for i in range(len(ch('123456000'))):
            print(i)
                

st = time.time()

print(bfs('123456700'))
et = time.time()

res = et - st


print("실행 시간: {:.5f}초".format(res))
