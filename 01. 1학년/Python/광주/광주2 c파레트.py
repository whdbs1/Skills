from collections import deque

def aro(n):
    li = []
    if n-6 >= 0:
        li.append(n-6)
    if n+6 < 12:
        li.append(n+6)
    if n-3 >= 0:
        li.append(n-3)
    if n+3 < 12:
        li.append(n+3)
    if n%3 != 0:
        li.append(n-1)
    if n%3 != 2:
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
        for x,val in enumerate(cur):
            if val == 'X':
                print('x:',x)
                for ser in aro(x):
                    print(ser)
##                    if cur[ser] == '0' and 
##                    cm = (exc(cur,x,ser))
##                    if cm not in vst:
##                        par[cm] = [cur,[ser,x]]
##                        vst.add(cm)
##                        q.append(cm)
##
##    if em not in par and em != sm:
##        return None
##                            
##    path = []
##    cur = em
##    while cur != sm:
##        p, m = par[cur]
##        path.append([m,cur])
##        cur = p
##    path.append(sm)
##
##



def aro(x,y,f,n):
    li=[]
    #위
    if n-x*f >= 0:
        li.append(n-x*f)
    #아래
    if n+x*f < x*y*f:
        li.append(n+x*f)
    #상
    if n-x > '?':
        li.append(n-x)
    
    #하
    if n+x < x*y:
        li.append(n+x)
    #좌 
    if n%x != 0:
       li.append(n-1)
    #우 
    if n%x != x-1:
        li.append(n+1)
    print(a)
return path[::-1]
                
