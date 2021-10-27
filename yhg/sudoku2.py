import sys
input = sys.stdin.readline

board = []
test = []
result = []
for i in range(9):
    board.append(list(input().rstrip()))

def candi_num(i,j):
    num = ['1','2','3','4','5','6','7','8','9']

    for k in range(9):
        if board[i][k] in num:
            num.remove(board[i][k])
    for k in range(9):
        if board[k][j] in num:
            num.remove(board[k][j])

    i = i//3
    j = j//3

    for k in range(i *3 , i *3 +3 ):
        for l in range(j * 3  , j* 3 + 3):
            if board[k][l] in num :
                num.remove(board[k][l])

    return num 

is_finish = False
def find_answer(n):
    global is_finish
    if is_finish:
        return

    if n == len(test): 
        is_finish = True
        for row in board:
            print("".join(row))
        return 
    else:
        i, j = test[n]
        test_nums = candi_num(i, j)
        for test_num in test_nums :
            board[i][j] = str(test_num)  
            find_answer(n+1)
        board[i][j] = '0'


for i in range(9):
    for j in range(9):
        if board[i][j] == '0':
            test.append([i,j])

find_answer(0)

