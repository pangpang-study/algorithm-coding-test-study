import sys
from collections import deque

input = sys.stdin.readline


def diffusion(room, top, bottom):
    copy_room = [[0] * c for y in range(r)]

    copy_room[top][0], copy_room[bottom][0] = -1, -1
    
    for y in range(r):
        for x in range(c):
            if room[y][x] == -1:
                continue
            
            direction = {'left': True, 'right': True, 'up': True, 'down': True}
            Arc = room[y][x] // 5 + room[y][x] % 5
            around = room[y][x] // 5
            
            if x == 0 or room[y][x - 1] == -1:
                direction['left'] = False
                Arc += around
            if x == c - 1:
                direction['right'] = False
                Arc += around
            if y == 0 or room[y - 1][x] == -1:
                direction['up'] = False
                Arc += around
            if y == r - 1 or room[y + 1][x] == -1:
                direction['down'] = False
                Arc += around
            
            copy_room[y][x] += Arc

            for direct in direction.keys():
                if direction[direct]:
                    if direct == 'left':
                        copy_room[y][x - 1] += around
                    elif direct == 'right':
                        copy_room[y][x + 1] += around
                    elif direct == 'up':
                        copy_room[y - 1][x] += around
                    else:
                        copy_room[y + 1][x] += around
                        
    for y in range(r):
        for x in range(c):
            room[y][x] = copy_room[y][x]                    
    return


def clean_top(top):
    route = deque([])
    for x in room[top][1:]: #청정기 윗 부분 행 끝까지
        route.append(x)
    for y in range(top - 1,0,-1):   #청정기 윗 부분 행 위로 쭉
        route.append(room[y][c - 1])
    for x in range(c - 1,0,-1): #맨 윗 행 1열까지
        route.append(room[0][x])
    for y in range(0,top):  #1열부터 청정기 윗부분까지
        route.append(room[y][0])
    
    room[top][1] = 0
    
    for x in range(2, c):
        room[top][x] = route.popleft()
    for y in range(top - 1,0,-1):
        room[y][c - 1] = route.popleft()
    for x in range(c - 1,0,-1):
        room[0][x] = route.popleft()
    for y in range(0,top):
        room[y][0] = route.popleft()
    return


def clean_bottom(bottom):
    route = deque([])
    for x in room[bottom][1:]:
        route.append(x)
    for y in range(bottom + 1,r):
        route.append(room[y][c - 1])
    for x in range(c - 2,0,-1):
        route.append(room[r - 1][x])
    for y in range(r - 1,bottom,-1):
        route.append(room[y][0])
    
    room[bottom][1] = 0
    
    for x in range(2, c):
        room[bottom][x] = route.popleft()
    for y in range(bottom + 1,r):
        room[y][c - 1] = route.popleft()
    for x in range(c - 2,0,-1):
        room[r - 1][x] = route.popleft()
    for y in range(r - 1,bottom,-1):
        room[y][0] = route.popleft() 
    return
    


def clean_room(top, bottom):
    clean_top(top)
    clean_bottom(bottom)
    return


def get_aircleaner_pos(r):
    for i in range(r):
        if room[i][0] == -1:
            return i, i + 1


def solution(r, c, t):
    top, bottom = get_aircleaner_pos(r)
    for time in range(t):
        diffusion(room ,top, bottom)
        clean_room(top, bottom)
    
    result = 0
    
    for i in range(r):
        result += sum(room[i])
    return result + 2


r, c, t = map(int, input().split())
room = []
for _ in range(r):
    room.append(list(map(int, input().split())))
print(solution(r, c, t))