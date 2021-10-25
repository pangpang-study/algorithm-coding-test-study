import sys
input = sys.stdin.readline

n= int(input())

num_list = list(map(int, input().split()))

plus , minus, multipler , divider = map(int, input().split())

start = num_list[0]
INF = 1e9
max_cal = -INF
min_cal = INF


def calculate (idx , cal_result , plus , minus, multipler , divider ):
    global max_cal
    global min_cal

    if idx == n-1:
        max_cal = max(max_cal , cal_result)
        min_cal = min(min_cal , cal_result)
        return 

    if plus >0:
        calculate( idx+1 , cal_result + num_list[idx+1]  ,plus-1 , minus, multipler , divider )
    if minus >0:
       
        calculate( idx+1 , cal_result - num_list[idx+1]  ,plus , minus-1, multipler , divider )
    if multipler >0:
        
        calculate( idx+1 , cal_result * num_list[idx+1]  ,plus , minus, multipler -1, divider  )
    if divider >0:

        calculate( idx+1 , int(cal_result / num_list[idx+1])  ,plus , minus, multipler , divider -1 )
calculate(0,num_list[0] , plus , minus, multipler , divider )

print(max_cal)
print(min_cal)