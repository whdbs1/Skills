from collections import deque

def arrow(x,y,n):
    a=[]
    if n+x < x*y:
        a.append(n+x)
    if n-x > 0:
        a.append(n-x)
    if n%x != 0:
       a.append(n-1)
    if n%x != x-1:
        a.append(n+1)
    print(a)


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
