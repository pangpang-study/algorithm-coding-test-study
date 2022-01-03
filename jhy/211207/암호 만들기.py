from itertools import combinations

l, c = map(int, input().split())

chars = list(map(str, input().split()))
vowel = []
consonant = []

for chr in chars:
    if chr in ['a', 'e', 'i', 'o', 'u']:
        vowel.append(chr)
    else:
        consonant.append(chr)

combs = list(combinations(chars, l))

result = []

for comb in combs:
    comb = list(comb)
    comb.sort()
    vowel_count, consonant_count = 0, 0
    for chr in comb:
        if chr in vowel:
            vowel_count += 1
        else:
            consonant_count += 1
    
    if vowel_count >= 1 and consonant_count >= 2:
        result.append(comb)
        
result.sort()
for i in result:
    print("".join(i))