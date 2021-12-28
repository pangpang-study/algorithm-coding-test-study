import sys
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    else:
        root_x = find(parent[x])
        parent[x] = root_x
        return parent[x]


def union(x,y):
    root_x = find(x)
    root_y = find(y)

    if root_x!=root_y:
        parent[root_y] = root_x
        number[root_x] +=number[root_y]


def solution():
    for _ in range(friend_num):
        friend1, friend2 = map(str, input().split())
        
        if friend1 not in parent:
            parent[friend1] = friend1
            number[friend1] = 1
        if friend2 not in parent:
            parent[friend2] = friend2
            number[friend2] = 1
        
        union (friend1, friend2)
        print(number[find(friend1)])

    
test = int(input())

for _ in range(test):
    parent = dict()
    number = dict()

    friend_num = int(input())

    solution()