from collections import deque
import copy

n, m = map(int, input().split())


sea = [list(map(int, input().split())) for _ in range(n)]


flag = False


def melt(n, m, sea):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    sea_copy = copy.deepcopy(sea) 
    count = 0
    for i in range(n):
        for j in range(m):
            if sea[i][j] != 0: 
                water_count = 0
                for k in range(4): 
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m: 
                        if sea[nx][ny] == 0:
                            water_count += 1
                sea_copy[i][j] -= water_count 
                if sea_copy[i][j] < 0: sea_copy[i][j] = 0
                count += sea_copy[i][j]
    return count, sea_copy

def count_ice(n, m, r, c, sea, visited):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = deque()
    q.append([r, c])
    visited[r][c] = True

    while q:
        cr, cc = q.popleft()
        for dirs in range(4):
            nr = cr + dx[dirs]
            nc = cc + dy[dirs]
            if 0 <= nr < n and 0 <= nc < m: # 맵을 벗어나지 않으면
                if not visited[nr][nc] and sea[nr][nc] != 0:
                    # 방문한 적이 없고 바다가 아니면
                    visited[nr][nc] = True
                    q.append([nr, nc])

result = 0

while True:
    
    iceSize, sea = melt(n, m, sea)
    if iceSize == 0:
        break

    count = 0 
    visited = [[False]*m for _ in range(n)] 
    for i in range(n): 
        for j in range(m): 
            if not visited[i][j] and sea[i][j] != 0:
                count += 1
                count_ice(n, m, i, j, sea, visited)
    
    result += 1

    if count >= 2: 
        flag = True
        break

if flag:
    print(result)
else:
    print(0)



    

