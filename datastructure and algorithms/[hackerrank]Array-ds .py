#array ds
n=int(input())
a=list(map(int,input().rstrip().split()))
i=n
while(i!=0):
    print(a[i-1],end=" ")
    i-=1
