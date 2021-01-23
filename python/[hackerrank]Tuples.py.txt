n=int(input())
l=list(map(int,input().rstrip().split()))
t=tuple(l)
print(hash(t))
    
