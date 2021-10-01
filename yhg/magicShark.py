import sys

input = sys.stdin.readline

n,m = map(int ,input().split())

board = []

directions  = {1 : (0,-1),
               2 : (-1,-1),
               3 : (-1,0),
               4 : (-1,1),
               5 : (0,1),
               6 : (1,1),
               7 : (1,0),
               8 : (1,-1)
                }
for i in range(n):
    board.append(list(map(int, input().split())))
    
clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]
moved_clouds = set()
new_clouds = set()


bug_copys = [[-1,-1],[1,-1],[1,1],[-1,1]]
for i in range(m):
    d , s  = map(int, input().split())
    
    for cloud in clouds:
        
        cloud[0] += directions[d][0] * (s%n) 
        cloud[1] += directions[d][1] * (s%n) 

        if cloud[0] < 0: 
            cloud[0] += n
        elif cloud[0] >= n:
            cloud[0] -= n

        if cloud[1] < 0 :
            cloud[1] += n
        elif cloud[1] >= n:
            cloud[1] -= n 
        
        board[cloud[0]][cloud[1]] +=1
        moved_clouds.add((cloud[0] , cloud[1]))


    for cloud in clouds:
        copy_count = 0
        for bug_copy in bug_copys:
            copy_x = cloud[0] + bug_copy[0]
            copy_y = cloud[1] + bug_copy[1]
            
            if 0 <= copy_x < n and 0 <= copy_y < n and board[copy_x][copy_y] >= 1:
                copy_count +=1
        board[cloud[0]][cloud[1]]  += copy_count

 
    clouds = []
    for x in range(n):
        for y in range(n):
            if (x,y) in moved_clouds:
                continue
            else:
                if board[x][y] >= 2:
                    board[x][y] -= 2
                    clouds.append([x,y])

    moved_clouds.clear()
    
result = 0
for i in board:
    result += sum(i)

print(result)
    