n = int(input())
l1 = list(map(int, input().rstrip().split()))
x={i:l1.count(i) for i in l1}
z=list(x.values())
k=[]
for i in z:
    p=int(i/2)
    k.append(p)
print(sum(k))    
