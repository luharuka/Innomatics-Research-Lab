import numpy as np
m,n=map(int,input().split())
arr=[input().strip().split() for _ in range(m)]
arr=np.array(arr,dtype=int)
t=np.min(arr,axis=1)
print(max(t))



