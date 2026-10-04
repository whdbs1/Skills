def arrow(n):   #2차원 좌표
    res = []
    x, y = divmod(n,3)
    x1, y1= [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(4):
        x2 = x + x1[i]
        y2 = y + y1[i]
        if 0 <= x2 < 3 and 0 <= y2 < 3:
            res.append((x2, y2))
    return res

def arrow(x,y,n): # 전체 맵 상하좌우
    li = []
    if n-x >= 0:
        li.append(n-x)
    if n+x < x*y:
        li.append(n+x)
    if n%x != 0:
        li.append(n-1)
    if n% x != y-1:
        li.append(n+1)
    return li

def arrow(n):  # 3x3 상하좌우
    li = []
    if n-3 >= 0:
        li.append(n-3)        
    if n+3 < 9:
        li.append(n+3)
    if n%3 != 0:
        li.append(n-1)
    if n%3 != 2:
        li.append(n+1)
    return li

def arrow(n):   # 짧은코드
    li = list()
    for pm in [-3,+3,-1,+1]:
        if 0 <= n+pm < 9 and (abs(pm) == 3 or n // 3 == (n + pm) // 3):
            li.append(n+pm)
    return li

def aro(x,y,f,n,w=0): # 상하좌우 위아래
    li=[]
    if n-x*y >= 0:
        if w == True:
            li.append(n-x*y)
    if n+x*y < x*y*f:
        if w == True:
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
