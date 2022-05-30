import sys
from collections import deque


def update(candidate):
    if len(candidates) == n:
        if candidate not in candidates.keys():
            idx = list(candidates.values()).index(min(candidates.values()))
            del candidates[list(candidates.keys())[idx]]
        
    if candidate not in candidates.keys():
            candidates[candidate] = 1
    else:
        candidates[candidate] += 1
    
    return list(candidates.keys())


def solution(n):
    for _ in range(recommend):
        candidate = number.popleft()
        result = update(candidate)
    result.sort()
    for i in range(len(result)):
        print(result[i], end=" ")


n = int(input())
recommend = int(input())
number = deque(map(int, input().split()))
candidates = {}

solution(n)