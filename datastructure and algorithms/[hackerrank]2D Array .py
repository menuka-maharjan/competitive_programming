#2D array ds
a=[]
for i in range(6):
    a.append(list(map(int,input().rstrip().split())))
b=[]
for j in range(4):
    for i in range(4):
        b.append(a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2])
print(max(b))
