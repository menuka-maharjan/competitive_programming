t = int(input())
l=[]
for t_itr in range(t):
    n = int(input())
    list1 = list(map(int, input().rstrip().split()))
    r = 1
    for x in list1:
        r *= x
        z=r%1234567
    l.append(z)    
for x in l:
    print(x)
