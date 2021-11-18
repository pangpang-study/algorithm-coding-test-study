import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [0] * m * n

for i in range(n):
    array[i] = list(map(int, input().rstrip()))

Max = min(n, m)
length = Max

result = 0

while length > 1:
    for i in range(n - length + 1):
        for j in range(m - length + 1):
            if array[i][j] == array[i][j + length - 1] == array[i + length - 1][j] == array[i + length - 1][j + length - 1]:
                result = length * length
                print(result)
                exit()
            
    length -= 1

print(1)