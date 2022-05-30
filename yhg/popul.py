import sys
from collections import deque
input = sys.stdin.readline
 
 
dy = [1, -1, 0, 0] 
dx = [0, 0, 1, -1]
 
 
def bfs(y, x):
    global visisted, m
    queue = deque()
    queue.append((y, x))
    sum_val = m[y][x]
    visisted[y][x] = 1
    pos = [(y, x)]
 
    while queue:
        y, x = queue.popleft()
 
        for my, mx in zip(dy, dx):
            ny = y + my
            nx = x + mx
            if 0 <= ny < N and 0 <= nx < N and not visisted[ny][nx]:
                if L <= abs(m[ny][nx] - m[y][x]) <= R:
                    visisted[ny][nx] = 1
                    sum_val += m[ny][nx]
                    queue.append((ny, nx))
                    pos.append((ny, nx))
 
    if len(pos) > 1:  # exist group
        cnt = len(pos)
        mean = sum_val // cnt
        for i in range(cnt):
            y, x = pos[i] 
            m[y][x] = mean
            q.append((y, x))
        return 0
    else:
        return 1
 
 
def check(y, x):
    for my, mx in zip(dy, dx):
        ny = y + my
        nx = x + mx
        if 0 <= ny < N and 0 <= nx < N:
            if L <= abs(m[ny][nx] - m[y][x]) <= R:
                return 0
    return 1
 
 
N, L, R = map(int, input().split())
m = [[] for _ in range(N)]
q = deque()
for i in range(N):
    m[i] = list(map(int, input().split()))
    for j in range(N):
        q.append((i, j))
 
cnt = 0
flag = False 
 
while not flag:
    visisted = [[0] * N for _ in range(N)]
    flag = True
    size = len(q)
    for _ in range(size):
        y, x = q.popleft()
        if visisted[y][x] or check(y, x):
            continue
        if not bfs(y, x):
            flag = False 
    if not flag:
        cnt += 1
print(cnt)