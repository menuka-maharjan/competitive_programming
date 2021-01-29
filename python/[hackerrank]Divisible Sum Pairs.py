nk = input().split()

n = int(nk[0])

k = int(nk[1])

ar = list(map(int, input().rstrip().split()))
count=0
for i in range(0,len(ar)):
    for j in range(i+1,len(ar)):
        if(i<j):
            if((ar[i]+ar[j])%k==0):
                count=count+1
print(count)
                
