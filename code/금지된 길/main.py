from time import time
from printer import printf
import heapq

def ecg(m,s,e,r):
    m = list(m)
    m[s],m[e] = m[e],m[s]
    info = [r,int(m[s])]
    return [''.join(m),info]

def aro(n):
    if n in ser:
        return ser[n]
    res=[]
    dy,dx=[-1,0,1,0],[0,1,0,-1]
    y,x=(n//sx)%sy,n%sx
    for i in range(4):
        ny,nx=y+dy[i],x+dx[i]
        if -1<ny<sy and -1<nx<sx:
            res.append(ny*sx+nx)
    ser[n]=res
    return res

def cs(m):
    res = []
    for i in [j for j in range(si) if m[j]!='0']:
        q = [i]
        r = {i:[i]}
        for cur in q:
            for j in aro(cur):
                if j in q or m[j]!='0':
                    continue
                q.append(j)
                r[j] = r[cur] + [j]
                res.append(ecg(m,j,i,r[j]))
    return res

def path(m,s,e):
    q=[[s]]
    v={s}
    for r in q:
        if r[-1] == e:
            return r
        for i in aro(r[-1]):
            if m[i-1]!='x' and i not in v:
                v.add(i)
                q.append(r + [i])

def H(m):
    ct = 0
    for i in range(si):
        if leaf[i] not in '0x':
            if m[i]==leaf[i]:
                ct-=5
    return ct

def bfs(m,*a):
    global res
    leaf, = a
    q = []
    mli = {m:[m]}
    st = {m:0}    
    ph = lambda c: heapq.heappush(q,(st[c]**[1,1,1][t]+H(c),c))
    ph(m)
    while 1:
        c = heapq.heappop(q)[1]
        if c==leaf:
            break
        for i,j in cs(c):
            if i not in mli:
                mli[i]=mli[c]+[j]
                st[i]=st[c]+1
                ph(i)
    res+=mli[c][1:]
    return c

def main(g,m,*a):
    global t,sy,sx,sz,si,fx,fxli,ser,res
    t=g
    sy,sx,sz = 3,3,1
    si = sy * sx
    fx = {i:0 for i in range(si)}
    fxli = lambda li,n: fx.update({i:n for i in li})
    ser = {}
    res = []
    leaf,=a
    m=bfs(m,leaf)
    return res

if __name__ == '__main__':
    t = 0
    if t == 0:
        m,leaf ='164730052', '713245006'
    ts = time()
    res = main(t,m,leaf)
    te = time() - ts
    print(res)
    print("{}step, idle {}s(DART-Studio {}m {}s) \n".format(len(res),round(te,3),int((te*250)//60),int((te*250)%60)))

