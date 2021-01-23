#athlete sort
n,m=map(int,input().split())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
k=int(input())
l.sort(key=lambda x: x[k])
for x in l:
    print(*x,sep=' ')
    
    
