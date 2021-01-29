#finding percentage
n=int(input())
d={}
for i in range(n):
    xy=input().split()
    x=xy[0]
    y=list(xy[1:])
    d[x]=y
a=input()
l=d.get(a)
b=0
for i in range(len(l)):
    b+=float(l[i])
print("{:.2f}".format(b/3))
