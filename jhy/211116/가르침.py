import sys
from itertools import combinations

input = sys.stdin.readline

n, k = map(int, input().split())

alphabets= []
default = {'a', 'n', 't', 'i', 'c'}

for _ in range(n):
    word = set(str(input().rstrip()))
    word = word - default
    alphabets.append(word)
#print(alphabets)
    
count = 0

if k < 5:
    print(0)

else:
    if n == 1:
        print(1)
        
    elif k == 5:
        for i in alphabets:
            if len(i) == 5:
                count += 1
    
    else:
        answer = 0
        
        not_default = set()
        for i in alphabets:
            not_default.update(i - default)
        if len(default) + len(not_default) <= k:
            print(n)
            exit()
        comb = list(combinations(not_default, k - 5))
        
        for i in range(len(comb)):
            result = 0
            ele = set(comb[i])
            #print("i: ", ele)
            for j in alphabets:
                #print("j: ", j)
                if j & ele == j:
                    #print(ele & j)
                    result += 1
            answer = max(answer, result)
        #print("result: ", result)
        
        print(answer)