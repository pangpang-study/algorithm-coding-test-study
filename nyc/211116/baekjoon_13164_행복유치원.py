import sys


def solution(n, k):
    gap = [heights[i+1] - heights[i] for i in range(n-1)]
    gap.sort()
    return sum(gap[:n-k])


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    heights = list(map(int, sys.stdin.readline().split()))
    print(solution(N, K))
