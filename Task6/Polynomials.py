import numpy as np

arr=input().split()
arr=np.array(arr,dtype=float)
val=int(input())
print(np.polyval(arr,val))


