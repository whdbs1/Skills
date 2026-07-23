import random
from collections import deque

'상하좌우'
def ch(m1,m2,n):
    a = []

    '상'
    if n < m1 * (m2 - 1):
        a.append(n+m1)

    '하'
    if n >= m1:
        a.append(n-m1)

    '좌'
    if n%m1 != 0:
        a.append(n-1)

    '우'
    if n%m1 != m1-1:
        a.append(n+1)

    return a


'시작맵'
array = '624153000'

print(array[0:3])
print(array[3:6])
print(array[6:9])
print()

'마무리'
stop = '123456000'

'deque에 시작 맵 넣기'
q = deque()
q.append(array)

'방문한 곳'
visited = set()
visited.add(array)

'길'
road = {}

'움직인 팩'
moved = {}

'정렬 시작'
while q:

    now = q.popleft()

    '정렬이 되면 멈추기'
    if now == stop:
        break

    '0이 있는 자리 찾기'
    ser = [i for i, value in enumerate(now) if value == '0']

    for s in ser:

        '0들의 상하좌우'
        for j in ch(3,3,s):

            '0이면 넘어가고'
            if now[j] == '0':
                continue

            num = now[j]

            '문자열을 리스트로 바꾸는거'
            ln = list(now)

            '0근처에 있는 숫자랑 0이랑 바꿔보기'
            ln[s], ln[j] = ln[j], ln[s]

            '하나로 만들기 ex) [0,0,0] -> 000'
            new = ''.join(ln)

            '방문 안 했으면'
            if new not in visited:

                '방문기록에 추가'
                visited.add(new)
                q.append(new)

                '000처럼 하나로 만든게 리스트형태로 바꾸기'
                road[new] = now
                '하나로 된거 무슨 숫자가 지나간지 저장'
                moved[new] = num


'이제 역추적'
if stop in visited:
    
    path = []

    cur = stop

    while cur != ''.join(array):
        path.append(cur)
        cur = road[cur]

    path.append(''.join(array))

    path.reverse()

    for i in range(len(path)):

        state = path[i]

        print(state[0:3])
        print(state[3:6])
        print(state[6:9])

        if i > 0:
            print("움직인 숫자 :", moved[state])

        print()

else:
    print("불가능")
                

           
    
