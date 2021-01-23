n=int(input())
l=list(map(int,input().rstrip().split()))
print(len(l))
for i in range(n):
    z=min(l)
    p=[x-z for x in l]
    y=p.count(0)
    a=len(p)-y
    l1=[x for x in p if x!=0]  
    l=l1
    i+=a
    if(a==0):
        break
    print(a)
