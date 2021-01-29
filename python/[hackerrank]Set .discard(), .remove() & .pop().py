#set.discard().remove() and pop()
n = int(input())
s = set(map(int, input().split()))
n1=int(input())
for _ in range(n1):
    ab=input().split()
    a=ab[0]
    if(a=='pop'):
        s.pop()
    elif(a=='remove'):
        b=int(ab[1])
        s.remove(b)
    elif(a=='discard'):
        b=int(ab[1])
        s.discard(b)
    else:
        pass
print(sum(s))
