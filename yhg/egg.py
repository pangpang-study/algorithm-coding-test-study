import sys
input = sys.stdin.readline

n = int(input())

egg = []
result = 0
for i in range(n):
   egg.append(list(map(int, input().split())))


def fight(egg , idx , count):
    global result
    if idx == n:
        result = max(count, result)
        return

    if egg[idx][0] <=0 :
        fight(egg , idx +1, count)
    else:
        hit_flag = False
        for i in range(n):
            if egg[i][0] <= 0 or i == idx:
                continue
            hit_flag = True;
            egg[idx][0] -= egg[i][1]
            egg[i][0] -= egg[idx][1]
            left =False
            right=False
            if egg[idx][0] <= 0 :
                count +=1
                left = True
            if egg[i][0] <= 0 :
                count +=1
                right = True
            fight(egg,idx+1,count)
            egg[idx][0] += egg[i][1]
            egg[i][0] += egg[idx][1]
            if left :
                count -=1
            if right:
                count -=1
        if  hit_flag ==False:
            fight(egg,idx+1,count)

        
fight(egg , 0, 0)

print(result)
        

