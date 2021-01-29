import numpy as np
nmp=input().split()
n=int(nmp[0])
m=int(nmp[1])
p=int(nmp[2])
l=np.array([input().split() for i in range(n)],int)
l1=np.array([input().split() for i in range(m)],int)
print(np.concatenate((l, l1), axis = 0))

