import sys
input = sys.stdin.readline
import copy
n = int(input())
'''
positions = []

result = 0

for i in range(n):
    start_x , start_y , direction , generation = map(int, input().split())
    d_positions = []
    d_positions.append([start_y,start_x])
    if direction == 0 :
        d_positions.append([start_y,start_x+1])
    elif direction == 1:
        d_positions.append([start_y-1,start_x])
    elif direction == 2:
        d_positions.append([start_y,start_x-1])
    elif direction == 3:
        d_positions.append([start_y+1,start_x])

    
    for i in range(generation):
        edge = d_positions[-1]
        d_positions.reverse()
        pre_d = copy.deepcopy(d_positions)
        b = edge[0] - edge[1]
        for position in pre_d:
            if edge == position:
                continue

            new_y,new_x  = position[0], position[1]

            new_y = position[1] + b
            new_x = position[0] - b

            d_positions.append([new_y, new_x])

    for d in d_positions:
        positions.append(d)

for i in range(100):
    for j in range(100):
        if [j,i] not in positions:
            continue
        if [j+1, i] not in positions:
            continue
        if [j+1 , i+1] not in positions:
            continue
        if [j, i+1] not in positions:
            continue
        result +=1
'''

graph = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):
    
    y, x, d, g = map(int, input().split())
    graph[x][y] = 1

    curve = [d]
    for j in range(g):
        for k in range(len(curve) - 1, -1, -1):
            curve.append((curve[k] + 1) % 4)

    for j in range(len(curve)):
        x += dx[curve[j]]
        y += dy[curve[j]]
        if x < 0 or x >= 101 or y < 0 or y >= 101:
            continue

        graph[x][y] = 1

result = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 0:
            continue
        if graph[i + 1][j] == 0:
            continue
        if graph[i][j + 1] == 0:
            continue
        if graph[i + 1][j + 1] == 0:
            continue

        result +=1


print(result)