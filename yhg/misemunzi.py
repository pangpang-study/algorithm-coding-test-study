import sys
from collections import deque
input = sys.stdin.readline


R,C,T = map(int, input().split())


def hwack():
    global board
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    zeroBase_board = [[0]* C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0 and board[i][j] != -1 and board[i][j] >= 5:
                h_count = 0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
            
                    if 0<= nx < R and 0<= ny < C :
                        if board[nx][ny] != -1 :
                            zeroBase_board[nx][ny] += board[i][j] // 5
                            h_count +=1
                if h_count != 0 :
                    board[i][j] -= (board[i][j] // 5)* h_count
    for i in range(R):
        for j in range(C):
            board[i][j] += zeroBase_board[i][j]
    return 


def airup():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = air_posi[0], 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == air_posi[0] and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        board[x][y], before = before, board[x][y]
        x = nx
        y = ny


def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = air_posi[1], 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == air_posi[1] and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        board[x][y], before = before, board[x][y]
        x = nx
        y = ny        

board =[]
munzi_pozi = deque()

air_posi = []
for i in range(R):
    b_input = list(map(int, input().split()))

    for j in range(C):
        if b_input[j] >= 5:
            munzi_pozi.append([i,j,b_input[j]])

    if b_input[0] == -1:
        air_posi.append(i)
    board.append(b_input)

for i in range(T):
    hwack()
    airup()
    air_down()
    
result =0 
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            result += board[i][j]

print(result)
