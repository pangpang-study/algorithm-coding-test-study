import sys


def change_guilty(i, n, guilty):
    global dead

    new_guilty = []
    for j in range(n):
        if dead[j]:
            new_guilty.append(0)
        else:
            new_guilty.append(guilty[j] + R[i][j])
    return new_guilty


def solution(n, night_cnt, total, guilty):
    global dead, answer

    if dead[mafia]:
        answer = max(answer, night_cnt)
        return

    if total % 2 == 0:      # night
        for i in range(n):
            if i == mafia:
                continue
            if not dead[i]:
                dead[i] = True
                new_guilty = change_guilty(i, n, guilty)
                solution(n, night_cnt + 1, total - 1, new_guilty)
                dead[i] = False
    else:
        idx = 0
        maximum = 0
        for i in range(n):
            if maximum < guilty[i]:
                maximum = guilty[i]
                idx = i
        dead[idx] = True
        solution(n, night_cnt, total - 1, guilty)
        dead[idx] = False


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    Guilty = list(map(int, sys.stdin.readline().split()))
    R = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    mafia = int(sys.stdin.readline().rstrip())
    dead = [False] * N
    answer = 0
    solution(N, 0, N, Guilty)
    print(answer)

