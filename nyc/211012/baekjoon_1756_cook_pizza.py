import sys


def solution(d):
    prev = 0
    for i in range(1, d):
        if oven[i] < oven[prev]:
            prev = i
        oven[i] = oven[prev]

    pizza.reverse()
    for i in range(d-1, -1, -1):
        if oven[i] >= pizza[-1]:
            pizza.pop()
        if not pizza:
            break
        oven.pop()
    return len(oven)


if __name__ == "__main__":
    D, N = map(int, sys.stdin.readline().split())
    oven = list(map(int, sys.stdin.readline().split()))
    pizza = list(map(int, sys.stdin.readline().split()))
    print(solution(D))
