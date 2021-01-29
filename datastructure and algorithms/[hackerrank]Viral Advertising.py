l1=[5]
x=5
l2=[]
n=int(input())
for i  in range(n-1):
    z=(x//2)*3
    x=z
    l1.append(z)
for i in l1:
    y=(i//2)
    l2.append(y)
print(sum(l2))

