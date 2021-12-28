import sys


def check_zero(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if board[nx][ny] == '0':
            return False
    return True               


def board_minus(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == '#':
            continue
        board[nx][ny] = str(int(board[nx][ny]) - 1)

def solution(n):
    if n <= 4:
        count = 0
    else:
        count = (n - 4) ** 2
    for i in range(1, n-1):
        if check_zero(1, i):
            count += 1
            board_minus(1, i)
        if check_zero(i, n-2):
            count += 1
            board_minus(i, n-2)
        if check_zero(n-2, i):
            count += 1
            board_minus(n-2, i)
        if check_zero(i, 1):
            count += 1
            board_minus(i, 1)
    print(count)


n = int(input())
board = []
for _ in range(n):
    board.append(list(map(str, input().rstrip())))

#상,하,좌,우,왼아래,왼위,오른아래,오른위
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, 1, -1, 1, -1]

solution(n)