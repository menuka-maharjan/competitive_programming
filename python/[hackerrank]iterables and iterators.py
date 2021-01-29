#iterables and itertools
from itertools import combinations
n=int(input())
s=input().split()
k=int(input())
l1=list(combinations(s,k))
l2= filter(lambda c: 'a' in c, l1)
print("{0:.3}".format(len(list(l2))/len(l1)))
