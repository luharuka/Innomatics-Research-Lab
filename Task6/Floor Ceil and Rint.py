import numpy as np
np.set_printoptions(sign=' ')
arr=input().split()
arr=np.array(arr,dtype=float)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))

