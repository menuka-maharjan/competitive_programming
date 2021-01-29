# Enter your code here. Read input from STDIN. Print output to STDOUT#permutation
from itertools import permutations
sk=input().split()
s=sk[0]
k=int(sk[1])
s=s.upper()
l1=list(permutations([s[i]for i in range(len(s))],k))
l1.sort()
for x in l1:
    print(''.join(x))
