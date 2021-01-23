ijk = input().split()
i = int(ijk[0])
j = int(ijk[1])
k = int(ijk[2])
c=0
for i in range(i,j+1):
    if((i - int(str(i)[::-1])) % k == 0 ):
        c+=1
print(c)
