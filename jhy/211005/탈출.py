def connected(field):
    new_field = [[False]* 6 for i in range(12)]

    while field:
        for y in range(12):
            for x in range(6):
                if field[y][x] != '.':
                    puyo = field[y][x]
                    new_field[y][x] = True
                    count = 1
                   

def dfs(word, field, x, y):
    count = 0
    while :
        for i in range(4):
            
            X = x + dx[i]
            Y = y + dy[i]
            if field[y][x] == word and 0 <= x <= 5 and 0 <= y <= 11
                count += 1
    return count

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

field = [list(map(str, input())) for i in range(12)]