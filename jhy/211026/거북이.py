import sys

def rect(order):
    x, y = 0, 0
    Max_x, Max_y, Min_x, Min_y = 0, 0, 0, 0
    #           북,동,남,서
    x_direct = [0, 1, 0, -1]
    y_direct = [1, 0, -1, 0]

    idx = 0

    for i in order:
        if i == 'F':
            x += x_direct[idx]
            y += y_direct[idx]
            Max_x = max(Max_x, x)
            Max_y = max(Max_y, y)
            Min_x = min(Min_x, x)
            Min_y = min(Min_y, y)

        elif i == 'B':
            x -= x_direct[idx]
            y -= y_direct[idx]
            Max_x = max(Max_x, x)
            Max_y = max(Max_y, y)
            Min_x = min(Min_x, x)
            Min_y = min(Min_y, y)

        elif i == 'R':
            if idx == 3:
                idx = 0
            else:
                idx += 1
        else:
            if idx == 0:
                idx = 3
            else:
                idx -= 1
    print((Max_x - Min_x) * (Max_y - Min_y))

input = sys.stdin.readline

t = int(input())

for i in range(t):
    order = str(input())
    rect(order)