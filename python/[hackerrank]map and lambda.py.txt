cube = lambda x:x**3
l1=[]
def fibonacci(n):
    if n==0:
        l1=[0]
    elif n==1:
        l1=[0,1]
    else:
        l1=[0,1]
        for i in range(2,n):
            l1.append(l1[i-1]+l1[i-2])
    return(l1[0:n])

