import sys


def solution():
    keys = sorted(trees.keys())
    for key in keys:
        print(key, format((trees[key]/total)*100, ".4f"))


if __name__ == "__main__":
    trees = dict()
    total = 0
    while tree := sys.stdin.readline().rstrip():
        if tree in trees:
            trees[tree] += 1
        else:
            trees[tree] = 1
        total += 1
    solution()