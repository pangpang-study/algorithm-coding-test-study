import sys
from collections import deque


def bfs(x, y, value, n, m):
    global visited
    que = deque()
    que.append((x, y))
    visited[x][y] = True
    flag = True
    while que:
        cur = que.popleft()
        for i in range(8):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if farm[nx][ny] > value:
                flag = False
            if visited[nx][ny]:
                continue
            if farm[nx][ny] == value:
                visited[nx][ny] = True
                que.append((nx, ny))
    if flag:
        return 1
    return 0


def solution(n, m):
    global visited
    answer = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            answer += bfs(i, j, farm[i][j], n, m)
    return answer


if __name__ == "__main__":
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    N, M = map(int, sys.stdin.readline().split())
    farm = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    print(solution(N, M))
