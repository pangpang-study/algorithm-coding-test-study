def solve(puzzle, r, c):
    global first
    for i in range(r):
        if '#' not in puzzle[i]:
            first = min(first, puzzle[i])
            continue
    
        else:
            start = 0
            for j in range(c):
                if puzzle[i][j] == '#':
                    length = j - start
                    if length >= 2:
                        word = puzzle[i][start:j]
                        first = min(first, word)
                    start = j + 1

                elif j == c - 1:
                    length = j - start + 1
                    if length >= 2:
                        word = puzzle[i][start:]
                        first = min(first, word)

    return first

def change_puzzle(puzzle, r, c):
    result = list()

    for i in range(c):
        str = ''
        for j in range(r):
            str += puzzle[j][i]

        result.append(str)

    return result

import sys

input = sys.stdin.readline

r, c = map(int, input().split())

puzzle = list()

for i in range(r):
    puzzle.append(str(input().rstrip()))

first = 'z' * 400

solve(puzzle, r, c)
solve(change_puzzle(puzzle, r, c), c, r)


print(first)