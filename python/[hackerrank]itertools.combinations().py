#combination
from itertools import combinations
sk=input().split()
s=sk[0]
k=int(sk[1])
s=s.upper()
l=[s[j]for j in range(len(s))]
l.sort()
for i in range(1,k+1):
    l1=list(combinations(l,i))
    l1.sort()
    for x in l1:
        print(''.join(x))
    
