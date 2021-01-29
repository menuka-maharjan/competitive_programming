#compress string
s=input()
from itertools import groupby
l= [list(g) for k, g in groupby(s)]
l1=[]
l2=[]
for x in l:
    y=x.count(x[0])
    l1.append(int(x[0]))
    l1.append(y)
i=0
while (i!=len(l1)):
    l2.append((l1[i+1],l1[i]))
    i+=2
for x in l2:
      print(x,end=" ")
    
    
