import numpy as np

v = np.array([1,5])
w = np.array([3,3])

v.shape = (2,1) # 2 rows, 1 column
w.shape = (2,1)

np.add(v,w)

vv = np.array([4,2])
ww = np.array([-1,2])
vv.shape = (2,1)
ww.shape = (2,1)

np.subtract(vv,ww)
