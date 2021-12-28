import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


t = int(input())

'''
def countFriend(left,network , net_list):
    network.add(left)
    for name in net_list[left]:
        if name not in network:
            network.add(name)
            countFriend(name , network , net_list)
'''

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
for _ in range(t):
    testTime = int(input())
    parent = dict()
    number = dict()

    for _ in range(testTime):
        x,y = input().rstrip().split()
        
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union (x,y)
        print(number[find(x)])


'''
    for _ in range(testTime):
        network = set()
        left , right = input().rstrip().split()
        if left not in net_list:
            net_list[left] = [right]
        else:
            net_list[left].append(right)


        if right not in net_list:
            net_list[right] = [left]
        else:
            net_list[right].append(left)

        network.add(left)
        countFriend(left , network , net_list)

        print(len(network))
'''