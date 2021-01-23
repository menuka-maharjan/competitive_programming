
from itertools import combinations_with_replacement
sk=input().split()
s=sk[0]
k=int(sk[1])
s=s.upper()
l=[s[i]for i in range(len(s))]
l.sort()
l1=list(combinations_with_replacement(l,k))
l1.sort()
for x in l1:
    print(''.join(x))
