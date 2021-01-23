n = int(input().strip())

s = list(map(int, input().rstrip().split()))

dm = input().rstrip().split()

d = int(dm[0])

m = int(dm[1])
count=0
def birthdaychocolate(s,m,d,count):
    for i in range(0,len(s)):
        sum=0
        for j in range(m):
            sum=sum+s[i+j]
            j=j+1
        if(sum==d):
            count=count+1
        if(i+j==len(s)):
            break
    return count
print(birthdaychocolate(s,m,d,count))
