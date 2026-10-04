import heapq

def exc(m,s,e):
    m = list(m)
    m[s],m[e] = m[e],m[s]
    return [''.join(m),[e,s],int(m[s])]

def aro(n):
    res = []
    x, y = divmod(n,mx)
    x1, y1= [0, 1, 0, -1], [1, 0,-1,0]
    for i in range(4):
        x2 = x + x1[i]
        y2 = y + y1[i]
        if 0 <= x2 < 3 and 0 <= y2 < 3:
            res.append(x2*mx+y2)
    return res

def f(m,f):
    for fd in [i for i in range(len(m)) if m[i] == str(f)]:
        return (fd//mx,fd%mx)
##    return divmod(m.index(str(f)), mx)

def cm(cur):
    cm = []
    for i in range(len(cur)):
        if cur[i] != str(0):
            for ser in aro(i):
                if cur[ser] == str(0):
                    cm.append(exc(cur,ser,i))
    return cm
    


def ast():    
    ol = {sm:0}
    h = [sm]
    p = mx*my-1
    
    while h:
        cur = heapq.heappop(h)
        if cur == em:
            break
        mt = lambda a,b:abs(a[0] - b[0]) + abs(a[1] - b[1])
        for c in cm(cur):
            hur = mt(f(c[0],c[2]),f(em,c[2]))
            if hur == 1:
                heapq.heappush(h,c[0])
                print(h)
                
            
sm='000010000'
em='100000000'
mx,my,mf = 3,3,1        

print(ast())




























 














