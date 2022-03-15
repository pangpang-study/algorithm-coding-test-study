import sys
input = sys.stdin.readline

def check(start , end , word):
    count = 0
    while start < end :
        if word[start] == word[end]:
            start +=1 
            end -=1
            count +=2
        else:
            return 0 
    if start == end :
        return count +1
    else:
        return count 


word = input().rstrip()




def making(word):
    answer = 0 
    start = 0 
    end = len(word)-1
    while start < end:
        if word[start] == word[end]:
            result = check(start ,end ,word)

            if result == 0 :
                start += 1
            else :
                return 2 * len(word)  - result
        else:
            start +=1

    return 2 * len(word) -1

print(making(word))