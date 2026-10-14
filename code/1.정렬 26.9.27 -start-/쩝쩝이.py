import heapq

def ze(m):
    li = []
    for i, val in enumerate(m):
        if val == str(0):
            for x in (-3, 3, -1, 1):
                n = i + x
                if 0 <= n < 9 and (abs(x) == 3 or i//3 == n//3) and m[n] != '0':
                    s = list(m)
                    s[i], s[n] = s[n], s[i]
                    li.append(''.join(s))
    return li

def hg(sm,em):
    h = 0
    for i in range(9):
        if sm[i] != str(0):
            s = (i//3,i%3)
            e = (int(sm[i])//3,int(sm[i])%3)
            h += (abs(s[0]-e[0])+abs(s[1]-e[1]))
    return h

    
def main():
    sm,em = '730401562','123456700'
    ol = []
    cl = {}
    par = {}
    g = 0
    heapq.heappush(ol,(hg(sm,em)+g,g,sm))
    cl[sm] = g
    while ol:
        f,g,cur = heapq.heappop(ol)
        if cl[cur]<g:
            continue
        if cur == em:
            break
        ng = g+1
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
            
