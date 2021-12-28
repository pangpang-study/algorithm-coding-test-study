import sys


def backtrack(answer, v_cnt, c_cnt, depth, l, c, visited, start):
    if depth == l:
        if v_cnt >= 1 and c_cnt >= 2:
            print(answer)
        return
    for i in range(start, c):
        if visited[i]:
            continue
        visited[i] = True
        if seq[i] in vowel:
            backtrack(answer + seq[i], v_cnt + 1, c_cnt, depth + 1, l, c, visited, i)
        else:
            backtrack(answer + seq[i], v_cnt, c_cnt + 1, depth + 1, l, c, visited, i)
        visited[i] = False


def solution(l, c):
    seq.sort()
    visited = [False] * c
    backtrack("", 0, 0, 0, l, c, visited, 0)


if __name__ == "__main__":
    L, C = map(int, sys.stdin.readline().rstrip().split())
    seq = list(map(str, sys.stdin.readline().rstrip().split()))
    vowel = {'a', 'e', 'i', 'o', 'u'}
    solution(L, C)
