#collections counter
from collections import Counter
import collections
x=int(input())
l=list(map(int,input().split()))
l1=collections.Counter(l)
n=int(input())
m=0
for i in range(n):
    sp=input().split()
    s=int(sp[0])
    p=int(sp[1])
    if l1[s]:
        m+=p
        l1[s]-=1
print(m)
    
    
