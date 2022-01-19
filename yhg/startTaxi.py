import sys
from collections import deque
import heapq
input = sys.stdin.readline

def find_human(taxi_x, taxi_y):
    queue = deque()
    queue.append([taxi_x,taxi_y])
    visited = [[0] * n for _ in range(n)]
    human_list = []
    min_dis = 1e9
    while queue:
        x, y = queue.popleft()
        if visited[x][y] > min_dis:
            break

        if [x,y] in start_List:
            min_dis = visited[x][y]
            heapq.heappush(human_list,[visited[x][y],x,y])
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < n and 0<= ny < n and visited[nx][ny] == 0 and board[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx,ny])
    if len(human_list) > 0:
        return human_list[0]
    else:
        return -1, -1, -1
def move_to_destianion(desti_x , desti_y , end_posi):
    queue = deque()
    queue.append([desti_x , desti_y])
    visited = [[0] * n for _ in range(n)]
    while queue:
        x, y = queue.popleft()
        if [x,y] == end_posi:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n  and 0<= ny < n and board[nx][ny] != 1 and visited[nx][ny] == 0 :
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
    return visited[x][y], x, y
n,m,oil = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

taxi_x, taxi_y = map(int, input().split())
taxi_x-=1
taxi_y-=1

start_List = []
end_List = []

for i in range(m):
    start_x, start_y , end_x , end_y = map(int, input().split())
    start_List.append([start_x-1 , start_y-1])
    end_List.append([end_x-1, end_y-1])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(m):
    find_oil , human_x, human_y = find_human(taxi_x,taxi_y)
    if find_oil == -1 or oil - find_oil <0:
        oil = -1
        break
    oil -= find_oil
    idx = start_List.index([human_x, human_y])
    start_List[idx] = [-1,-1]
    move_oil , desti_x , desti_y = move_to_destianion(human_x , human_y , end_List[idx])

    if oil - move_oil < 0 or [desti_x , desti_y] != end_List[idx]:
        oil = -1
        break
    oil += move_oil
    taxi_x = desti_x
    taxi_y = desti_y

print(oil)
