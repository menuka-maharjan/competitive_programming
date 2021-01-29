
def countappleorange(x,y,s,t,count,count1):
    for i in apples:
        k=a+i
        x.append(k)
    for j in x:
        if j in range(s,t+1):
            count=count+1
    for i in oranges:
        l=b+i
        y.append(l)
    for o in y:
        if o in range(s,t+1):
            count1=count1+1
    return(count,count1)          
st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
count=0
count1=0

apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
x=[]
y=[]
u,v=countappleorange(x,y,s,t,count,count1)
print(u)
print(v)
