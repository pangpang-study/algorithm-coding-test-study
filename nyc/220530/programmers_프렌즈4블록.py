def convert_2d_list(m, board):
    game_board = []
    for i in range(m):
        game_board.append([e for e in board[i]])
    return game_board


def get_pop_target(m, n, board):
    targets = set()
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] and board[i][j] != "":
                targets.add((i, j))
                targets.add((i, j+1))
                targets.add((i+1, j))
                targets.add((i+1, j+1))
    return targets, len(targets)


def pop(board, targets):
    for i, j in targets:
        board[i][j] = ""
    return board


def move_down(m, x, y, board):
    cur = x
    for i in range(x, m-1):
        if cur + 1 >= m or board[cur+1][y] != "":
            break
        board[cur+1][y], board[cur][y] = board[cur][y], board[cur+1][y]
        cur += 1
    return board


def drop(m, n, board):
    for i in range(m-1, -1, -1):
        for j in range(n):
            board = move_down(m, i, j, board)
    return board


def solution(m, n, board):
    board = convert_2d_list(m, board)
    answer = 0
    while True:
        targets, count = get_pop_target(m, n, board)
        if count == 0:
            break
        answer += count
        board = pop(board, targets)
        board = drop(m, n, board)
    return answer