from collections import deque

def aro(x,y,f,n):
    li=[]
    if n-x*y >= 0:
        li.append(n-x*y)
    if n+x*y < x*y*f:
        li.append(n+x*y)
    if (n-x)//(x*y) == n//(x*y):
        li.append(n-x)    
    if (n+x)//(x*y) == n//(x*y):
        li.append(n+x)
    if n%x != 0:
       li.append(n-1)
    if n%x != x-1:
        li.append(n+1)
    return li             

def exc(m,s,e):
    m = list(m)
    m[s],m[e] = m[e],m[s]
    m = ''.join(m)
    return m

def array():
    sm,em= '362415X000X0','32615400XX00'
    q = deque([sm])
    vst,par= {sm},{}
    while q:
        cur = q.popleft()
        if cur == em:
            break
        for x,val in enumerate(cur):
            if val == 'X':
                for ser in aro(3,2,2,x):
                    if (cur[ser] == str(0) and not (ser-6 == x or ser+6 == x)) or (ser-6 == x or ser+6 == x):     
                        cm = (exc(cur,x,ser))
                        if cm not in vst:
                            par[cm] = [cur,[x,ser]]
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

    return path[::-1]

print(array())

내가 X만 바꿀수 있는걸 봐서 그런가 봄




