import numpy as np
np.set_printoptions(sign=' ',precision=11,legacy='1.13')
m,n=map(int,input().split())
arr=[input().strip().split() for _ in range(m)]
arr=np.array(arr,dtype=int)
print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print(np.std(arr,axis=None))

