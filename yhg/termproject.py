import sys
from collections import deque
input = sys.stdin.readline

t = int(input())


def find_team(p_list, target, visited):
    queue = deque()
    queue.append(target)
    team = deque()
    team.append(target)
    while queue:
        p = queue.popleft()
        pp = p_list[p]
        visited[p]  = True 
        if visited[pp]== False:
            team.append(pp)
            queue.append(pp)
        else:
            if pp in team:
                while True:
                    if team[-1] != pp :
                        team.pop()
                    else:
                        break
                
                team.pop()
            
            return len(team)
            

        

        
result = []

for i in range(t):

    n = int(input())

    p_list = {}

    wanted = list(map (int, input().split()))
    
    team_count =  0 
    
    for idx in range(n):
        p_list[idx + 1] = wanted[idx]
    
    visited = [False] * (n+1)
    
    for p in range(1,n+1):
        if visited[p] == False:
            team_count += find_team(p_list ,p, visited)
            

    result.append(team_count)
    


for i in result:
    print(i)