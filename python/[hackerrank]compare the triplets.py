l1=list(map(int,input().split()))
c1=0
l2=list(map(int,input().split()))
c2=0
for i in range(len(l1)):
    if(l1[i]>l2[i]):
        c1+=1
    elif(l1[i]<l2[i]):
        c2+=1
    elif(l1[i]==l2[i]):
        pass
    else:
        pass
print(c1,c2)
    
