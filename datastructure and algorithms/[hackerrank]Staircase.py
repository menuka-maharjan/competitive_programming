n=int(input())
i=n-1
for j in range(0,n):
    for k in range(0,i):
        print(end=" ")
    i=i-1
    for k in range(0,j+1):
        print("#",end="")
    print()
