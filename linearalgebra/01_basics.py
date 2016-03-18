import numpy as np
import matplotlib.pyplot as plt
zz = np.array([ [5,0], [0,0] ]) 
xx, yy = zip(*zz)
ww = np.multiply(xx,2)
plt.figure()
ax = plt.gca()
ax.quiver(xx,yy,(10,0), (0,0), angles='xy',scale_units='xy',scale=1)
ax.set_xlim([0,10])
ax.set_ylim([-1,10])
plt.draw()
plt.show()

def componentForm(a, b, fn, aDeg, bDeg):
    return (a * fn(np.radians(aDeg))) + (fn(np.radians(bDeg)) * b)
