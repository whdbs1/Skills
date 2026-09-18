from collections import deque

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


def ck(cm,em,ser):
    if cm[ser] == em[ser]:
        return cm
    

def bfs():    
    sm = '000103020'
    em = '123000000'

    q = deque([sm])
    vst, par = {sm},{}               

    while q:
        cur = q.popleft()

        if cur == em:
            break

##        for n in [i for i in range(9) if cur[i] != str(0)]:
        for i, val in enumerate(cur):
            if val != str(0):
                for ser in aro(i):
                    if cur[ser] == str(0):
                        cm = exc(cur,i,ser)
                        if cm[ser] == em[ser]:
                            '현 cm을 리스트에 중복되는 값이 전 cm보다 많으면 현 cm 사용'
                            
                            if cm not in vst:
                                par[cm] = [cur,[ser,i]]
                                vst.add(cm)
                                q.append(cm)
                        
        print(cur)
        print(par)

                        

                        

                                              
print(bfs())
                        
        
                
                

