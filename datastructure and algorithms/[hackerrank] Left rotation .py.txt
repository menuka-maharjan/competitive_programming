nd=input().split()
n=int(nd[0])
d=int(nd[1])
l=list(map(int,input().rstrip().split()))
l1=l[d:]+l[:d]
for x in l1:
    print(x,end=" ")
