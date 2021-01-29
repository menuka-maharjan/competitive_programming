nk = input().rstrip().split()
n = int(nk[0])
k = int(nk[1])
l1 = list(map(int, input().rstrip().split()))
b = int(input().strip())
z=l1.remove(l1[k])  
avg=int(sum(l1)/2)
if avg==b:
    print("Bon Appetit")
else:
    j=b-avg
    print(int(j))
