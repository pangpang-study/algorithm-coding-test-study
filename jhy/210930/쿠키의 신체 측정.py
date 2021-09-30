import sys

def heart(n):
    for j in range(n):
        for i in range(n):
            if array[j][i] == '*':
                x = i
                y = j + 1
                return x, y

def left_arm(n):
    length = 0
    (x, y) = heart(n)
    x -= 1
    while True:       
        if array[y][x] == '*':
            x -= 1
            length += 1
        else:
            return length

def right_arm(n):
    length = 0
    (x, y) = heart(n)
    x += 1
    while True:       
        if array[y][x] == '*':
            x += 1
            length += 1
        else:
            return length

def waist(n):
    length = 0
    (x, y) = heart(n)
    y += 1
    while True:       
        if array[y][x] == '*':
            y += 1
            length += 1
        else:
            return length

def left_leg(n):
    length = 0
    (x, y) = heart(n)
    x -= 1
    y += waist(n) + 1
    while True:       
        if array[y][x] == '*':
            y += 1
            length += 1
            if y == n:
                return length
        else:
            return length

def right_leg(n):
    length = 0
    (x, y) = heart(n)
    x += 1
    y += waist(n) + 1
    while True:       
        if array[y][x] == '*':
            y += 1
            length += 1
            if y == n:
                return length
        else:
            return length

n = int(sys.stdin.readline())

global array
array = [list(map(str, sys.stdin.readline())) for i in range(n)]

(x, y) = heart(n)
print(str(y + 1), str(x + 1), end=" ")
print(end='\n')
print(left_arm(n), right_arm(n), waist(n), left_leg(n), right_leg(n))