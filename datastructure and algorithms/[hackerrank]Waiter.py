nq = input().split()
n = int(nq[0])
q = int(nq[1])
number = list(map(int, input().rstrip().split()))
l= 2
u = 10000
prime = [i for i in range(l,u+1) if all(i % j != 0 for j in range(2, i))]
l1= [[] for i in range(q + 1)] 
l2= [[] for i in range(q + 1)] 
l1[0] = number
for i in range(q):
    for j in range(len(l1[i])):
        n = l1[i].pop()
        if n % prime[i] == 0:
            l2[i].append(n)
        else :
            l1[i+1].append(n)
for i in range(len(l2)):
    while(l2[i]!=[]):
        print(l2[i].pop(),)
for i in range(len(l1)):
    while(l1[i]!=[]):
        print(l1[i].pop(),)

