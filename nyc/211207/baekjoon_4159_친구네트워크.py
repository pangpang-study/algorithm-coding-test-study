import sys


def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent, count):
    a = find(a, parent)
    b = find(b, parent)
    answer = count[a] + count[b]
    if a < b:
        parent[b] = a
        count[a] = count[b] = answer
    elif a > b:
        parent[a] = b
        count[a] = count[b] = answer
    else:
        answer = count[a]
    return parent, count, answer


def solution(n):
    parent = [i for i in range(n)]
    count = [1 for _ in range(n)]
    for num1, num2 in connections:
        parent, count, answer = union(num1, num2, parent, count)
        print(answer)


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        F = int(sys.stdin.readline().rstrip())
        idx = 0
        connections = []
        name_to_num = dict()
        for _ in range(F):
            name1, name2 = map(str, sys.stdin.readline().split())
            if name1 not in name_to_num:
                name_to_num[name1] = idx
                idx += 1
            if name2 not in name_to_num:
                name_to_num[name2] = idx
                idx += 1
            connections.append([name_to_num[name1], name_to_num[name2]])
        solution(len(name_to_num))
