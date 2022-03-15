import sys
input = sys.stdin.readline


def isPalindrome(s):
    start, end = 0, len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
        
    return True


def solution(s):
    idx = 0
    while not isPalindrome(s[idx:]):
        idx += 1                   
        
    print(len(s) + idx)


s = list(map(str, input().rstrip()))

solution(s)