import math
q = int(input())
l=[]
for j in range(q):
    ab=input().split()
    a=int(ab[0])
    b=int(ab[1])
    c=math.floor(math.sqrt(b)-math.ceil(math.sqrt(a))+1)
    l.append(c)
for x in l:
    print(x)
