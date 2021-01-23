bnm = input().split()

b = int(bnm[0])

n = int(bnm[1])

m = int(bnm[2])

l1 = list(map(int, input().rstrip().split()))

l2 = list(map(int, input().rstrip().split()))
l3=[]
l4=[]
for i in l1:
    z=[x+i for x in l2 if (x+i)<=b]
    l3.append(z)
for i in l3:
    l4.extend(i)
if(len(l4)==0):
    print("-1")
else:    
    print(max(l4))          
