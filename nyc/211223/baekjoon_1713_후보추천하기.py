import copy
import sys


def solution(n, r):
    numbers = [[i, 1001, 1001] for i in range(101)]
    frame = set()
    for i in range(r):
        if students[i] in frame:
            numbers[students[i]][1] += 1
            continue
        if len(frame) >= n:
            targets = copy.deepcopy(numbers)
            targets.sort(key=lambda x: (x[1], x[2]))
            frame.remove(targets[0][0])
            numbers[targets[0][0]][1] = 1001
            numbers[targets[0][0]][2] = 1001
        frame.add(students[i])
        numbers[students[i]][1] = 1
        numbers[students[i]][2] = i
    return " ".join(map(str, sorted(list(frame))))


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    R = int(sys.stdin.readline().rstrip())
    students = list(map(int, sys.stdin.readline().split()))
    print(solution(N, R))
