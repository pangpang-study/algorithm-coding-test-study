import sys
from collections import deque
input = sys.stdin.readline

string = deque(input().rstrip())


count = {'(' : 0 , ')' : 0 , '[' : 0 , ']' : 0}

new_string = deque()

break_flag = True
while string and break_flag :
    s = string.popleft()

    if s == ')':
        cal = 0 
        if len(new_string) == 0:
            break_flag  = False
            break 
        while new_string:
            n_s = new_string.pop()
            if n_s == '(' and cal == 0:
                new_string.append(2)
                break
            elif n_s == '(' and cal != 0 :
                new_string.append(cal*2)
                break
            elif n_s == '[':
                break_flag = False
                break
            else:
                cal += n_s
                
            
    elif s== ']':
        cal = 0
        if len(new_string) == 0:
            break_flag  = False
            break 
        while new_string:
            n_s = new_string.pop()
            if n_s == '[' and cal == 0:
                new_string.append(3)
                break
            elif n_s == '[' and cal != 0 :
                new_string.append(cal*3)
                break
            elif n_s == '(':
                break_flag = False
                break
            else:
                cal += n_s
    else:
        new_string.append(s)


if '(' in new_string or '[' in new_string or not break_flag:
    print(0)
else:
    print(sum(new_string))