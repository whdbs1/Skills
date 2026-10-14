
import heapq
import random
import time

em = '123456700'
N = 1000

aro = [
    tuple(j for j in (i-3, i+3, i-1, i+1)
          if 0 <= j < 9 and (abs(i-j) == 3 or i//3 == j//3))
    for i in range(9)
]

pos = {v: i for i, v in enumerate(em) if v != '0'}
dst = {
    v: [abs(i//3-pos[v]//3) + abs(i%3-pos[v]%3)
        for i in range(9)]
    for v in pos
}

def hg(m):
    return sum(dst[v][i] for i, v in enumerate(m) if v != '0')

def ze(m, h):
    for i, v in enumerate(m):
        if v != '0':
            continue
        for n in aro[i]:
            t = m[n]
            if t == '0':
                continue
            nh = h - dst[t][n] + dst[t][i]
            s = list(m)
            s[i], s[n] = s[n], s[i]
            yield ''.join(s), nh

def astar(sm):
    ol = [(hg(sm), 0, sm)]
    cl = {sm: 0}

    while ol:
        f, g, cur = heapq.heappop(ol)

        if cl[cur] != g:
            continue
        if cur == em:
            return g

        ng = g + 1
        h = f - g

        for cm, nh in ze(cur, h):
            if ng < cl.get(cm, float('inf')):
                cl[cm] = ng
                heapq.heappush(ol, (ng + nh, ng, cm))

    return -1

def random_map():
    m = list(em)
    prev = -1

    for _ in range(40):
        z = [i for i, v in enumerate(m) if v == '0']
        moves = [
            (i, n)
            for i in z
            for n in aro[i]
            if m[n] != '0' and n != prev
        ]

        i, n = random.choice(moves)
        m[i], m[n] = m[n], m[i]
        prev = i

    return ''.join(m)

total = 0
longest = 0
shortest = float('inf')
start = time.perf_counter()

for i in range(1, N + 1):
    sm = random_map()

    t = time.perf_counter()
    g = astar(sm)
    elapsed = time.perf_counter() - t

    total += elapsed

    if g > longest:
        longest = g
    if g < shortest:
        shortest = g

    print('{} | 맵: {} | 이동: {} | 탐색시간: {:.6f}초'.format(
        i, sm, g, elapsed
    ))

end = time.perf_counter()

print('\n========== 최종 결과 ==========')
print('총 실행 횟수: {}'.format(N))
print('평균 탐색시간: {:.6f}초'.format(total / N))
print('최대 이동 횟수: {}'.format(longest))
print('최소 이동 횟수: {}'.format(shortest))
print('전체 실행시간: {:.2f}초'.format(end - start))
print('================================')

