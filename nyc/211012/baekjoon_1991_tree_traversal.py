import sys


def traversal(node):
    global pre, ino, pos
    if node == ".":
        return
    pre += node
    traversal(tree[node][0])
    ino += node
    traversal(tree[node][1])
    pos += node


if __name__ == "__main__":
    pre, ino, pos = "", "", ""
    N = int(sys.stdin.readline().rstrip())
    tree = dict()
    for _ in range(N):
        me, left, right = map(str, sys.stdin.readline().rstrip().split())
        tree[me] = [left, right]
    traversal('A')
    print(pre)
    print(ino)
    print(pos)
