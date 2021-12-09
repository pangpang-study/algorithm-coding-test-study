import sys
input = sys.stdin.readline

testCount = int(input())

for i in range(testCount):
    start_x, start_y, end_x, end_y = map(int, input().split())
    n = int(input())
    
    result = 0 
    
    for j in range(n):

        planet_x, planet_y, pl_distance = map(int, input().split())
        distance_pl_to_start = (((start_x - planet_x) ** 2) + ((start_y - planet_y) ** 2)) ** 0.5 
        distance_pl_to_end = (((end_x - planet_x) ** 2) + ((end_y - planet_y) ** 2)) ** 0.5 
        
        if distance_pl_to_start < pl_distance and distance_pl_to_end < pl_distance: 
            continue
        elif distance_pl_to_start < pl_distance: 
            result += 1
        elif distance_pl_to_end < pl_distance: 
            result += 1
    
    print(result)