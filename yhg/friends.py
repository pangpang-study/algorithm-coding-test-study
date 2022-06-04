from collections import deque
def checker(i,j,board):
    checkList = []

    checkList.append(board[i][j])
    checkList.append(board[i][j+1])
    checkList.append(board[i+1][j])
    checkList.append(board[i+1][j+1])

    index_list = []


    if len(set(checkList)) == 1: 
        index_list = [[i,j] , [i,j+1] , [i+1,j] , [i+1,j+1]]
        return index_list
    else:
        return False
                    


    
def solution(m, n, board):
    answer = 0
    
    for i in range(m):
        board[i] = list(board[i])
    
    while True :
        d_tup = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 :
                    d_list = checker(i,j,board)
                    if d_list:
                        for d in d_list:
                            if d not in d_tup:
                                d_tup.append(d)
                    
                    
    
        if d_tup:
            answer += len(d_tup)
            for d in d_tup:
                board[d[0]][d[1]] = 0 
            
            for l in range(1,len(board)):
                for k in range(len(board[0])):
                    if board[l][k] == 0 and board[l-1][k] != 0 :
                        for h in range(l, 0, -1):
                            board[h][k] = board[h-1][k]
                        board[0][k] = 0 
        else:
            break


    return answer