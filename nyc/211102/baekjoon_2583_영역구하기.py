import sys
from collections import deque


def fill(x1, y1, x2, y2):
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = False


def bfs(sx, sy, n, m):
    que = deque()
    visited[sx][sy] = True
    que.append((sx, sy))
    count = 1
    while que:
        x, y = que.popleft()
        for nxt in range(4):
            nx = x + dx[nxt]
            ny = y + dy[nxt]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] or not board[nx][ny]:
                continue
            visited[nx][ny] = True
            que.append((nx, ny))
            count += 1
    return count


if __name__ == "__main__":
    M, N, K = map(int, sys.stdin.readline().split())
    board = [[True] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for _ in range(K):
        n1, m1, n2, m2 = map(int, sys.stdin.readline().split())
        fill(n1, m1, n2, m2)

    answer = 0
    space = []
    for i in range(N):
        for j in range(M):
            if board[i][j] and not visited[i][j]:
                space.append(bfs(i, j, N, M))
                answer += 1
    space.sort()
    print(answer)
    print(" ".join(map(str, space)))
