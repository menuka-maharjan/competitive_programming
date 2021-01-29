n=int(input())
x=list(map(int,input().split()))
n1=int(input())
y=list(map(int,input().split()))
x1=set(x)
y1=set(y)
x=x1^y1
z=list(x)
z.sort()
for i in z:
    print(i)

