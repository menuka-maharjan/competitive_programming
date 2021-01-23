#and product
n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    d=b-a+1
    res=0
    for i in range(0,32):
        if(d>(1<<i)):
            pass
        else:
            if((a & (1<<i)) & (b & (1<<i))):
                res+=1<<i
            
    l.append(res)
for x in l:
    print(x)
