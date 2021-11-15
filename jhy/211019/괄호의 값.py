def recur(idx, pre):
    count = 0
    flag = True
    while idx < len(str):
        if str[idx] == ")":
            if pre == "(":
                if count == 0:
                    count = 1
                return 2 * count, idx + 1
            else:
                flag = False
                break
        if str[idx] == "]":
            if pre == "[":
                if count == 0:
                    count = 1
                return 3 * count, idx + 1
            else:
                flag = False
                break
        if str[idx] == "(" or "[":
            inner, idx = recur(idx + 1, str[idx])
            count += inner
    if flag and pre == "":
        print(count)
    else:
        print(0)
    exit()

import sys

input = sys.stdin.readline

str = list(input().rstrip())

recur(0, "")