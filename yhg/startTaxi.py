import sys
from collections import deque
import copy
input = sys.stdin.readline

dx = [0,-1,0,0,1]
dy = [0,0,-1,1,0]
def find_Human(x,y):
    queue = deque()
    queue.append([x,y])
    distance = [[1e9] * n for _ in range(n)]
    distance[x][y] = 0
    human_list = []
    if board[x][y] != 0 and board[x][y] != 1:
        return 0, x,y,board[x][y]
    while queue:
        x , y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0 <= ny < n and distance[nx][ny] == 1e9:
                if board[nx][ny] == 1:
                    distance[nx][ny] = 0
                elif board[nx][ny] == 0:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append([nx, ny])
                else:
                    distance[nx][ny] = distance[x][y] + 1
                    human_list.append([distance[x][y] + 1 , nx, ny , board[nx][ny]])
                    
    sorted(human_list , key = lambda x : (x[0] , x[1] , x[2])) 
    if len(human_list) == 0:
        return 0,0,0,0
    else:
        return human_list[0]

def move_to_destinaion(index, x, y):
    queue = deque()
    queue.append([x,y])
    distance = [[1e9] * n for _ in range(n)]
    distance[x][y] = 0
    
    while queue:
        x , y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0 <= ny < n and distance[nx][ny] == 1e9:
                if desti_board[nx][ny] == 1:
                    distance[nx][ny] = 0
                else:
                    if desti_board[nx][ny] == index:
                        return distance[x][y] + 1 , nx, ny
                    else:
                        distance[nx][ny] = distance[x][y] + 1
                        queue.append([nx,ny])
    
    return -1,-1,-1

n, m, oil = map(int, input().split())

board = []


for i in range(n):
    board.append(list(map(int,input().split())))

taxi_x , taxi_y = map(int ,input().split())
taxi_x -=1
taxi_y -=1
info_index = -1

desti_board = copy.deepcopy(board)
for i in range(m):
    start_x, start_y, end_x , end_y = map(int, input().split())
    board[start_x-1][start_y-1] =  info_index
    desti_board[end_x-1][end_y-1] = info_index
    info_index -= 1

for i in range(m):
    find_oil , new_x, new_y , index_num = find_Human(taxi_x,taxi_y)
    if index_num == 0 :
        print(-1)
        exit()
    board[new_x][new_y] = 0
#사람 찾는데 기름을 초과해서 사용했을 때
    if find_oil >= oil :
        print(-1)
        exit()
#사람 찾는데 기름이 남았을 떄 
    elif find_oil < oil:
        oil -= find_oil
        move_oli , moved_x , moved_y = move_to_destinaion(index_num , new_x, new_y)
        if move_oli == -1:
            print(-1)
            exit()
        desti_board[moved_x][moved_y] = 0
        #도착지 까지 갔을 때 기름을 초과해서 사용했을 떄 
        if move_oli > oil:
            print(-1)
            exit()
        #도착지 까지 갔을때 기름이 남았을 떄 
        elif move_oli < oil:
            oil += move_oli

        #도착지 까지 갔을 때 기름이 0일때
        else:
            if i == m-1:
                oil += move_oli
            else:
                print(-1)
                exit()
    taxi_x = moved_x
    taxi_y = moved_y

print(oil)
