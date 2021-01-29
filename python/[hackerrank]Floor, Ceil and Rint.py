import numpy as np
a=np.array(list(map(float,input().rstrip().split())))
np.set_printoptions(sign=" ")
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))
