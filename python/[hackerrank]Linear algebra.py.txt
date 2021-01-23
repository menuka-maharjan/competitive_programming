import numpy as np
x= int(input())
z=np.array([input().split() for _ in range(x)],float)
np.set_printoptions(legacy="1.13")
print(np.linalg.det(z))
