n = int(input())

numbers = list(map(int, input().split()))

array = [100] * n
for i in range(n):
    if i == 0:
        array[numbers[i]] = i + 1
        continue

    count = numbers[i]

    for j in range(n):
        if array[j] == 100:
            if count == 0:
                array[j] = i + 1
                break
            else:
                count -= 1

        else:
            continue

print(' '.join(map(str, array)))