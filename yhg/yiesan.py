import sys
input = sys.stdin.readline

n = int(input())

request = list(map(int, input().split()))

bg = int(input())
request = sorted(request)
start = 0
end = request[-1]

while start <= end:
    mid =(start+ end)//2
    count = 0 
    
    for req in request:
        if req > mid :
            count += mid
        else:
            count += req

    if count >  bg:
        end = mid - 1
    else:
        start = mid + 1
        
print(end)