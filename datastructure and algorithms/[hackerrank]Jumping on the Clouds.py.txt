n=int(input())
l=list(map(int,input().rstrip().split()))
count=0
pos=0
while(pos<=len(l)):
    if(pos+2<len(l) and l[pos+2]==0):
        count+=1
        pos+=2
    elif(pos+1<len(l) and l[pos+1]==0):
        count+=1
        pos+=1
    else:
        pos+=1
print(count)
