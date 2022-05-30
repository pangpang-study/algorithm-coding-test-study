import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start, l, r, visited, n):
    q = deque()
    q.append(start)
    population = graph[start[0]][start[1]]
    result = []
    flag = False
    while q:
        now = q.popleft()
        result.append(now)
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            # 인덱스 범위 밖
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 이미 연합됨
            if visited[nx][ny]:
                continue
            # 만약 연합할 수 있는 도시라면
            dist = abs(graph[now[0]][now[1]] - graph[nx][ny])
            if l <= dist <= r:
                visited[nx][ny] = True
                q.append((nx, ny))
                population += graph[nx][ny]
                flag = True     # 연합을 수행했다는 것.

    answer = population // len(result)
    for res in result:
        graph[res[0]][res[1]] = answer
    return visited, flag


def solution(n, l, r):
    visited = [[False]*n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                visited, f = bfs((i, j), l, r, visited, n)
                if f:
                    flag = True
    return flag


if __name__ == "__main__":
    N, L, R = map(int, sys.stdin.readline().rstrip().split())
    graph = list()
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    count = 0
    while True:    # O(2000)
        if solution(N, L, R):       # O(2500)
            count += 1
        else:
            break
    print(count)
