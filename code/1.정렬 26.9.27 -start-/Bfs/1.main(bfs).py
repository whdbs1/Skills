from collections import deque
import time
sm,em = '325671400','123456700'
def aro(n):
    li = []
    for x in [-3,+3,-1,+1]:
        if 0 <= n+x <9 and (x in (-3,3) or n // 3 == (n+x) // 3):
            li.append(n+x)
    return li

def exc(m,s,e):
    m = list(m)
    m[s],m[e] = m[e],m[s]
    return ''.join(m)
    

def bfs():
    q = deque([sm])
    vst, par = {sm},{}
    while q:
        cur = q.popleft()
        if cur == em:
            break
        for ze,val in enumerate(cur):
            if val == '0':
                for ser in aro(ze):
                    cm = (exc(cur,ze,ser))
                    if cm not in vst:
                        par[cm] = [cur,[ser,ze]]
                        vst.add(cm)
                        q.append(cm)

    if em not in par and em != sm:
        return None
                            
    path = []
    cur = em
    while cur != sm:
        p, m = par[cur]
        path.append([m,cur])
        cur = p
    path.append(sm)

    return path
