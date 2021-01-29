n= int(input().strip())
l1= list(map(int, input().rstrip().split()))
z=[]
for i in range(1,6):
    z.append(l1.count(i))
for i in range(1,6):
    if l1.count(i)==max(z):
        print(i)
        break
