import numpy as np

a = np.array([[1,2,2],[4,5,5]], dtype=float)
b = a.copy()
print(a)

if 2 in a[:-1,-2:]:
    print('nigga\n')

x=np.array([1,2,3,4], dtype=int)
y=np.array([1,2,3,4], dtype=float)

c = sorted(y)

print(np.diagonal(a))