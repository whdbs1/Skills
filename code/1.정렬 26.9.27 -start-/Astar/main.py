import heapq
import time
sm,em ='325671400','123456700'
mx,my = 3,3

def aro(n):
    res = []
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    y,x = (n//mx)%my,n%mx
    for i in range(4):
        y1,x1 = y+dy[i],x+dx[i]
        if -1<y1<mx and -1<x1<mx:
            res.append(y1*mx+x1)
    return res

def exc(m,s,e):
    m = list(m)
    m[s],m[e] = m[e],m[s]
    return''.join(m)

def f(m,f):
        for fd in [i for i in range(len(m)) if m[i] == str(f)]:
            return (fd//mx,fd%mx)

def hst(sm,em):
    t = 0
    for i in range(9):
        if em[i] != str(0):
            t += abs(f(em,i+1)[0] - f(sm,i+1)[0]) + abs(f(em,i+1)[1] - f(sm,i+1)[1])
    return t

def ast():
    par = {}
    cl = {}
    ol = []
    g = 0
    heapq.heappush(ol,(hst(sm,em)+g,g,sm))
    cl[sm] = g
    while ol:
        f,g,cur = heapq.heappop(ol)
        if cl[cur] < g:
            continue
        if cur == em:
            break
        for i in range(len(cur)):
            if cur[i] == str(0):
                for ser in aro(i):
                    ng = g + 1
                    cm = exc(cur,i,ser)
                    if cm not in cl or ng < cl[cm]:
                        cl[cm] = ng
                        par[cm] = cur
                        heapq.heappush(ol,(ng + hst(cm,em),ng,cm))
    path = []
    cur = em
    while cur != sm:
        path.append(cur)
        cur = par[cur]
    path.append(sm)
    path.reverse()

    return path
