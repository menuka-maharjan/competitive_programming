def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return(arr)
arr=list(map(int,input().split()))
print(bubble(arr))
    