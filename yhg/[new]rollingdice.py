import sys
from collections import deque
input = sys.stdin.readline

n , m , x, y, k  = map(int, input().split())

board = []

for i in range(n):
    board.append(list(map(int ,input().split())))

dice = [0,0,0,0,0,0]
order = deque(map(int, input().split()))

while order:
    direction = order.popleft()
    
    if direction == 1:
        y += 1
        
        if y >= m:
            y-=1
            continue

        dice[1] , dice[4] , dice[3] , dice[5] , = dice[4] , dice[3], dice[5], dice[1]
    
    if direction == 2:
        y -= 1
        
        if y < 0:
            y+=1
            continue
        
        dice[1] , dice[4] , dice[3] , dice[5] , = dice[5] , dice[1], dice[4], dice[3]

    if direction == 3:
        x -= 1
        
        if x < 0:
            x+=1
            continue

        dice[1] ,dice[2],dice[3],dice[0]  = dice[0] ,dice[1],dice[2], dice[3]

    if direction == 4:
        x += 1
        
        if x >= n:
            x-=1
            continue

        dice[0] ,dice[1],dice[2],dice[3]  = dice[1] ,dice[2],dice[3], dice[0]


    if board[x][y] == 0 :
        board[x][y] = dice[3]

    else:
        dice[3] = board[x][y]
        board[x][y] = 0

    print(dice[1])