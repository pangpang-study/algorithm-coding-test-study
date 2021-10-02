import sys


def solution(h, w):
    answer = 0
    for j in range(h):
        count = 0
        started = False
        for i in range(w):
            if board[i][j]:
                started = True
                answer += count
                count = 0
            elif started:
                count += 1
    return answer


if __name__ == "__main__":
    H, W = map(int, sys.stdin.readline().split())
    board = []
    block = list(map(int, sys.stdin.readline().split()))
    for b in block:
        board.append([True]*b + [False]*(H-b))
    print(solution(H, W))

