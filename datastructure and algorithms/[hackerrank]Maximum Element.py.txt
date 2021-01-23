l=[]
l2=[]
n=int(input())
for _ in range(n):
    ab=input().split()
    a=int(ab[0])
    if(a==1):
        b=int(ab[1])
        l.append(b)
        if(len(l2)):
            if(b>l2[-1]):
                l2.append(b)
            else:
                x=l2[-1]
                l2.append(x)
        else:
            l2.append(b)
    elif(a==2):
        if len(l)==[]:
            pass
        else:
            l.pop()
            l2.pop()
    elif(a==3):
        if len(l)==[]:
            pass
        else:
            print(l2[-1])
