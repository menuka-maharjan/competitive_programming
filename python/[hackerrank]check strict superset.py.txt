# Enter your code here. Read input from STDIN. Print output to STDOUT
l=list(map(int,input().split()))
a=set(l)
n=int(input())
l2=[]
for i in range(n):
    l1=list(map(int,input().split()))
    b=set(l1)
    if(b.issubset(a)==True):
        s=a.difference(b)
        if(len(s)>=1):
            l2.append(True)
        else:
            l2.append(False)
    else:
        l2.append(False)
s1=set(l2)
if(len(s1)==1):
    for x in s1:
        print(x)
else:
    print(False)
