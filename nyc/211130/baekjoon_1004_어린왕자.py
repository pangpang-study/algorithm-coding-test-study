import sys


def is_inside(cx, cy, x, y, r):
    return ((cx-x)**2 + (cy-y)**2)**0.5 < r


def solution(x1, y1, x2, y2):
    answer = 0
    for cx, cy, r in circles:
        if is_inside(cx, cy, x1, y1, r) != is_inside(cx, cy, x2, y2, r):
            answer += 1
    return answer


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        X1, Y1, X2, Y2 = map(int, sys.stdin.readline().split())
        N = int(sys.stdin.readline().rstrip())
        circles = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
        print(solution(X1, Y1, X2, Y2))