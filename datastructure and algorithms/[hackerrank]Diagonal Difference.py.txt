n=int(input())
l=[]
for i in range(0,n):
    list=[int(i) for i in input().split()]
    l.append(list)
count=0
s1=0
s2=0
j1=0
j2=n-1
while(count<n):
    s1=s1+l[count][j1]
    s2=s2+l[count][j2]
    count=count+1
    j1=j1+1
    j2=j2-1
print(abs(s1-s2))

