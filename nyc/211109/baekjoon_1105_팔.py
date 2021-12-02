import sys


def solution(left, right):
    count = 0
    if len(left) != len(right):
        return count

    for i in range(len(left)):
        if left[i] == right[i]:
            if left[i] == '8':
                count += 1
        else:
            break
    return count


if __name__ == "__main__":
    L, R = map(str, sys.stdin.readline().split())
    print(solution(L, R))
