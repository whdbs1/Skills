def srh(m,x,y):
    res = []
    for i in range(len(m)):
        if m[i] != '0':
            continue
        sy,sx = divmod(i,x)
        dy,dx = [1,0,-1,0],[0,1,0,-1]
        for j in range(4):
            y1,x1 = sy+dy[j],sx+dx[j]
            if -1<y1<y and -1<x1<x:
                c = y1*x+x1
                if m[c] == '0':
                    continue
                cm = list(m)
                cm[i],cm[c] = cm[c],cm[i]
                res.append(''.join(cm))
    return res

def hg(m,em,x):
    res = 0
    for i in range(len(m)):
        if m[i] != '0':
            j = em.index(m[i])
            sx,sy = (i//x, i%x)
            ex,ey = (j//x, j%x)
            res += abs(sx-ex) + abs(sy-ey)
    return res

def dfs(cur,em,vst):
    vst.append(cur)
    for cm in srh(cur,3,3):
        if cm not in vst:
            dfs(cm,'123456700',vst)
    return vst

print(dfs('123456070','123456700',[]))
            
