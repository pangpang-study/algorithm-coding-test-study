import sys
from collections import deque


def game_over(k):
    return False if A.count(0) >= k else True


def rotate(entry, out, n):
    return (entry+n-1) % n, (out+n-1) % n


def move(pos, belts, n):
    nxt_pos = (pos + 1) % n
    if belts[nxt_pos] or A[nxt_pos] == 0:
        return False
    belts[nxt_pos] = True
    belts[pos] = False
    A[nxt_pos] -= 1
    return True


def solution(n, k):
    entry, out = 0, n-1
    robot_pos = deque()
    belts = [False] * 2*n
    answer = 0
    while game_over(k):
        entry, out = rotate(entry, out, 2*n)
        if belts[out]:
            robot_pos.popleft()
            belts[out] = False

        for i in range(len(robot_pos)):
            if move(robot_pos[i], belts, 2*n):
                robot_pos[i] = (robot_pos[i] + 1) % (2*n)
        if belts[out]:
            robot_pos.popleft()
            belts[out] = False

        if A[entry] != 0:
            belts[entry] = True
            A[entry] -= 1
            robot_pos.append(entry)
        answer += 1
    return answer


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    print(solution(N, K))
