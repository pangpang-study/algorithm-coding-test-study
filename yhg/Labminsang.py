import sys
import copy 

input = sys.stdin.readline

def object_One (d):
    if d[1] == 1 or d[1] == -1:
        d[1] = 0
    return d

def object_Two (d):
    if d[0] == 1 or d[0] == -1:
        d[0] = 0
    return d

def object_Three (d):
    d[0] , d[1] = -d[1] , -d[0]
    return d

def object_Four (d):
    d[0] , d[1] = d[1] , d[0]
    return d


n, m = map(int, input().split())

board  = []
condi_positions = []
directions = [[1,0],[-1,0],[0,1],[0,-1]]
result = set()

for i in range(n):
    board_input = (list(map(int, input().split())))
    board.append(board_input)

for i in range(n):
    for j in range(m):
        if board[i][j] == 9:
            condi_positions.append([i,j])
            result.add((i,j))


for condi_position in condi_positions:
    for direction in directions:
        d = copy.deepcopy(direction)
        x = condi_position[0]
        y = condi_position[1]

        
        while d[0] != 0 or d[1] != 0 :
            x += d[0]
            y += d[1]

            if 0 <= x < n and 0 <= y < m:
                if (x,y) not in result:
                    result.add((x,y)) 

                if board[x][y] == 1:
                    d = object_One(d)
                elif board[x][y] == 2:
                    d = object_Two(d)
                elif board[x][y] == 3:
                    d = object_Three(d)
                elif board[x][y] == 4:
                    d = object_Four(d)
                elif board[x][y] == 9:
                    break
                
            else:
                break

print(len(result))

