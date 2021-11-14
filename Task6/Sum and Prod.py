import numpy as np
m,n=map(int,input().split())
arr=np.array([input().strip().split() for _ in range(m)],dtype=int)
final=np.sum(arr,axis=0)
print(final.prod())



