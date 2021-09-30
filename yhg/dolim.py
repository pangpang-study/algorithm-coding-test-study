import sys
from collections import deque
from typing import Counter
input = sys.stdin.readline

n,k = map(int, input().split())
board = list(input().rstrip())

board_queue = deque(board)
result = ""
for i in range(k):
    for _ in range(len(board_queue)):
        mid = board_queue.popleft()
        right = board_queue.popleft()
        left = board_queue.pop()
        count_list = [mid, left, right]
        if (mid == right and mid == left and right == left) or (mid != right and mid != left and right != left):
            result += "B"
        else:
            R_count = 0
            G_count = 0
            B_count = 0
            for i in count_list:
                if i == "R":
                    R_count+=1
                elif i == "G":
                    G_count +=1
                else:
                    B_count +=1
            if (R_count==2 and  G_count == 1) or (G_count==2 and  B_count == 1) or (B_count == 2 and R_count == 1):
                result += "R"
            else:
                result += "G"

        board_queue.appendleft(right)
        board_queue.append(left)
        board_queue.append(mid)
    board_queue = deque(result)    
    result = ""
print(board_queue.count("R"),board_queue.count("G"),board_queue.count("B"))        