global result
result = 0

def recur(start):
    global result
    if start >= len(str):
        return result

    if str[start] == ')' or ']':
        print(0)
        exit()

    elif str[start] == '(':
        if str[start + 1] == ')':
            result += 2
            start += 2
            recur(start)

        elif str[start + 1] == '(' or '[':
            start += 1
            result += 2 * recur

        else:
            print(0)
            exit()

    else:
        if str[start + 1] == ']':
            result += 3
            start += 2
            recur(start)

        elif str[start + 1] == '(' or '[':
            start += 1
            result += 3 * recur

        else:
            print(0)
            exit()

str = str(input())

print(recur(0))