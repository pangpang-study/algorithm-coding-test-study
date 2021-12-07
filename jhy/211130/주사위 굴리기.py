import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

commands = list(map(int, input().split()))
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)
# 가장 처음에 주사위의 값은 0
dice, temp = [0] * 6, [0] * 6
# 주사위의 현재 인덱스
direction = [
    (2, 0, 5, 3, 4, 1), # 동쪽
    (1, 5, 0, 3, 4, 2), # 서쪽
    (4, 1, 2, 0, 5, 3), # 북쪽
    (3, 1, 2, 5, 0, 4) # 남쪽
]
# 윗면 0, 동 1, 서 2, 북 3, 남 4
for command in commands:
    command -= 1
    x, y = x + dx[command], y + dy[command]
    if x < 0 or x >= n or y < 0 or y >= m:
        x, y = x - dx[command], y - dy[command]
        continue
    for idx in range(6):
        temp[idx] = dice[idx]
    for idx in range(6):
        dice[idx] = temp[direction[command][idx]]
    if board[x][y]:
        dice[5] = board[x][y]
        board[x][y] = 0
    else:
        board[x][y] = dice[5]
    
    print(dice[0])