#collections.deque
from collections import deque
d = deque()
n = int(input())
for _ in range(n):
    ab=input().split()
    a=ab[0]
    if(a=='append'):
        b=int(ab[1])
        d.append(b)
    elif(a=='appendleft'):
        b=int(ab[1])
        d.appendleft(b)
    elif(a=='pop'):
        d.pop()
    elif(a=='popleft'):
        d.popleft()
    else:
        pass
for x in d:
    print(x, end=" ")
