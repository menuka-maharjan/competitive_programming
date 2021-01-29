n=int(input())
l=list(map(int,input().rstrip().split()))
d={x:l.count(x) for x in l}
l1=list(d.values())
print(sum(l1)-max(l1))

    
