import sys
input = sys.stdin.readline



n = int(input())

start = {}
end = {}
for i in range(1,n+1):
    car = input().rstrip()
    start[car] = i

for i in range(1,n+1):
    car = input().rstrip()
    end[car] = i


car_list = list(end.keys())
result = set()
for i in range(len(car_list)-1):
    for j in range(i+1 ,len(car_list)):
    
        ordinay = start[car_list[i]] - start[car_list[j]]
        change = end[car_list[i]] - end[car_list[j]]

        if ordinay * change < 0:
            result.add(car_list[i])
            break

print(len(result))

