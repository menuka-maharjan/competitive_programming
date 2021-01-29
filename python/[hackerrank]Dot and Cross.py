import numpy as np
x= int(input())
a=np.array([input().split() for _ in range(x)],int)
b=np.array([input().split() for _ in range(x)],int)
np.set_printoptions(legacy='1.13')
print(np.dot(a,b))
