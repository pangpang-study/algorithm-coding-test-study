import sys


def update_min(tmp):
    global crossword
    if len(tmp) >= 2 and crossword > tmp:
        crossword = tmp


def solution(r, c):
    global crossword

    for i in range(r):
        tmp = ""
        for j in range(c):
            if board[i][j] == "#":
                update_min(tmp)
                tmp = ""
                continue
            tmp += board[i][j]
        update_min(tmp)

    for j in range(c):
        tmp = ""
        for i in range(r):
            if board[i][j] == "#":
                update_min(tmp)
                tmp = ""
                continue
            tmp += board[i][j]
        update_min(tmp)


if __name__ == "__main__":
    R, C = map(int, sys.stdin.readline().split())
    crossword = "z" * max(R, C)

    board = []
    for _ in range(R):
        board.append(list(sys.stdin.readline().rstrip()))

    solution(R, C)
    print(crossword)
