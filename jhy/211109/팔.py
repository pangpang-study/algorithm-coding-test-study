l, r = map(str, input().split())

if len(l) != len(r):
    print(0)
    
elif l == r:
    print(l.count('8'))
    
else:   #l r 서로 다른 값이면서 자릿수 같은 경우
    idx = 0
    count = 0
    while idx < len(l):
        if l[idx] == r[idx]:
            if l[idx] == '8':
                count += 1
            idx += 1
        else:
            break
    print(count)