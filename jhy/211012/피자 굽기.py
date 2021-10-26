import sys

input = sys.stdin.readline

d, n = map(int, input().split())

oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

pre = 0
for i in range(1, d):
    if oven[i] < oven[pre]:
        pre = i
    oven[i] = oven[pre]

pizza.reverse()

for i in range(d - 1, -1, -1):
    if oven[i] >= pizza[-1]:
        pizza.pop()
    if not pizza:
        break
    oven.pop()

print(len(oven))