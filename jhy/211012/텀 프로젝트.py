import sys

input = sys.stdin.readline

def test(n):
    team = [False] * (n + 1)

    students = [0] + list(map(int, input().split()))

    for i in range(1, n + 1):
        new_team = []

        if team[i]:
            continue
        
        new_team.append(students[i])

        if students[i] == i:
            team[i] = True
            continue

        for j in range(1, n + 1):
            if team[j]:
                continue
            new_team.append(students[j])
            if new_team[-1] == new_team[0]:
                for k in new_team:
                    team[k] = True
                break

    return team.count(False) - 1

t = int(input())

for i in range(t):
    n = int(input())
    print(test(n))