n=int(input())
l=[]
for j in range(n):
    pxpyqxqy=input().split()
    px=int(pxpyqxqy[0])
    py=int(pxpyqxqy[1])
    qx=int(pxpyqxqy[2])
    qy=int(pxpyqxqy[3])
    x=(2*qx)-px
    y=(2*qy)-py
    l.append(x)
    l.append(y)
for x in range (0,len(l),2):
        print(l[x],l[x+1])
