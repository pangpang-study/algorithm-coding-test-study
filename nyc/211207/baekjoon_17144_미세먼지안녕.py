import copy
import sys
from collections import deque


def air_cleaner_row(r):
    for i in range(r):
        if room[i][0] == -1:
            return i


def spread_dust(x, y, tmp_room, r, c):
    global room

    if room[x][y] <= 0:
        return

    count = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= r or ny >= c or room[nx][ny] == -1:
            continue
        count += 1
        tmp_room[nx][ny] += (room[x][y] // 5)
    tmp_room[x][y] += room[x][y] - ((room[x][y] // 5)*count)


def clean_upper(x, c):
    global room
    que = deque()
    for i in range(1, c - 1):
        que.append(room[x][i])
    for i in range(x, 0, -1):
        que.append(room[i][c - 1])
    for i in range(c - 1, 0, -1):
        que.append(room[0][i])
    for i in range(0, x):
        que.append(room[i][0])

    room[x][1] = 0
    for i in range(2, c - 1):
        room[x][i] = que.popleft()
    for i in range(x, 0, -1):
        room[i][c - 1] = que.popleft()
    for i in range(c - 1, 0, -1):
        room[0][i] = que.popleft()
    for i in range(0, x):
        room[i][0] = que.popleft()


def clean_lower(x, r, c):
    global room
    que = deque()
    for i in range(1, c - 1):
        que.append(room[x][i])
    for i in range(x, r - 1):
        que.append(room[i][c - 1])
    for i in range(c - 1, 0, -1):
        que.append(room[r - 1][i])
    for i in range(r - 1, x, -1):
        que.append(room[i][0])

    room[x][1] = 0
    for i in range(2, c - 1):
        room[x][i] = que.popleft()
    for i in range(x, r - 1):
        room[i][c - 1] = que.popleft()
    for i in range(c - 1, 0, -1):
        room[r - 1][i] = que.popleft()
    for i in range(r - 1, x, -1):
        room[i][0] = que.popleft()


def total_dust(r, c):
    global room
    answer = 2
    for i in range(r):
        for j in range(c):
            answer += room[i][j]
    return answer


def solution(r, c, t):
    global room

    x = air_cleaner_row(r)
    for _ in range(t):
        tmp_room = [[0] * c for _ in range(r)]
        tmp_room[x][0] = -1
        tmp_room[x+1][0] = -1
        for i in range(r):
            for j in range(c):
                spread_dust(i, j, tmp_room, r, c)
        room = copy.deepcopy(tmp_room)
        clean_upper(x, c)
        clean_lower(x+1, r, c)

    return total_dust(r, c)


if __name__ == "__main__":
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    R, C, T = map(int, sys.stdin.readline().split())
    room = []
    for _ in range(R):
        room.append(list(map(int, sys.stdin.readline().split())))
    print(solution(R, C, T))