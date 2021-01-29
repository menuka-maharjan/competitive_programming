n=int(input())
l=list(map(int,input().rstrip().split()))
c1=c2=c3=0
for i in l:
    if(i>0):
        c1=c1+1
    elif(i<0):
        c2=c2+1
    else:
        c3=c3+1

print("%.6f" %(c1/n) )
print("%.6f" %(c2/n))
print("%.6f" %(c3/n))
