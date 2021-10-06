import sys
from collections import deque


def button_a(num):
    return num+1 if num+1 <= 99999 else -1


def button_b(num):
    if num*2 > 99999:
        return -1
    if num == 0:
        return 0
    str_num = str(num*2)
    front = int(str_num[0]) - 1
    return int(str(front) + str_num[1:])


def solution(n, t, g):
    que = deque()
    que.append([n, 0])
    visited = {n}
    while que:
        num, count = que.popleft()
        if count > t:
            break

        if num == g:
            return count

        nxt = button_a(num)
        if nxt != -1 and nxt not in visited:
            visited.add(nxt)
            que.append([nxt, count+1])

        nxt = button_b(num)
        if nxt != -1 and nxt not in visited:
            visited.add(nxt)
            que.append([nxt, count+1])

    return "ANG"


if __name__ == "__main__":
    N, T, G = map(int, sys.stdin.readline().split())
    print(solution(N, T, G))
