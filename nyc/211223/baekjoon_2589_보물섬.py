import sys
from collections import deque


def bfs(x, y, r, c):
    visited = [[False] * c for _ in range(r)]
    que = deque()
    que.append((x, y, 0))
    visited[x][y] = True
    count = 0
    while que:
        cur = que.popleft()
        count = max(count, cur[2])
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c or visited[nx][ny]:
                continue
            if board[nx][ny] == "W":
                continue
            que.append((nx, ny, cur[2]+1))
            visited[nx][ny] = True
    return count


def solution(r, c):
    answer = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'L':
                answer = max(answer, bfs(i, j, r, c))
    return answer


if __name__ == "__main__":
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    R, C = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
    print(solution(R, C))
