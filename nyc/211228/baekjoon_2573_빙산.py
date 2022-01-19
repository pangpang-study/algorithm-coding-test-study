import sys
from collections import deque


def bfs(x, y, n, m, visited):
    que = deque()
    que.append((x, y))
    visited[x][y] = True
    while que:
        cur = que.popleft()
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or sea[nx][ny] == 0 or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            que.append((nx, ny))


def seperated(n, m):
    count = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if sea[i][j] != 0 and not visited[i][j]:
                bfs(i, j, n, m, visited)
                count += 1
    if count == 0:
        print(0)
        exit(0)
    if count == 1:
        return True
    return False


def melt(n, m):
    coord = []
    for i in range(n):
        for j in range(m):
            if sea[i][j] == 0:
                continue

            count = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if sea[nx][ny] == 0:
                    count += 1
            coord.append((i, j, count))
    for x, y, c in coord:
        sea[x][y] = sea[x][y] - c if sea[x][y] >= c else 0


def solution(n, m):
    answer = 0
    while seperated(n, m):
        melt(n, m)
        answer += 1
    return answer


if __name__ == "__main__":
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    N, M = map(int, sys.stdin.readline().split())
    sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(solution(N, M))
