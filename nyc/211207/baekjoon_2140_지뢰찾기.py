import sys


def can_put_mine(x, y, n):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if board[nx][ny] == '0':
            return False
    return True


def decrease_border(x, y, n):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == '#':
            continue
        board[nx][ny] = str(int(board[nx][ny]) - 1)


def solution(n):
    count = 0 if n <= 4 else (n - 4) ** 2
    for i in range(1, n-1):
        if can_put_mine(1, i, n):
            count += 1
            decrease_border(1, i, n)
        if can_put_mine(i, n-2, n):
            count += 1
            decrease_border(i, n-2, n)
        if can_put_mine(n-2, i, n):
            count += 1
            decrease_border(n-2, i, n)
        if can_put_mine(i, 1, n):
            count += 1
            decrease_border(i, 1, n)
    return count


if __name__ == "__main__":
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    N = int(sys.stdin.readline().rstrip())
    board = []
    for _ in range(N):
        board.append(list(sys.stdin.readline().rstrip()))
    print(solution(N))
