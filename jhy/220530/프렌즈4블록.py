def erase(m, n, board):
    to_erase = set()
    for x in range(m-1):
        for y in range(n-1):
            if board[x][y] == board[x+1][y] == board[x][y+1] == board[x+1][y+1] != '':
                to_erase.add((x, y))
                to_erase.add((x+1, y))
                to_erase.add((x, y+1))
                to_erase.add((x+1, y+1))
    return to_erase

def clean(m, n, board):
    for i in range(m-1, -1, -1):
        for j in range(n):
            board = move_down(m, i, j, board)
    return board
            
def move_down(m, x, y, board):
    cur = x
    for i in range(x, m - 1):
        if cur + 1 >= m or board[cur + 1][y] != '':
            break
        board[cur + 1][y], board[cur][y] = board[cur][y], board[cur + 1][y]
        cur += 1
    return board        
            

def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    while True:
        erase_list = list(erase(m, n, board))
        if erase_list == []:
            break
        else:
            for x, y in erase_list:
                board[x][y] = ''
            board = clean(m, n, board)
    for i in range(m):
        answer += board[i].count('')
    return answer

solution(m, n, board)