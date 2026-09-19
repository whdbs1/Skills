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

def bfs():    
    sm = '0000200013'
    em = '123000000'

    q = deque([sm])
    vst, par = {sm},{}               

    kcm = []
    while q:
        cur = q.popleft()
        if cur == em:
            break
        for one in [i for i in range(9) if cur[i] != str(0)]:
            for ze in [i for i in aro(one) if cur[i] == str(0)]:
                cm = exc(cur,one,ze)
                if cm[ze] == em[ze]:
                    cur = cm
                    
                    if cm not in vst:
                        par[cm] = [cur]
                        vst.add(cm),q.append(cm)
                else:
                    if cm not in vst:
                        par[cm] = [cur]
                        vst.add(cm),q.append(cm)
        print(par)
                
                
'''
조건문
if cm[ze] == em[em]:
    print(ze)
'''
##        for n in [i for i in range(9) if cur[i] != str(0)]:
##        for i, val in enumerate(cur):
##            if val != str(0):
##                for ser in aro(i):
##                    if cur[ser] == str(0):
##                        cm = exc(cur,i,ser)
##                        print('i:', i)
##                        print(cm,':',cm[i],' ',em,':',em[i])
##                        if cm[ser] == em[ser]:
##                            if cm not in vst:
##                                par[cm] = [cur,[ser,i]]
##                                vst.add(cm)
##                                q.append(cm)
##        print(cur)




'''
현재 맵보다 탐색맵의 맞는 ser의 개수가 더적으면 건너뛴다
if cm[ser] == em[ser] < cur[ser] == em[ser]:
    continue
'''


##                        if cm[ser] == em[ser]:
##                            kcm.append(cm)
##                            if kcm == 1:
##                                break
##                        else:
##                            if cm not in vst:
##                                par[cm] = [cur,[ser,i]]
##                                vst.add(cm)
##                                q.append(cm)
        
    
print(bfs())
    
