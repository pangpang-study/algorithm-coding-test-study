import sys

input = sys.stdin.readline

def calculate(operators_index, a, b):
    if operators_index == 0:
        result = a + b
    elif operators_index == 1:
        result = a - b
    elif operators_index == 2:
        result = a * b
    else:
        if a < 0:
            result = -(-a // b)
            #a 부호만 확인하는 이유는 b의 경우 항상 a 이상이기 때문에 음수가 될 수 없음
        else:
            result = a // b

    return result

def recur(max_depth, depth, result):
    global Max, Min

    if depth == max_depth:
        Max = max(Max, result)
        Min = min(Min, result)
        return

    for i in range(len(operators)):
        if operators[i] != 0:
            operators[i] -= 1
            recur(max_depth, depth + 1, calculate(i, result,  numbers[depth]))
            operators[i] += 1

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

Max = -int(1e9)
#가능한 수의 최소값
Min = int(1e9)
#가능한 수의 최댓값

recur(n, 1, numbers[0])
#n이 2 이상이기 때문에 초기값을 넣어주면서 depth는 1로 시작

print(Max)
print(Min)