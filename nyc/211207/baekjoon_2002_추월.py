import sys


def solution(n):
    answer = 0
    for i in range(n):
        tmp = set()
        for j in range(i):
            tmp.add(before[j])
        for j in range(n):
            if after[j] == before[i]:
                break
            if after[j] in tmp:
                tmp.remove(after[j])
        if tmp:
            answer += 1
    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    before = [sys.stdin.readline().rstrip() for _ in range(N)]
    after = [sys.stdin.readline().rstrip() for _ in range(N)]
    print(solution(N))
