q=int(input())
l=[]
while(q!=0):
    xyz=list(map(int,input().rstrip().split()))
    x=int(xyz[0])
    y=int(xyz[1])
    z=int(xyz[2])
    a=abs(z-x)
    b=abs(z-y)
    if(a<b):
        l.append("Cat A")
    elif(a>b):
        l.append("Cat B")
    else:
        l.append("Mouse C")  
    q-=1
for x in l:
    print(x)
        
    
    
