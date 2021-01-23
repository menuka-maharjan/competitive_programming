import numpy as np
a=np.array(list(map(int,input().rstrip().split())))
np.set_printoptions(legacy='1.13')
print(np.reshape(a,(3,3)))
