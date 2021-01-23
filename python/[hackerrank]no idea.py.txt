# Enter your code here. Read input from STDIN. Print output to STDOUT
#no idea
nm=input().split()
n=int(nm[0])
m=int(nm[1])
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
a=set(l1)
b=set(l2)
c1=0
c2=0
for x in l:
    if x in a:
        c1+=1
    if x in b:
        c2-=1
print(c1+c2)
