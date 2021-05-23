def quick(arr):
    n=len(arr)
    if n<=1:
        return arr
    else:
        pivot=arr[-1]
        arr=arr[:n-1]
    g=[]
    l=[]
    for x in arr:
        if x>pivot:
            g.append(x)
        else:
            l.append(x)
    return quick(l)+[pivot]+quick(g)
arr=list(map(int,input().split()))
print(quick(arr))


   