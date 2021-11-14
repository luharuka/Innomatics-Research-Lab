import numpy as np
n,m,p=map(int,input().split())
arr=np.array([input().strip().split() for _ in range(n+m)],int)
arr=np.reshape(arr,(n+m,p))
print(arr)
