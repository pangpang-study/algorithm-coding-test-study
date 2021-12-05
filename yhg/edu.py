import sys
from collections import deque
input = sys.stdin.readline


n , k = map(int, input().split())

words = []
know_alpha = set()
know_alpha.add('a')
know_alpha.add('n')
know_alpha.add('t')
know_alpha.add('i')
know_alpha.add('c')
result = 0 

for i in range(n):
    w = deque(input().rstrip())
    for j in range(4):
        w.pop()
        w.popleft()
    words.append(w)
visited = {'a','n','t','i','c'}


def learn(start ,know_alpha):
    global k ,result , visited

    pre_result = 0
    if len(know_alpha) > k:
        return 
    elif len(know_alpha) <k :
        for i in range(start , 26):
            if chr(97+i) not in know_alpha :
                if know_alpha not in visited:
                    visited.add(chr(97+i))
                    know_alpha.add(chr(97+i))
                    learn(i,know_alpha)
                    know_alpha.remove(chr(97+i))
    else:
        for word in words:
            flag = True
            for w in word:
                if w not in know_alpha:
                    flag = False
            if flag:
                pre_result +=1
        result = max(pre_result , result)
                    
learn(0,know_alpha)
print(result)
