x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])

v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])
def kangaroo(x1,v1,x2,v2):
    for i in range(10000):
        c=c1=0
        
        if((x1+v1==x2+v2) and (c==c1)):
            return "YES"
        x1=x1+v1
        c=c+1
        x2=x2+v2
        c1=c1+1
    return "NO"
z=kangaroo(x1,v1,x2,v2)
print(z)
