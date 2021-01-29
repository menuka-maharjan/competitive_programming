#sparse arrays
n=int(input())
l=[]
l1=[]
for i in range(n):
    x=input()
    l.append(x)
q=int(input())
for i in range(q):
    y=input()
    l1.append(y)
l2=[l.count(y) for y in l1]
for x in l2:
    print(x)
