import sys
input  = sys.stdin.readline

kind = {}
count = 0

while True:
    tree = input().rstrip()
    if not tree: 
        break

    if tree not in kind:
        kind[tree] = 1
    else:
        kind[tree] += 1

    count +=1


for n in sorted(kind.keys()):
     print('{0} {1:0.4f}'.format(n, kind[n]*100/count))





