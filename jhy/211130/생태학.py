import sys

input = sys.stdin.readline
trees = {}
number = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    number += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

tree_set = sorted(trees.items(), key=lambda tree: tree[0])

for i in tree_set:
    print(i[0] + " " + "%.4f" %(round(i[1] * 100 / number, 4)))