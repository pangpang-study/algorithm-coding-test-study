import sys
from itertools import combinations

def solution(k):
    answer = 0
    if k < 0:
        return answer

    bit_list = [2 ** i for i in range(21)]
    for comb in combinations(bit_list, k):
        count = 0
        candidate = sum(comb)
        for word in words:
            if word & candidate == word:
                count += 1
        answer = max(answer, count)
    return answer

alpha_to_bit = {'b': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5,
                'h': 6, 'j': 7, 'k': 8, 'l': 9, 'm': 10,
                'o': 11, 'p': 12, 'q': 13, 'r': 14, 's': 15,
                'u': 16, 'v': 17, 'w': 18, 'x': 19, 'y': 20, 
                'z': 0}

N, K = map(int, sys.stdin.readline().split())
words = []
reserved = ['a', 'n', 't', 'i', 'c']
for _ in range(N):
    tmp = 0
    for e in set(sys.stdin.readline().rstrip()[4:-4]) - set(reserved):
        tmp |= (1 << alpha_to_bit[e])
    words.append(tmp)
print(solution(K - 5))  