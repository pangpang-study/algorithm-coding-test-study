import sys


def cal(op, a, b):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        return -(-a // b) if a < 0 else a // b


def recur(max_depth, depth, result):
    global MAX, MIN
    if depth == max_depth:
        MAX = max(result, MAX)
        MIN = min(result, MIN)
        return

    for i in range(len(ops)):
        if ops[i] != 0:
            ops[i] -= 1
            recur(max_depth, depth+1, cal(i, result, seq[depth]))
            ops[i] += 1


if __name__ == "__main__":
    MAX, MIN = -int(1e9), int(1e9)
    N = int(sys.stdin.readline())
    seq = list(map(int, sys.stdin.readline().split()))
    ops = list(map(int, sys.stdin.readline().split()))
    recur(N, 1, seq[0])
    print(MAX)
    print(MIN)
