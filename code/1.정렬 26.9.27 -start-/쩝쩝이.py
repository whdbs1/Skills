import heapq

def ze(m):
    li = []
    for i, val in enumerate(m):
        if val != '0':
            continue
        for x in (-4, 4, -1, 1):
            n = i + x
            if 0 <= n < 18 and (abs(x) == 4 or i//4 == n//4) and m[n] != '0':
                s = list(m)
                s[i], s[n] = s[n], s[i]
                li.append(''.join(s))
    return li

def hg(sm,em):
    h = 0
    for i in range(9):
        if sm[i] != str(0):
            s = (i//4,i%4)
            e = (int(sm[i])//4,int(sm[i])%4)
            h += (abs(s[0]-e[0])+abs(s[1]-e[1]))
    return h

    
def main():
    sm,em = '704350126','123456700'
    ol = [(hg(sm,em),0,sm)]
    cl = {sm:0}
    
    while ol:
        f,g,cur = heapq.heappop(ol)
        if cl[cur]!=g:
            continue
        if cur == em:
            return g
        ng = g+1
        h = f-g
        for cm in ze(cur):
            if cm not in cl or ng < cl[cm]:
                cl[cm] = ng
                par[cm] = cur
                heapq.heappush(ol,(hg(cm,em)+ng,ng,cm))
    path = []
    cur = em
    while cur != sm:
        path.append(cur)
        cur = par[cur]
    path.append(sm)
    path.reverse()
    return path
            
