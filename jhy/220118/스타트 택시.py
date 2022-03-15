import sys
from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline


def isin(y,x):
    if -1<y<n:
        if -1<x<n: 
            return True
    return False


# 출발지와 도착지 거리 계산
def bfs():
    global taxi_pos, f
    sy, sx = taxi_pos[0] - 1, taxi_pos[1] - 1
    check = [[False for _ in range(n)] for _ in range(n)]
    table = [[INF for _ in range(n)] for _ in range(n)]
    q = deque([])
    table[sy][sx] = 0
    q.append([sy, sx])
    check[sy][sx] = True
    
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]

            if isin(ny, nx):
                if not check[ny][nx]:
                    check[ny][nx] = True
                    if arr[ny][nx] != 1:
                        table[ny][nx] = table[y][x] + 1
                        q.append([ny, nx])
    
    return table


# 택시와 가까운 손님을 찾는 함수
def find_guest():
    global arr, f, picked 
    table = bfs()
    pq = []

    for i in range(m):
        if not picked[i]:
            y, x = srcs[i][0] - 1, srcs[i][1] - 1
            dist = table[y][x]
            if f - dist >= 0:
                heappush(pq, [dist, y, x, i]) 

    if not pq: 
        return -1
    dist, _, _, guest_index = heappop(pq)
    f -= dist
    picked[guest_index] = True

    return guest_index


# 손님의 목적지까지 가는 함수
def go_dst(guest_index):
    global f
    table = bfs()
    y, x = dsts[guest_index][0] - 1, dsts[guest_index][1] - 1
    dist = table[y][x]
    if f - dist < 0: 
        return -1
    return dist


n, m, f = map(int, input().rstrip().split())
arr = [[] for i in range(n)]
INF = int(1e9)
d = [[1,0], [-1,0], [0,1], [0,-1]]

for i in range(n):
    x = list(map(int, input().rstrip().split()))
    arr[i] = x


taxi_pos = list(map(int, input().rstrip().split()))
srcs = [[] for i in range(m)]
dsts = [[] for i in range(m)]

for i in range(m):
    src_y, src_x, dst_y, dst_x = map(int, input().rstrip().split())
    srcs[i] = [src_y, src_x]
    dsts[i] = [dst_y, dst_x]

picked = [False for _ in range(m)]

# 실행코드
ok = True
cnt = m
while cnt:
    guest_index = find_guest()
    if guest_index == -1:
        ok = False
        break
    taxi_pos = srcs[guest_index]
    dist = go_dst(guest_index)
    if dist == -1:
        ok = False
        break
    f += dist
    taxi_pos = dsts[guest_index]
    cnt -= 1

if ok: 
    print(f)
else: 
    print(-1)