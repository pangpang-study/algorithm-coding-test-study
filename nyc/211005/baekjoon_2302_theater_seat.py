import sys


def fibonacci(n):
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]


def solution(n, m):
    fibonacci(n)
    answer = 1
    for i in range(1, m+2):
        gap = fixed_seat[i] - fixed_seat[i-1] - 1
        answer *= dp[gap]
    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    dp = [1, 1] + [0] * (N-1)
    fixed_seat = [0]
    for _ in range(M):
        fixed_seat.append(int(sys.stdin.readline()))
    fixed_seat.append(N + 1)
    print(solution(N, M))

