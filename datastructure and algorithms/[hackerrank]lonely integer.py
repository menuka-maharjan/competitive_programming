#unique number
n=int(input())
l=list(map(int,input().split()))
x=0
for i in l:
    x=x ^ i
print(x)
    
