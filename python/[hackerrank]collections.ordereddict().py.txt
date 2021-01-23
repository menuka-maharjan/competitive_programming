#ordereddict
from collections import OrderedDict
n=int(input())
od=OrderedDict()
for i in range(n):
    np=input().split()
    n=" ".join(np[0:-1])
    p=int(np[-1])
    if od.get(n):
        od[n]+=p
    else:
        od[n]=p
for x,y in od.items():
    print(x,y)

    
    
