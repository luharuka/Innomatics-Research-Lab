import numpy as np
np.set_printoptions(legacy='1.13')
m=int(input())
arr=[(input().strip().split()) for _ in range(m)]
arr=np.array(arr,dtype=float)
print(np.linalg.det(arr))
