import sys


def get_min(li, limit):
    li.sort()
    if len(li) < limit:
        return 1
    return li[max(0, len(li)-limit)]


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    classes = []
    for _ in range(N):
        P, L = map(int, sys.stdin.readline().split())
        classes.append(get_min(list(map(int, sys.stdin.readline().split())), L))
    classes.sort()
    answer = 0
    for c in classes:
        if M-c < 0:
            break
        M -= c
        answer += 1
    print(answer)

