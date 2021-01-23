#zipped
nx=input().split()
n=int(nx[0])
x=int(nx[1])
l1=[]
for i in range(x):
    l=list(map(float,input().split()))
    l1.append(l)
for i in zip(*l1):
    a=sum(i)/len(i)
    print(a)
