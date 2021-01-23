
n = int(input())
arr = map(int, input().split())
arr1=[]
for x in arr:
    if x not in arr1:
        arr1.append(x)
arr1.sort()
print(arr1[-2])
