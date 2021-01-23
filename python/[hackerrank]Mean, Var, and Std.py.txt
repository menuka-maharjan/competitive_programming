import numpy as np
x,y= map(int, input().split())
z=np.array([input().split() for _ in range(x)],int)
np.set_printoptions(sign=" ")
print(np.mean(z,axis=1))
print(np.var(z,axis=0))
a=np.std(z,axis=None)
print(round(a,12))
