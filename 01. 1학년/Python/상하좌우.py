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
