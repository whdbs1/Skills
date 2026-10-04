import heapq
import time

def exc(m,s,e):
    m = list(m)
    m[s],m[e] = m[e],m[s]
    return ''.join(m)

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

def f(m,f):
    return divmod(m.index(str(f)), mx)

def cm(cur):
    cm = []
    for i, val in enumerate(cur):
        if val != str(0):
            for ser in aro(i):
                if cur[ser] == str(0):
                    cm.append([exc(cur,i,ser),[ser,i]])
    return cm
def ast():    
    ol = {sm:0}
    h = [sm]
    

    while h:
        cur = heapq.heappop(h)
        if cur == em:
            break
        
        mt = lambda a,b: abs(a[0] - b[0]) + abs(a[1] - b[1])
        res = mt(divmod(cm(cur)[1][0],mx),f(em,cm(cur)[1][0]))
        print(res)
        
                        
                        
                            
##                        ol[i] = cm
##                        hapq.heappush(h,cm)
                                
sm='000010000'
em='100000000'

mx,my,mf= 3,3,2                             
                        
st = time.time()
print(ast())
et = time.time()
res = et - st


print("실행 시간: {:.5f}초".format(res))





