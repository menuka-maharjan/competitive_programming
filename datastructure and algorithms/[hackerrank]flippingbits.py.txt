#flipping bits
q=int(input())
l=[]
for i in range(q):
    n=int(input())
    l.append((~n)+(1<<32))
for x in l:
    print(x)
