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
    answer = 0
    
    not_default = set()
    for i in alphabets:
        not_default.update(i - default)
        
    if len(default) + len(not_default) <= k:
        print(n)
        exit()
        
    comb = list(combinations(not_default, k - 5))
    #print("comb: ", comb)
    for case in comb:
        result = 0
        for word in alphabets:
            #print("set(case) - word: ", set(case) - word)
            if word - set(case) == set():
                result += 1
        answer = max(answer, result)
    #print("result: ", result)
    
    print(answer)