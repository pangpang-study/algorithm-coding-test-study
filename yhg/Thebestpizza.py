import sys
input = sys.stdin.readline

n = int(input())

dow , topping = map(int, input().split())
dow_kcal = int(input())
top_kcal = []
for i in range(n):
    top_kcal.append(int(input()))

top_kcal = sorted(top_kcal)

result = dow_kcal//dow
pizza = dow_kcal
for i in range(n+1):
    if i >= 1:
        pizza += top_kcal.pop()
    
    if result <= pizza //(dow + (topping*i) ):
        result = pizza //(dow + (topping*i) )
    else:
        break

print(result)
