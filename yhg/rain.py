import sys
input = sys.stdin.readline

h, w = map(int, input().split())

w_list = list(map(int, input().split()))

result = 0
for height in range(h,0,-1):
    start_flag = False
    water_count = 0 
    
    for idx in range(w):
        if start_flag == False and w_list[idx] >= height:
            start_flag = True 
        
        elif start_flag == True and w_list[idx] < height:
            water_count += 1
        
        elif start_flag == True and water_count != 0 and w_list[idx] >= height:
            result += water_count
            water_count = 0 
        
print(result)
    