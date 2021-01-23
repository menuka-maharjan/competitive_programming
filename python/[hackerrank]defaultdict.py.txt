
#defaultdict
from collections import defaultdict
d1= defaultdict(list)
l=[]
nm=input().split()
n=int(nm[0])
m=int(nm[1])
for i in range(n):
    x=input()
    d1[x].append(i+1)
for i in range(m):
    x=input()
    l.append(x)

for i in l: 
    if i in d1:
        print(" ".join( map(str,d1[i]) ))
    else:
        print(-1)
