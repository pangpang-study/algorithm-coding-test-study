import sys


def swap(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] ^= 1


def solution(n, m):
    count = 0
    if A == B:
        return count
    for i in range(n-3+1):
        for j in range(m-3+1):
            if A[i][j] != B[i][j]:
                swap(i, j)
                count += 1
            if A == B:
                return count
    return -1


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    A = []
    B = []
    for _ in range(N):
        A.append(list(map(int, sys.stdin.readline().rstrip())))
    for _ in range(N):
        B.append(list(map(int, sys.stdin.readline().rstrip())))
    print(solution(N, M))
