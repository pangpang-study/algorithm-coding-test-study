import sys
from collections import deque


def update_outer_air(x, y, n, m):
    que = deque()
    que.append((x, y))
    while que:
        cur = que.popleft()
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] != 0:
                continue
            board[nx][ny] = -1
            que.append((nx, ny))


def find_melting_cheese_pos(n, m):
    coords = []
    for i in range(n):
        for j in range(m):
            if board[i][j] != 1:
                continue
            count = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if board[nx][ny] == -1:
                    count += 1
            if count >= 2:
                coords.append((i, j))
    return coords


def melt(coords, n, m):
    for x, y in coords:
        board[x][y] = -1
        update_outer_air(x, y, n, m)


def solution(n, m):
    answer = 0
    update_outer_air(0, 0, n, m)
    while coords := find_melting_cheese_pos(n, m):
        melt(coords, n, m)
        answer += 1
    return answer


if __name__ == "__main__":
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    N, M = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(solution(N, M))
