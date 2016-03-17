import numpy as np
import matplotlib.pyplot as plt
zz = np.array([ [5,0], [0,0] ]) 
xx, yy = zip(*zz)
plt.figure()
ax = plt.gca()
ax.quiver(xx,yy, angles='xy',scale_units='xy',scale=1)
ax.set_xlim([0,10])
ax.set_ylim([-1,10])
plt.draw()
plt.show()
