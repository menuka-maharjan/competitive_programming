s=input()
n=int(input())
i=(n//len(s))
j=s.count('a')
x1=i*j
x2=s[:n%(len(s))].count('a')
print(x1+x2)
