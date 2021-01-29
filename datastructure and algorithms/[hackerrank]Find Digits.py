t=int(input())
l2=[]
for i in range(t):
    n=int(input())
    y=str(n)
    l=[]
    c=0
    for i in range(len(y)):
        l.append(y[i])
    for x in l:
        if(int(x)!=0):
            if(n%int(x)==0 ):
                c+=1 
    l2.append(c)
for z in l2:
    print(z)
                
