import random
import time
from collections import deque

##list(map(int, input().split()))

def pos(n):
    trans(n,[40,0,0,0,0,0])

def ch(n):
    return(n//3, n%3)

def ch(n):
    return(divmod(n,3))

def arrow(x,y,n):
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

def arrow1(n):    
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

def arrow2(n):
    x, y = ch(n)

    x1 = [-1, 1, 0, 0]
    y1 = [0, 0, -1, 1]

    li = []

    for i in range(4):
        x2 = x + x1[i]
        y2 = y + y1[i]

        if 0 <= x2 < 3 and 0 <= y2 < 3:
            li.append((x2, y2))

    return li

def arrow3(n):
    li = list()
    for pm in [-3,+3,-1,+1]:
        if 0 <= n+pm < 9 and (abs(pm) == 3 or n // 3 == (n + pm) // 3):
            li.append(n+pm)
    return li

def spr(n):
    A = [0] * 9
    A[n] = 1
    
    for e in range(5):
        for i, value in enumerate(A):
            if value == 1+e:
                for s in arrow1(i):
                    if A[s] == 0:
                        A[s] = 2+e
##def spr2(n):
##    def spr(n):
##    li = [0]*9
##    li[n] = 1
##
##    for e in range(5):        
##        for i in range(9):
##            if li[i] == 1+e:
##                for a in arrow(i):
##                    if li[a] == 0:
##                        li[a] = 2+e
##    return lst(li)

def bfs(start, end):
    q = deque([[start, [start]]])
    visit = set([start])

    while q:
        node, route = q.popleft()
        if node == end:
            return route 
        
        for next_node in arrow1(node):
            if next_node not in visit:
                visit.add(next_node)
                q.append([next_node, route + [next_node]])

def lst(li):
    print(li[0:3])
    print(li[3:6])       
    print(li[6:9])

def ch(m,s,e):
    m = list(m)
    m[s],m[e] = m[e],m[s]
    return ''.join(m)


start_time = time.perf_counter()

from collections import deque, defaultdict

from collections import deque, defaultdict

def array():
    leaf = '123456780'
    start = '134608725'

    q = deque([start])
    visit = {start}
    parent = {}

    # BFS
    while q:
        cur = q.popleft()

        if cur == leaf:
            break

        zero = cur.index('0')

        for nxt_zero in arrow1(zero):
            if cur[nxt_zero] != '0':
                nxt = ch(cur, zero, nxt_zero)

                if nxt not in visit:
                    visit.add(nxt)
                    parent[nxt] = cur
                    q.append(nxt)

    # 경로 복원 (시작 -> 목표)
    path = []
    while True:
        path.append(cur)
        if cur == start:
            break
        cur = parent[cur]

    path.reverse()

    # 경로 출력
    print("=== 경로 ===")
    for p in path:
        print(p[:3])
        print(p[3:6])
        print(p[6:])
        print()

    # 움직인 팩 순서 출력
    print("=== 움직인 팩 순서 ===")
    for before, after in zip(path, path[1:]):
        zero_before = before.index('0')
        zero_after = after.index('0')

        # 0과 자리를 바꾼 숫자
        moved = before[zero_after]

        print(moved)

    # 숫자별 방문 위치(중복 포함)
    step = defaultdict(list)

    for p in path:
        for i, value in enumerate(p):
            if value != '0':
                step[value].append(i)

    step = [[k, v] for k, v in sorted(step.items())]

    return stepprint(array())
end_time = time.perf_counter()
result = round(end_time - start_time, 4)
print("실행 시간:", result, "초")

