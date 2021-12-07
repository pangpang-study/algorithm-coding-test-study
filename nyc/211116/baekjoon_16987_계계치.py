import sys


def solution(cur):
    global eggs
    global answer

    count = 0
    for egg in eggs:
        if egg[0] <= 0:
            count += 1
    answer = max(answer, count)

    if cur == len(eggs):
        return

    if eggs[cur][0] <= 0:
        solution(cur+1)
        return

    for i in range(len(eggs)):
        if i == cur or eggs[i][0] <= 0:
            continue
        eggs[cur][0] -= eggs[i][1]
        eggs[i][0] -= eggs[cur][1]
        solution(cur+1)
        eggs[cur][0] += eggs[i][1]
        eggs[i][0] += eggs[cur][1]


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    answer = 0
    eggs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    solution(0)
    print(answer)
