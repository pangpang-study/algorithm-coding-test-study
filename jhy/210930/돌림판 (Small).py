import sys
n, k = map(int, sys.stdin.readline().split())
array = str(sys.stdin.readline().rstrip())
rgb = [0, 0, 0]

if n == 1:
    if array =='R':
        rgb = [n, 0, 0]
    elif array =='G':
        rgb = [0, n, 0]
    else:
        rgb = [0, 0, n]
    print(rgb[0], rgb[1], rgb[2])
    exit()

for i in range(k):
    if n == 2:
        if array[0] == array[1]:
            rgb = [0, 0, 2]
            print(rgb[0], rgb[1], rgb[2])
            exit()
        else:
            if array == "RG" or array == "GB" or array == "BR":
                array = array.replace(array[1],"R")
            else:
                array = array.replace(array[1],"G")

    else:
        array = list(array)
        newArray = [array[-1]] + array + [array[0]]
        for i in range(n):
            if newArray[i] == newArray[i + 1] == newArray[i + 2] or (newArray[i] != newArray[i + 1] and newArray[i + 1] != newArray[i + 2] and newArray[i + 2] != newArray[i]):
                array[i] = 'B'
            elif (newArray[i:i + 3].count('R') == 2 and newArray[i: i + 3].count('G') == 1) or (newArray[i:i + 3].count('G') == 2 and newArray[i: i + 3].count('B') == 1) or (newArray[i:i + 3].count('B') == 2 and newArray[i: i + 3].count('R') == 1):
                array[i] = 'R'
            else:
                array[i] = 'G'
        
print(array.count('R'), array.count('G'), array.count('B'))