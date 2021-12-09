import sys


def move_down(d1, d2, d3, d4, d5, d6):
    return d5, d1, d3, d4, d6, d2


def move_up(d1, d2, d3, d4, d5, d6):
    return d2, d6, d3, d4, d1, d5


def move_left(d1, d2, d3, d4, d5, d6):
    return d4, d2, d1, d6, d5, d3


def move_right(d1, d2, d3, d4, d5, d6):
    return d3, d2, d6, d1, d5, d4


def solution(x, y, n, m):
    d1, d2, d3, d4, d5, d6 = 0, 0, 0, 0, 0, 0
    for command in commands:
        nx = x + dx[command]
        ny = y + dy[command]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if command == 1:
            d1, d2, d3, d4, d5, d6 = move_right(d1, d2, d3, d4, d5, d6)
        elif command == 2:
            d1, d2, d3, d4, d5, d6 = move_left(d1, d2, d3, d4, d5, d6)
        elif command == 3:
            d1, d2, d3, d4, d5, d6 = move_up(d1, d2, d3, d4, d5, d6)
        elif command == 4:
            d1, d2, d3, d4, d5, d6 = move_down(d1, d2, d3, d4, d5, d6)

        if board[nx][ny] == 0:
            board[nx][ny] = d1
        else:
            d1, board[nx][ny] = board[nx][ny], 0
        x, y = nx, ny
        print(d6)


if __name__ == "__main__":
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    N, M, X, Y, _ = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    commands = list(map(int, sys.stdin.readline().split()))
    solution(X, Y, N, M)

