n, m = map(int,input().split())
for i in range(1,n,2):
    print((".|."*i).center(m,"-"))
print('WELCOME'.center(m,'-'))
i=1
while(2*i<=n):
    print((".|."*(n-2*i)).center(m,"-"))
    i+=1
