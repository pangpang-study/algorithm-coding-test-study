import sys
input = sys.stdin.readline
n = int(input())

board = []
for i in range(n):
    board.append(list(input().rstrip()))
head = []
heart = []
left_leg = []
right_leg = []
hurry = []
break_flag = False

for i in range(n):
    
    if break_flag:
        break
    
    
    for j in range(n):
        if board[i][j] == "*":
            head = [i,j]
            break_flag = True
            break


heart = [head[0] +1  , head[1] ]

left_leg_length = 0
right_leg_length = 0
left_arm_length = 0
right_arm_length = 0
hurry_length = 0

for i in range(heart[1]-1 , -1 , -1 ):
    if board[heart[0]][i] != "*":
        break
    left_arm_length +=1

for i in range(heart[1]+1 , n):
    if board[heart[0]][i] != "*":
        break
    right_arm_length +=1

for i in range(heart[0]+1 ,n):
    if board[i][heart[1]] != "*":
        hurry = [i-1, heart[1]]
        break
    hurry_length +=1


for i in range(hurry[0]+1 , n ):
    if board[i][hurry[1]-1] != "*":
        break
    left_leg_length +=1


for i in range(hurry[0]+1 , n ):
    if board[i][hurry[1]+1] != "*":
        break
    right_leg_length +=1


print(heart[0] +1 , heart[1] + 1)
print(left_arm_length, right_arm_length, hurry_length,left_leg_length , right_leg_length)