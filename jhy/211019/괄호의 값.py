global start, count
start = 0
count = 0

def recur(idx):
    global start, count
    result = 0
    
    if string[idx] == '(':
        count += 1
        if string[idx + 1] == ')':
            idx += 2
            if idx >= len(string):
                return 2
            result += (2 + recur(idx))

        elif string[idx + 1] == '(' or '[':
            idx += 1
            if idx >= len(string):
                print(0)
                exit()
            result += 2 * recur(idx)

        else:
            print("wrong")
            print(0)
            exit()

    elif string[idx] == '[':
        count += 1
        if string[idx + 1] == ']':
            idx += 2
            if idx >= len(string):
                return 3
            result += (3 + recur(idx))

        elif string[idx + 1] == '(' or '[':
            idx += 1
            if idx >= len(string):
                print(0)
                exit()
            result += 3 * recur(idx)

        else:
            print("wrong")
            exit()

    start = 2 * count
    
    return result

string = str(input())

if string[start] == (')' or ']'):
    print(0)
    exit()

else:
    answer = 0
    while start < len(string):
        print("result: ", recur(start))
        print("start: ", start)
        print(string[:start + 1])
        answer += recur(start)
    print(answer)