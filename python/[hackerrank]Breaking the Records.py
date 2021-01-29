n=int(input())
l=list(map(int,input().rstrip().split()))
m=l[0]
n=l[0]
c=0
c1=0
for i in l:
    if(n>=i): 
        if(i!=n):
            c=c+1
            n=i
for j in l:
    if(m<=j): 
        if(j!=m):
            c1=c1+1
            m=j        
print(c1,c)
