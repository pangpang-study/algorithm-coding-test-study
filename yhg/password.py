import sys
from types import resolve_bases
input = sys.stdin.readline

l , c = map(int, input().split())

alpha = list(input().rstrip().split())
alpha.sort()
v_list = ["a" ,"e" , "i" , "o" , "u"]
result = []
def check(pass_com , consonant ,vowel, idx):
    if len(pass_com) == l:
        if consonant >= 2 and vowel >= 1:
            result.append(pass_com)
            return 

    for i in range(idx , c):
        if visited[i] == 0 :
            pass_com += alpha[i]
            visited[i] = 1
            c_flag = False
            v_flag = False
            if alpha[i] in v_list:
                vowel+=1
                v_flag = True

            else:
                consonant +=1
                c_flag = True

            check(pass_com , consonant, vowel,i+1 )

            visited[i] = 0 
            if v_flag :
                vowel-= 1 

            if c_flag :
                consonant -= 1    
    
            pass_com = pass_com[:-1]
        else:
            continue
        

        
        
visited = [0] * c
check ("" , 0,0, 0)

for r in result:
    print(r)