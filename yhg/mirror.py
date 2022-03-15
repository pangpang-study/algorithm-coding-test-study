import sys
from collections import deque
input = sys.stdin.readline


n = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

board = []
posi = []
for i in range(n):
    input_list = list(input().rstrip())
    if "#" in input_list:
        posi.append([i , input_list.index("#")])

    board.append(input_list)

visited = [[1e9] * n for _ in range(n)]

def starting (board , posi):
    start_x, start_y = posi[-1]
    visited[start_x][start_y] = 0 
    posi.pop()
    queue = deque()
    for i in range(4):
        nx = start_x + dx[i]
        ny = start_y + dy[i]

        if 0 <= nx < n and 0 <=  ny < n and  board[nx][ny] == ".":
            queue.append([start_x , start_y , i , 0])

    while queue:
        x , y , direction , mirror = queue.popleft()
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < n and 0 <=  ny < n :
            if board[nx][ny] == "." and visited[nx][ny] >= mirror:
                queue.append([nx , ny , direction, mirror])
                visited[nx][ny] = mirror
            elif board[nx][ny] == "!" and visited[nx][ny] >= mirror:
            
                if direction == 0 or direction == 2:
                    queue.append([nx , ny , 3, mirror + 1])
                    queue.append([nx, ny , 1, mirror + 1])
                else:
                    queue.append([nx , ny , 0, mirror + 1])
                    queue.append([nx, ny , 2, mirror + 1])
                visited[nx][ny]  =  mirror + 1
            elif board[nx][ny] == "#":
                visited[nx][ny] = min(visited[nx][ny] , mirror)
    return visited[posi[0][0]][posi[0][1]]

print(starting(board , posi))







