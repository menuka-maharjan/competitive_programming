import numpy as np
a=np.array(list(map(int,input().rstrip().split())))
b=np.array(list(map(int,input().rstrip().split())))
np.set_printoptions(legacy='1.13')
print(np.inner(a,b))
print(np.outer(a,b))
