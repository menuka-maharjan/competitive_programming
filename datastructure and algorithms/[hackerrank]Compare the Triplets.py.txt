
a=list(map(int,input().rstrip().split()))
b=list(map(int,input().rstrip().split()))
count1=count2=0
for i in range(0,len(a)):
    if(a[i]>b[i]):
        count1=count1+1
    elif(a[i]<b[i]):
        count2=count2+1
    else:
        pass
print(count1,count2)

