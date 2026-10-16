from collections import deque
import heapq
import time

def aro(m):
    c = []
    for i, val in enumerate(m):
        if val != '0':
            continue

        for j in (1, x, -1, -x):
            a = i
            cm = list(m)

            while True:
                n = a + j
                if not (0 <= n < x*y):
                    break
                if abs(j) == 1 and a//x != n//x:
                    break
                if cm[n] == '0':
                    break

                cm[a], cm[n] = cm[n], cm[a]
                a = n
                c.append([''.join(cm), [a, i]])

    return c
x,y = 3,3
def aro(m):
    c = []
    for i, val in enumerate(m):
        if val != '0':
            continue
        for j in (1,x,-1,-x):
            a = i+j
            if -1<a<x*y and (abs(j)==x or i//x==a//x) and m[a] != '0':
                cm = list(m)
                cm[i], cm[a] = cm[a], cm[i]
                c.append([''.join(cm),[a,i]])
    return c

def bfs(sm='700134652',em='123456700'):
    q = deque([sm])
    vst,par = {sm},{}
    while q:
        cur = q.popleft()
        if cur == em:
            break
        for cm ,s in aro(cur):
            if cm not in vst:
                par[cm] = [cur,s]
                vst.add(cm)
                q.append(cm)
    path = []
    cur = em
    while cur != sm:
        p,m = par[cur]
        path.append([m,cur])
        cur = p
    path.append(sm)
    path.reverse()
    return path

def ast(sm='700134652',em='123456700')
