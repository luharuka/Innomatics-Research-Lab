import numpy as np
np.set_printoptions(sign=' ')
n=int(input())
a=np.array([input().strip().split() for _ in range(n)],dtype=int)
b=np.array([input().strip().split() for _ in range(n)],dtype=int)
print(np.dot(a,b))


